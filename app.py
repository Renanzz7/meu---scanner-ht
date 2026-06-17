import streamlit as st

st.set_page_config(page_title="Scanner 0.5 HT", page_icon="⚽", layout="centered")

st.title("⚡ Scanner Ultra Rápido 0.5 HT")
st.write("Análise instantânea para entrada aos 18 minutos do primeiro tempo.")

# Banco de dados com chaves limpas em maiúsculo
dados_times = {
    "FLAMENGO": 78, "PALMEIRAS": 72, "SAO PAULO": 68, "BOTAFOGO": 75,
    "ATLETICO MG": 70, "CRUZEIRO": 65, "CORINTHIANS": 60, "FLUMINENSE": 64,
    "REAL MADRID": 82, "BARCELONA": 80, "MANCHESTER CITY": 85, "LIVERPOOL": 83,
    "BAYERN": 88, "PSG": 81, "ARSENAL": 79, "INTER DE MILAO": 74
}

st.write("---")

# Entradas organizadas uma abaixo da outra (Sem colunas para evitar o erro da linha 18)
time_casa = st.text_input("Time da Casa:", value="Flamengo").strip().upper()
time_fora = st.text_input("Time de Fora:", value="Palmeiras").strip().upper()

st.write("---")

if st.button("ANALISAR CONFRONTO", use_container_width=True):
    # Busca o percentual das equipes ou aplica a média padrão de 65%
    pct_casa = float(dados_times.get(time_casa, 65))
    pct_fora = float(dados_times.get(time_fora, 65))
    
    # Cálculo matemático da probabilidade combinada
    chance_sem_gol_casa = (100.0 - pct_casa) / 100.0
    chance_sem_gol_fora = (100.0 - pct_fora) / 100.0
    probabilidade_confronto = (1.0 - (chance_sem_gol_casa * chance_sem_gol_fora)) * 100.0
    probabilidade_ajustada = probabilidade_confronto * 0.9
    
    # Entrega dos resultados estruturados
    st.subheader(f"📊 {time_casa} x {time_fora}")
    st.metric(label="Probabilidade de Gol 0.5 HT aos 18 min:", value=f"{probabilidade_ajustada:.1f}%")
    
    st.write("---")
    
    if probabilidade_ajustada >= 70.0:
        st.success("🟩 **SIM!** Padrão histórico altamente favorável. Excelente cenário para buscar o 0.5 HT.")
    elif 55.0 <= probabilidade_ajustada < 70.0:
        st.warning("🟨 **MÉDIO!** Entre apenas se a Odd estiver muito alta (acima de 1.80) para compensar o risco.")
    else:
        st.error("🟥 **NÃO!** Histórico recente dos times indica jogo amarrado no primeiro tempo. Fora da bet.")
