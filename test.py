from PIL import Image
# import pytesseract
import pytesseract

# Path of the image
path = r'./imgs/bcp.jpeg'

# Extract the text from the image
print(pytesseract.image_to_string(Image.open(path)))
