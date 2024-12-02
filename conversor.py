from PIL import Image

# Abrir o arquivo .webp
webp_image = Image.open(r"C:\Users\jhona\Downloads\prompt.webp")

# Converter para .jpg
jpg_image = webp_image.convert("RGB")

# Salvar a imagem como .jpg
jpg_image.save(r"C:\Users\jhona\Downloads\fiverr_p.jpg", "JPEG")
print("pronto")
