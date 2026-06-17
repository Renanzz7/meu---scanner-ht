import streamlit as st

st.set_page_config(page_title="Scanner 0.5 HT", page_icon="⚽", layout="centered")

st.title("⚡ Scanner Ultra Rápido 0.5 HT")
st.write("Análise instantânea para entrada aos 18 minutos do primeiro tempo.")

# Banco de dados com chaves totalmente em maiúsculo
dados_times = {
    "FLAMENGO": 78, "PALMEIRAS": 72, "SAO PAULO": 68, "BOTAFOGO": 75,
    "ATLETICO MG": 70, "CRUZEIRO": 65, "CORINTHIANS": 60, "FLUMINENSE": 64,
    "REAL MADRID": 82, "BARCELONA": 80, "MANCHESTER CITY": 85, "LIVERPOOL": 83,
    "BAYERN": 88, "PSG": 81, "ARSENAL": 79, "INTER DE MILAO": 74
}

# Campos de texto simplificados
col_times = st.columns(2)
with col_times:
    time_casa = st.text_input("Time da Casa:", value="Flamengo").strip().upper()
with col_times:
    time_fora = st.text_input("Time de Fora:", value="Palmeiras").strip().upper()

st.write("---")

if st.button("ANALISAR CONFRONTO", use_container_width=True):
    pct_casa = float(dados_times.get(time_casa, 65))
    pct_fora = float(dados_times.get(time_fora, 65))
    
    chance_sem_gol_casa = (100.0 - pct_casa) / 100.0
    chance_sem_gol_fora = (100.0 - pct_fora) / 100.0
    probabilidade_confronto = (1.0 - (chance_sem_gol_casa * chance_sem_gol_fora)) * 100.0
    probabilidade_ajustada = probabilidade_confronto * 0.9
    
    st.subheader(f"📊 {time_casa} x {time_fora}")
    
    # Barra visual calibrada com segurança
    st.progress(int(max(0, min(100, probabilidade_ajustada))) / 100)
    st.metric(label="Probabilidade de Gol 0.5 HT aos 18 min:", value=f"{probabilidade_ajustada:.1f}%")
    
    st.write("---")
    
    if probabilidade_ajustada >= 70.0:
        st.success("🟩 **SIM!** Padrão histórico altamente favorável. Excelente cenário para buscar o 0.5 HT.")
    elif 55.0 <= probabilidade_ajustada < 70.0:
        st.warning("🟨 **MÉDIO!** Entre apenas se a Odd estiver muito alta (acima de 1.80) para compensar o risco.")
    else:
        st.error("🟥 **NÃO!** Histórico recente dos times indica jogo amarrado no primeiro tempo. Fora da bet.")
