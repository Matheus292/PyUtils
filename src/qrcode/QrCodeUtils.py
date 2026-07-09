import qrcode


def gerar_qrcode(texto: str, caminho_saida: str = "qrcode.png", tamanho: int = 10, borda: int = 4):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=tamanho,
        border=borda,
    )
    qr.add_data(texto)
    qr.make(fit=True)

    imagem = qr.make_image(fill_color="black", back_color="white")
    imagem.save(caminho_saida)
    return caminho_saida


if __name__ == "__main__":
    arquivo = gerar_qrcode("https://forms.gle/uarsZDA8ppZemaEL9", "retiro_mulheres.png")
    print(f"QR Code gerado em: {arquivo}")