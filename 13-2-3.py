from PIL import Image
image1 = Image.open('lab12-1-lenna.PNG')
# 이미지 자르기 crop함수 이용 ex. crop(left,up, rigth, down)
croppedImage1 = image1.crop((0, 0, 256, 256))
croppedImage1.show()
croppedImage1.save('croppedImage1.PNG')

croppedImage2 = image1.crop((0, 256, 256, 512))
croppedImage2.show()
croppedImage2.save('croppedImage2.PNG')

croppedImage3 = image1.crop((256, 0, 512, 256))
croppedImage3.show()
croppedImage3.save('croppedImage3.PNG')

croppedImage4 = image1.crop((256, 256, 512, 512))
croppedImage4.show()
croppedImage4.save('croppedImage4.PNG')
# 이미지 사이즈 변경
img_resized = image1.resize((64,64))
# 변경한 이미지 출력
img_resized.show()
img_resized.save('img_resized.PNG')

