import streamlit as st
import pokebase as pb
from PIL import Image
from io import BytesIO
import requests
import pandas as pd


st.header("POKEDEX")
st.markdown("---")

tab_pokemons_with_names, tab_search_pokemon_data = st.tabs(["Pokedex", "Procurar dados de um Pokemon"])


with tab_pokemons_with_names:
    n = 3
    base_url = "https://pokeapi.co/api/v2/pokemon/"

    data = {
        "names": [],
        "imgs": []
    }

    for i in range(1, 100):
        try:
            url = f"{base_url}{i}/"
            response = requests.get(url)
            if response.status_code == 200:
                names = response.json()
                name = names['name']
                data['names'].append(name)

            im = pb.SpriteResource("pokemon", i, back=False)
            img = Image.open(BytesIO(im.img_data))
            data["imgs"].append((img, name))
        except:
            pass

    groups = [data["imgs"][i:i + n] for i in range(0, len(data["imgs"]), n)]

    cols = st.columns(n)
    for group in groups:
        for i, (img, name) in enumerate(group):
            cols[i].image(img, caption=name)

with tab_search_pokemon_data:
    df = pd.read_csv("./data/pokedex.csv")
    st.dataframe(df)
    st.selectbox(options = df.name.to_list(), label = "Escolha")