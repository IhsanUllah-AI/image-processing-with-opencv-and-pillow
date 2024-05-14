import cv2
import numpy as np
img=cv2.imread('a.jpg',cv2.IMREAD_GRAYSCALE)
#every image is id in memory 
print('id of img=',id(img))
#this type copying is only share memory adres now both these refer to same loc
A=img
#will gave same id of img when we change in one will change the other bcs both refer to same addres
print('id of A=',id(A))
#will copy image to B and also give new  id to B  one chnge will not effect other
B=img.copy()
print('id of B=',id(B)) 
##make window normal to display img image 
cv2.namedWindow("B",cv2.WINDOW_NORMAL) #will make window normal to display image in normal as image as 
cv2.imshow("B",B) 
cv2.waitKey(0)
cv2.destroyAllWindows()


#let do some change in A is this change img image
A-=50 #will decrease intensity by 50 chnage A will directly effect img 
#make window normal to display A image 
cv2.namedWindow("A",cv2.WINDOW_NORMAL)
cv2.imshow("A",A)
cv2.waitKey(0)
cv2.destroyAllWindows()
#make window normal to display img image 
cv2.namedWindow("img",cv2.WINDOW_NORMAL)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#let do some change in img is this change A image
img+=30 #will increase intensity by 30 chnage img will directly effect A  
#make window normal to display A image 
cv2.namedWindow("A",cv2.WINDOW_NORMAL)
cv2.imshow("A",A)
cv2.waitKey(0)
cv2.destroyAllWindows()
#make window normal to display img image 
cv2.namedWindow("img",cv2.WINDOW_NORMAL)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()