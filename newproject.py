import streamlit as st

st.set_page_config(
    page_title="Painel de Estudos",
    page_icon="📚",
    layout="wide"

)

st.title("Painel de Estudos")
st.subheader("Registre e visualize seus estudos diários")

st.sidebar.header("Seus hábitos de estudo")
horas = st.sidebar.slider("Horas estudadas no dia", 0, 7, 4)
pausas = st.sidebar.slider("Número de pausas", 0, 5, 3)
tipo_atividade = st.sidebar.selectbox("Tipo de atividade realizada", ["Leitura", "Exercícios", "Revisão", "Nenhum"])

st.metric("Horas", f"{horas}horas")
st.metric("Pausas", f"{pausas}pausas")
st.metric("Tipo de atividade realizada", tipo_atividade)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Detalhes do seu Estudo")
    st.write("Hoje cumpriu a meta!" if horas >= 7 else "Recupare amanhã sem falta!")

with col2:
    st.header("Quantidade de Pausas")
    st.write("Ótimas pausas!" if pausas >= 5 else "Não estrapole e durma mais a noite")

with col3:
    st.header("Atividade Realizada")
    st.write("Leitura, Exercício, Revisão" if tipo_atividade != "Nenhum" else "Nenhuma das opções")


with st.expander("Ler recomendações"):
    st.write("-Durma pelo menos 7 horas para evitar pausas maiores")
    st.write("-Assista videoaulas")
    st.write("-Se alongue durante suas pausas")


st.markdown("---")
st.markdown("Projeto com streamlit")



