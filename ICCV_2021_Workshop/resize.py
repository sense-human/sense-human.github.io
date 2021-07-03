import cv2
img = cv2.imread('wanli_ouyang.jpg')
new_img = img[150:, :, :]
cv2.imwrite('new.png', new_img)
