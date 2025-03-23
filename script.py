from PIL import Image
import pillow_heif

heif_file = pillow_heif.open_heif(r"C:\cd69-python\Python\python\IMG_1000.HEIC")
image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data)
image.save(r"C:\cd69-python\Python\python\IMG_1000converted.jpg", "JPEG")
print("保存完了")
