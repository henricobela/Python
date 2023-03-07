from src.functions import *


text = "c2R410j"
captcha = create_captcha(text=text, shear=0.65)


def main():
    config()

    st.image(captcha)

    text_captcha = st.text_input("Captcha: ")
    button_captcha = st.button("Verificar", key="captcha")

    if button_captcha:
        if text_captcha == text:
            st.success("Captcha correto!")
            st.balloons()
            switch_page("correct")
        else:
            st.error("Captcha Incorreto!!!")


if __name__ == "__main__":
    main()
