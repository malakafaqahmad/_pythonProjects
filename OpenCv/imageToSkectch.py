import cv2

img = cv2.imread(r'C:\Users\iafqa\OneDrive\Desktop\python\scrapBasics\image.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

invert_img = cv2.bitwise_not(gray_img)

blurred_img = cv2.blur(invert_img, (21, 21),0)  # Adjust the kernel size (e.g., (5, 5)) as desired

inverted_blurred_img = cv2.bitwise_not(blurred_img)

sketched_img = cv2.divide(gray_img, inverted_blurred_img, scale = 256.0)

cv2.imshow('orignal image', img)
cv2.imshow('skeched image', sketched_img)


cv2.waitKey(0)