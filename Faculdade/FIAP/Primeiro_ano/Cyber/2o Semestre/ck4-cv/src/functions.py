import streamlit as st
import pandas as pd
import numpy as np
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import string
import matplotlib.pyplot as plt
import numpy as np
import random
from PIL import Image, ImageDraw, ImageFont
from skimage import transform as tf


def config():
    """
    Esta função é responsavel por configurar as features da pagina do streamlit
    """
    st.set_page_config(
        page_title="Santander", layout="centered", initial_sidebar_state="expanded"
    )
    st.header("Checkpoint Cyber 4")
    # st.image("Santander-Logo.png")
    st.write(
        "Esta aplicação recebe uma selfie que identifica se a pessoa está usando um relogio ou não, para realizar a autenticação!"
    )
    st.write("Insira sua imagem abaixo!")


def random_generator(size=6, chars=string.ascii_letters + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def create_captcha(text, shear=0, size=(200, 40), scale=1):
    im = Image.new("L", size, "black")
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(r"src/Coval-Black.ttf", 22)
    draw.text((2, 2), text, fill=1, font=font)

    image = np.array(im)

    affine_tf = tf.AffineTransform(shear=shear)
    image_tf = tf.warp(image, affine_tf)

    return image_tf / image_tf.max()


def process_image(image):
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    return normalized_image_array


def switch_page(page_name: str):
    """
    Esta função é resposavel por direcionar a pagina do streamlit desejada
    """
    from streamlit import _RerunData, _RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")

    page_name = standardize_name(page_name)

    pages = get_pages("main.py")

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise _RerunException(
                _RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")
