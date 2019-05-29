import cv2
img = cv2.imread('angjoo-kanazawa.png')
new_img = img[100:1100, 250:1250, :]
cv2.imwrite('new.jpg', new_img)
