# =============================================================================
# Q1:
# =============================================================================
print('---Q1---')
import statistics as st
x=[3,1.5,4.5,6.75,2.25,5.75,2.25]
print(st.mean(x))#output:3.7142857142857144
print(st.harmonic_mean(x))#output:2.8769027134348115
print(st.median(x))#output:3
print(st.median_low(x))#output:3
print(st.median_high(x))#output:3
print(st.median_grouped(x))#output:3.0
print(st.mode(x))#output:2.25
print(st.pstdev(x))#output:1.8391990270833904
print(st.pvariance(x))#output:3.38265306122449
print(st.stdev(x))#output:1.9865619978819116
print(st.variance(x))#output:3.9464285714285716
# =============================================================================
#Q2: 
# =============================================================================
print('---Q2---')
import random 
print( random.random() )#output:0.9735442342029252
print ( random.randrange(10))#output:0
print ( random.choice(['Ali', 'Khalid' ,'Hussam']))#output: Ali
print ( random.sample(range(1000), 10))#output:[871, 851, 512, 593, 984, 750, 408, 390, 169, 391]
print ( random.choice('Orange Academy'))#output:e
items = [1,5,8,9,2,4] 
random.shuffle(items) 
print( items )#output:[5, 8, 4, 9, 2, 1]
print ( random.randint(20, 30))#output:27
print ( random.randrange(1000,2111, 5))#output:1625
print  ( random.uniform(10000, 11000))#output:10450.229936665924
# =============================================================================
#Q3: 
# =============================================================================
print('---Q3---')
import math
print ('pi: %.40f' % math.pi)#output:pi: 3.1415926535897931159979634685441851615906
print(math.cos(200))#output:0.4871876750070059
print(math.sin(30))#output:-0.9880316240928618
print(math.tan(180))#output:1.3386902103511544
print(math.floor(10.8))#output:10
print(math.ceil(10.8))#output:11
# =============================================================================
#Q4: 
# =============================================================================
print('---Q4---')
from PIL import Image,ImageDraw,ImageFilter
im=Image.open("spring.jpg")
print(im.format,im.size,im.mode)#output: JPEG (1000, 665) RGB
im.show()
image_flip=im.transpose(Image.FLIP_TOP_BOTTOM)
image_flip.show()
greyscale_image=im.convert('L')
greyscale_image.show()
cropped=im.crop((0,0,50,50))
cropped.show()
draw=ImageDraw.Draw(im)
draw.line((0,0)+im.size,fill=(255,255,255))
draw.line((0,im.size[1],im.size[0],0), fill=(255,255,255))
draw.text((im.size[0]/2-im.size[0]/2,im.size[1]/2+20),"yasmin",fill=(255,255,0))
im.show()
newimage=im.filter(ImageFilter.SMOOTH)
newimage1=im.filter(ImageFilter.EDGE_ENHANCE)
newimage2=im.filter(ImageFilter.FIND_EDGES)
newimage3=im.filter(ImageFilter.SHARPEN)
newimage.show()
newimage1.show()
newimage2.show()
newimage3.show()
alpha=0.5
im1=Image.open("snow.jpg").resize(im.size)
Image.blend(im,im1,alpha).save("New.jpg".format(alpha))
imm=Image.open("New.jpg")
imm.show()
blurred=im.filter(ImageFilter.BLUR)
blurred.show()
size=(128,128)
im.thumbnail(size)
im.show()
image_rot_90=im1.rotate(90)
image_rot_90.show()
image1=Image.open("spring.jpg")
image2=Image.open("snow.jpg")
image2=image2.resize(image1.size)
mask=Image.open("mask.png")
mask=mask.resize(image1.size)
Image.composite(image1,image2,mask).save("Image_composite_01.jpg")
imo=Image.open("Image_composite_01.jpg")
imo.show()













