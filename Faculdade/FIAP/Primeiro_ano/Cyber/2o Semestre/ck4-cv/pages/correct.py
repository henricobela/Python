from src.functions import *

config()

image = st.file_uploader("Choose a file")
verif = st.button("Verificar", key="verif")

if verif:
    try:
        image = Image.open(image)
        if image:
            st.image(image)

        model = load_model("model/keras_model.h5")
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        data[0] = process_image(image)

        prediction = model.predict(data)
        pred_have_watch = prediction[0][0]
        pred_dont_have_watch = prediction[0][1]

        if pred_have_watch > pred_dont_have_watch:
            st.success(
                f"Permitido!!! Selfie com relogio, Precisão: {pred_have_watch:.2f}"
            )
        else:
            st.error(
                f"Negado!!! Selfie sem relogio, Precisão: {pred_dont_have_watch:.2f}"
            )

    except:
        st.warning("Por favor faça o upload de uma imagem")
