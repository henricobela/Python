from source import *

def main():
    st.set_page_config(page_icon = "📜")
    st.header("Sprint Cyber")
    st.subheader("📜 Classificador de selfie com CNH ou Não 📜")

  
    nome = st.text_input("Digite seu Nome")
    endereco = st.text_input("Digite seu endereço")
    num_endereco = st.number_input("Digite o numero do seu endereco", format = "%d", step = 1)
    cep = st.text_input("Digite seu CEP")
    veiculo = st.text_input("Digite a placa do seu Carro")

    col1, col2 = st.columns(2)

    with col1:
        col1_form = col1.form("form_col1")
        image = col1_form.file_uploader(label = f"{nome} Envie aqui sua selfie com CNH!")
        button_image = col1_form.form_submit_button("Ver Imagem")
        if button_image:
            col1_form.image(image)

    with col2:
        col2_form = col2.form("form_col2")
        col2_form.write("Classificar, clique abaixo")
        button_classificar = col2_form.form_submit_button("Classificar")
        if button_classificar:
            col2.write("Classificando...")
            col2_form.image(image)
            pred = classify_photo(image)
            if pred == "Real":
                col2_form.success(f"{nome} Voce pode passar!!!")
                st.balloons()
            elif pred == "Fake":
                col2_form.error(f"{nome} Voce nao pode passar!!!")
                st.snow()


if __name__=="__main__":
    main()
