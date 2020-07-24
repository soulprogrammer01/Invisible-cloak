import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.imread('./image.jpg')

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv", hsv)
        red = np.uint8([[[0,0, 255]]])
        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV),

        l_red = np.array([0, 100, 100])
        u_red = np.array([10, 255, 255])

        mask = cv2.inRange(hsv, l_red, u_red)
        #cv2.imshow("mask", mask)
        
        
        #cv2.imshow("part1", part1)
        mask=cv2.morphologyEx(mask, cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
        mask1=cv2.morphologyEx(mask, cv2.MORPH_DILATE,np.ones((3,3),np.uint8))

        mask1 = cv2.bitwise_not(mask)
        part1 = cv2.bitwise_and(back, back, mask=mask)
        part2 = cv2.bitwise_and(frame,frame , mask=mask1)
        #cv2.imshow("part2", part2)

        finalOutput=cv2.addWeighted(part1,1,part2,1,0)


        cv2.imshow("cloak",finalOutput)

        if cv2.waitKey(5) == ord('q'):
            break



cap.release()
cv2.destroyAllWindows()
