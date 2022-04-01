import cv2

def update():
    pass


img=cv2.imread('img/aquarium.jpg')
rainbow=cv2.imread('img/rainbow.png')

cv2.namedWindow('ui')
cv2.createTrackbar('h_min', 'ui', 0, 180, update)
cv2.createTrackbar('s_min', 'ui', 0, 255, update)
cv2.createTrackbar('v_min', 'ui', 0, 255, update)

cv2.createTrackbar('h_max', 'ui', 180, 180, update)
cv2.createTrackbar('s_max', 'ui', 255, 255, update)
cv2.createTrackbar('v_max', 'ui', 255, 255, update)

cv2.imshow('ui', img)
cv2.waitKey(0)



