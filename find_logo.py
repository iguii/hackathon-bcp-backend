import cv2
import pytesseract
from pytesseract import Output

# Configuración de pytesseract para usar OCR en macOS
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

def recognize_bank(image_path):
    # Cargar la imagen
    img = cv2.imread(image_path)
    
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Usar pytesseract para extraer texto
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(gray, config=custom_config)
    
    # Lista de bancos conocidos
    banks = {
        "BancoSol": "BancoSol",
        "BCP": "BCP",
        "nco bi": "Banco Bisa",
        "BNB": "BNB",
        "Banco Ganadero": "Banco Ganadero",
        "Mercantil Santa Cruz": "Mercantil Santa Cruz"
    }
    
    # Verificar si alguno de los bancos conocidos está en el texto extraído
    for bank_key in banks.keys():
        if bank_key.lower() in text.lower():
            return banks[bank_key]
    
    return "Banco no reconocido"

# Lista de imágenes de ejemplo
image_paths = [
    "./test/g.jpeg"
    # "./imgs/bancosol.jpeg",
    # "./imgs/bcp.jpeg",
    # "./imgs/bisa.jpeg",
    # "./imgs/bnb.jpeg",
    # "./imgs/ganadero.jpeg",
    # "./imgs/mercantil.jpeg"
]

# Reconocer cada banco
for image_path in image_paths:
    bank_name = recognize_bank(image_path)
    print(f"La imagen {image_path} es del banco: {bank_name}")
