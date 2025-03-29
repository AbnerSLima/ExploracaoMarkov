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

# Dicionário com as situações de cada estado
situacoes = {
    "s0": ("🚀 Preparação para o lançamento", "Os sistemas estão sendo checados e a contagem regressiva começou!"),
    
        "s1": ("🔥 Decolagem", "O foguete se desprende da base de lançamento e começa a subir."),
            "s5": ("🌍 Deixando a Terra para trás", "O planeta azul já começa a ficar pequeno na visão da tripulação."),
                "s17": ("🌟 Atingindo a órbita", "O foguete entra na órbita terrestre e a missão segue conforme o planejado."),
                "s18": ("🌙 Atingindo a órbita", "O foguete alcança a órbita lunar, pronto para uma missão interplanetária."),
            "s6": ("🌫️ Atravessando a atmosfera", "A nave enfrenta resistência do ar enquanto ganha altitude."),
                "s19": ("🔭 Primeiro vislumbre do espaço", "A vastidão do universo se abre diante dos olhos da tripulação."),
                "s20": ("💫 Acima da atmosfera", "A nave alcança o espaço exterior e a gravidade começa a ser controlada."),
            "s7": ("⚡ Turbulência inesperada", "Algumas oscilações foram detectadas, mas a missão segue."),
                "s21": ("🌀 Superando turbulência", "A nave ajusta sua estabilidade e segue sua trajetória sem maiores problemas."),
                "s22": ("🌪️ Enfrentando tempestades solares", "O foguete atravessa uma zona de intensa atividade solar."),

        "s2": ("🌪️ Condições meteorológicas adversas", "O foguete decola mas precisa ajustar sua trajetória devido a condições climáticas."),
            "s8": ("🛰️ Ajustando trajetória", "O foguete realiza uma manobra para entrar na órbita correta."),
                "s23": ("🛸 Entrada na órbita final", "A nave atinge a órbita desejada para iniciar o próximo estágio da missão."),
                "s24": ("⚙️ Ajuste de velocidade", "O foguete faz um ajuste na velocidade para a entrada na órbita desejada."),
            "s9": ("💨 Ventos solares detectados", "As condições espaciais estão sendo analisadas para ajustes."),
                "s25": ("🌬️ Filtros de vento solar ativados", "A nave ativa os filtros para lidar com o impacto dos ventos solares."),
                "s26": ("⚡ Interferência magnética", "A nave enfrenta interferências magnéticas e a equipe monitora o impacto na trajetória."),
            "s10": ("🛑 Pequena correção de curso", "Os propulsores são ativados para alinhar a nave."),
                "s27": ("🔄 Ajuste completo", "A nave está devidamente ajustada e a missão segue sem mais ajustes."),
                "s28": ("🧭 Precisão nos ajustes", "Os sistemas confirmam que a nave está na trajetória correta."),
        "s3": ("🔧 Pequeno problema técnico", "A equipe monitora um possível ajuste necessário."),
            "s11": ("⚠️ Problema com o sistema de navegação", "O sistema de navegação apresenta falhas e a tripulação trabalha para resolver."),
                "s29": ("🔧 Reparo concluído", "O sistema de navegação foi reparado e a nave continua seu curso."),
                "s30": ("🔍 Diagnóstico em andamento", "A equipe ainda está analisando o problema e buscando soluções."),
            "s12": ("⚡ Falha no sistema de comunicação", "A comunicação com a base de controle foi perdida temporariamente."),
                "s31": ("📡 Reestabelecendo comunicação", "A comunicação foi restaurada e a missão segue com total coordenação."),
                "s32": ("🚨 Comunicação crítica", "A equipe está enfrentando sérias dificuldades de comunicação."),
            "s13": ("🔥 Superaquecimento no motor", "O motor apresenta superaquecimento e a missão precisa ser ajustada."),
                "s33": ("❄️ Resfriamento bem-sucedido", "O sistema de resfriamento é ativado e o motor volta a operar normalmente."),
                "s34": ("💥 Motor comprometido", "O motor está gravemente danificado e a missão está em risco."),
        
        "s4": ("⚠️ Grande problema técnico", "Um grande problema técnico foi detectado! O foguete encontra falhas críticas e a missão corre risco."),
            "s14": ("💔 Perda de comunicação", "A comunicação com a nave foi perdida por completo."),
                "s35": ("📡 Tentando restabelecer comunicação", "As equipes na Terra tentam restabelecer a comunicação com a nave."),
                "s36": ("❌ Comunicação irreparável", "A nave perdeu completamente a comunicação e não é possível reiniciar a missão."),
            "s15": ("🔋 Falha no sistema de energia", "O sistema de energia falhou e a nave está sem energia suficiente para continuar."),
                "s37": ("🔌 Reparos energéticos em andamento", "A equipe está tentando restaurar a energia, mas o tempo está se esgotando."),
                "s38": ("⚡ Falha irreparável de energia", "A nave não tem mais energia para continuar a missão."),
            "s16": ("🛠️ Despressurização da cabine", "A pressão interna da nave caiu drasticamente e a equipe está em risco."),
                "s39": ("🔧 Reparação bem-sucedida", "A cabine foi pressurizada novamente e os sistemas estão estáveis."),
                "s40": ("💨 Perda total de pressão", "A cabine foi despressurizada completamente e a missão foi abortada."),
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

        st.subheader(f"🔸 Estado {i}: `{estado}`")
        
        # Exibir título e descrição da situação
        if estado in situacoes:
            titulo, descricao = situacoes[estado]
            st.markdown(f"### {titulo}")
            st.write(descricao)

        if estado in estados:
            transicoes = estados[estado]
            possibilidades = ", ".join([f"{dest} ({prob:.2f})" for dest, prob in transicoes])
            st.write(f"**🔢 Possibilidades de transição:** {possibilidades}")

        # Apenas o último estado recebe o botão para avançar
        if i == len(st.session_state.historico) - 1:
            if st.button("Avançar 🚀", key=f"botao_{i}"):
                avancar_estado(i)
    
    st.markdown("---")  # Linha divisória entre os estados
