#digitil image is rectangular array of number (where height is numb of row and width is numb of columns)
#image comprised rectangular grid of block called pixel and pixcel is reprseneted by number called intensity valve which is unlimited 
#for D_image is range is from 0 to 255
#grid refer pattren of hor and ver line overlaid on image help framing and layout of image
#two popular format jpeg(join photographic expert group)and PNG(portable network graphics) used to reduce file size and other feature
from PIL import Image
import numpy as np
img=Image.open('b.jpg') #load img and store in obj img
img.show(title="eye") #display  image we will  plot used  matplotlib below
print("will show image extension commonly known as format= ",img.format)
print("will show number of pixel make width and height= ",img.size)
width,height=img.size
print("width=",width)
print("heigth=",height)
print("will show image attribute color space  mean color combination = ",img.mode)
import matplotlib.pyplot as plt
#first image convert to float imshow support only float 
img_array=np.array(img)#convert img to array which is int
print("img_array=",img_array)
img_array=img_array.astype(float) #convert int array to float 
plt.imshow(img_array)
plt.show()

#pillow has a module imageops which is several operation for images
from PIL import ImageOps as pimg
image_gray=pimg.grayscale(img) #convert to gray
image_gray.show()
print("will show imag_gramy mode l mean liminance=",image_gray.mode)
#we can save grayscale image
image_gray.save("eye.jpg")
image_gray.quantize(2)
image_gray=Image.open("eye.jpg") #will load gray image 
#above i upload img image which i can split into its different channel RGB
R,G,B=img.split()
print("red channel=",R) 
#give red channel detail size mode etc
#opencv has more functionalty than pillow its difficult pil is order RGB and opencv is order GBR thay why not show color image
import cv2
img=cv2.imread("b.jpg") #will load img pillow used open() for loading images
arr=np.array(img)
#img.shape(3840,2160,3) #hieght,width,no of channel 3 RGB shpe return dimension of array as tuple and column
cv2.imshow("TERMINAL",arr)
cv2.waitKey(0)#0 untill key presed


