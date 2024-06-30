import cv2
from fastapi import FastAPI, UploadFile, File
from PIL import Image
import pytesseract
from pytesseract import Output

app = FastAPI()

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    # Save uploaded file locally
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    # Open the image file
    image = Image.open(file_path)

    img_cv = cv2.imread(file_path)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(gray, config=custom_config)
    banks = {
        "BancoSol": "BancoSol",
        "BCP": "BCP",
        "banco bisa": "Banco Bisa",
        "BNB": "BNB",
        "Banco Ganadero": "Banco Ganadero",
        "Mercantil Santa Cruz": "Mercantil Santa Cruz"
    }
    bank_name = "Banco Bisa" #change this to Banco no encontrado
    for bank_key in banks.keys():
        if bank_key.lower() in text.lower():
            bank_name = banks[bank_key]
            break
    

    # Perform OCR using pytesseract with Spanish language
    text = pytesseract.image_to_string(image, lang='spa')

    # Clean up the saved file
    import os
    os.remove(file_path)

    return {"filename": file.filename, "text": text, "bank_name": bank_name}
