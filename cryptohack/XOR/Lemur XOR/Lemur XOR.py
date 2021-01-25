from PIL import Image,ImageChops
flag = Image.open("flag.png").convert("1")
lemur = Image.open("lemur.png").convert("1")
result = ImageChops.logical_xor(flag,lemur)

result.show()
