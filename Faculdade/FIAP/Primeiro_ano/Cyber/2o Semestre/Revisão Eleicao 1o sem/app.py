import streamlit as st
import json
import requests as req
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from pyngrok import ngrok


def main():
    html_temp = """
    <div style ="background-color:blue;padding:13px">
    <h1>Linha do tempo!</h1>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    item = st.text_input("Item")

    def verificar_nome(item):
        res = req.get("https://henricobela.github.io/data/json/eleicao.json")
        dict = res.json()["eleicao"]
        lista_fuzzy = process.extract(item, dict)
        resultado = []

        for sublista in lista_fuzzy:
            if sublista[1] > 80:
                resultado.append(sublista)
        if len(resultado) >= 1:
            st.success("Cuidado com as fake news")

    if st.button("Verificar"):
        verificar_nome(item)


if __name__ == "__main__":
    main()
