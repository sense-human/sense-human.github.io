import cv2
img = cv2.imread('tinghui-zhou.png')
new_img = img[20:800, :, :]
cv2.imwrite('new.png', new_img)
