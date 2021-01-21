from PIL import Image,ImageChops
flag = Image.open("flag.png").convert("1")
lemur = Image.open("lemur.png").convert("1")
result = Image.open("result.png")
flag1 = ImageChops.invert(flag)
lemur1 = ImageChops.invert(lemur)

result1 = ImageChops.logical_or(result,lemur)
result2 = ImageChops.logical_or(flag,result1)
result3 = ImageChops.logical_or(result2,lemur)

result.show()
