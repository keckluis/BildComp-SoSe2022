import cv2 as cv
import numpy as np

line0 = []
line1 = []
def click(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print('mouse click at: ' + str(x) + ', ' + str(y))
        if len(line0) < 2:
            line0.append([x,y])
        elif len(line1) < 2:
            line1.append([x, y])
        
        if len(line0) == 2:
            cv.line(img, (line0[0][0], line0[0][1]), (line0[1][0], line0[1][1]), (255,0,0), 5)
        
        if len(line1) == 2:
            cv.line(img, (line1[0][0], line1[0][1]), (line1[1][0], line1[1][1]), (255,0,0), 5)
            intersection()

    cv.imshow(title, img)

def intersection():
    cp0 = np.cross([line0[0][0], line0[0][1], 1], [line0[1][0], line0[1][1], 1])
    print('cp0: ' + str(cp0))
    cp1 = np.cross([line1[0][0], line1[0][1], 1], [line1[1][0], line1[1][1], 1])
    print('cp1: ' + str(cp1))

    res = np.cross(cp0, cp1)
    res = res/res[2]

    print('result: ' + str(res))
    
img = cv.imread('images/IMG_3232.JPEG', cv.IMREAD_COLOR)

title = 'test'
cv.namedWindow(title,  cv.WINDOW_FREERATIO)
cv.imshow(title, img)
cv.setMouseCallback(title, click)

while True:
    if cv.waitKey(10) == ord('q'):
        break

cv.destroyAllWindows()