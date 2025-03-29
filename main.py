import streamlit as st
import random

# Definição dos estados e suas probabilidades de transição
estados = {
    "s0": [("s1", 0.43), ("s2", 0.27), ("s3", 0.17), ("s4", 0.13)],  
    "s1": [("s5", 0.5), ("s6", 0.3), ("s7", 0.2)],  
    "s2": [("s8", 0.5), ("s9", 0.3), ("s10", 0.2)],  
    "s3": [("s11", 0.5), ("s12", 0.3), ("s13", 0.2)],  
    "s4": [("s14", 0.5), ("s15", 0.3), ("s16", 0.2)],  
    "s5": [("s17", 0.6), ("s18", 0.4)], 
    "s6": [("s19", 0.6), ("s20", 0.4)], 
    "s7": [("s21", 0.6), ("s22", 0.4)], 
    "s8": [("s23", 0.6), ("s24", 0.4)],  
    "s9": [("s25", 0.6), ("s26", 0.4)], 
    "s10": [("s27", 0.6), ("s28", 0.4)], 
    "s11": [("s29", 0.6), ("s30", 0.4)], 
    "s12": [("s31", 0.6), ("s32", 0.4)], 
    "s13": [("s33", 0.6), ("s34", 0.4)], 
    "s14": [("s35", 0.6), ("s36", 0.4)], 
    "s15": [("s37", 0.6), ("s38", 0.4)], 
    "s16": [("s39", 0.6), ("s40", 0.4)], 
}

# Título da página
st.set_page_config(page_title="🚀 Exploração Markov", layout="centered")

# Inicializando variáveis no estado da sessão
if "historico" not in st.session_state:
    st.session_state.historico = [("s0", None, None)]  # [(estado, próximo estado sorteado, número sorteado)]

st.title("🚀 ExploracaoMarkov: Simulação de Estados do Foguete")
st.markdown("---")

# Função para avançar o estado a partir de um estado específico
def avancar_estado(index):
    estado_atual = st.session_state.historico[index][0]  # Estado da transição
    if estado_atual in estados:
        transicoes = estados[estado_atual]

        # Sorteando o próximo estado e pegando o número aleatório usado
        pesos = [t[1] for t in transicoes]
        sorteio = random.uniform(0, sum(pesos))  # Número aleatório para a decisão
        acumulado = 0
        for estado_destino, prob in transicoes:
            acumulado += prob
            if sorteio <= acumulado:
                proximo_estado = estado_destino
                break

        st.session_state.historico.append((proximo_estado, estado_atual, sorteio))
        st.rerun()

# Exibir cada estado do histórico em um bloco separado
for i, (estado, estado_anterior, sorteio) in enumerate(st.session_state.historico):
    with st.container():
        if sorteio is not None:
            st.write(f"🎲 **Porcentagem sorteada:** `{sorteio:.5f}`")

        st.subheader(f"🛰️ Estado {i}: `{estado}`")

        if estado in estados:
            transicoes = estados[estado]
            possibilidades = ", ".join([f"{dest} ({prob:.2f})" for dest, prob in transicoes])
            st.write(f"**🔢 Possibilidades de transição:** {possibilidades}")

        # Apenas o último estado recebe o botão para avançar
        if i == len(st.session_state.historico) - 1:
            if st.button("Avançar 🚀", key=f"botao_{i}"):
                avancar_estado(i)
    
    st.markdown("---")  # Linha divisória entre os estados
