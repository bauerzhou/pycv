from PIL import Image 

pil_im = Image.open('IMG_0491.jpg').convert('L')
#pil_im.convert('L')
pil_im.save('IMG_0491_gray.jpg')
pth = Image.open('IMG_0491.jpg')
pth.thumbnail((256,256))
pth.save('IMG_0491_thumb.jpg')