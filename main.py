from fastapi import FastAPI, UploadFile, File
from PIL import Image
import pytesseract

app = FastAPI()

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    # Save uploaded file locally
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    # Open the image file
    image = Image.open(file_path)

    # Perform OCR using pytesseract with Spanish language
    text = pytesseract.image_to_string(image, lang='spa')

    # Clean up the saved file
    import os
    os.remove(file_path)

    return {"filename": file.filename, "text": text}
