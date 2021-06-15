

import cv2


cap = cv2.VideoCapture(0) # To open a video pr image , cv2.VideoCapture(filename.extension)
print(cap.isOpened())
print("The Width of the frame is:" , cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("The Width of the frame is:" , cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: break

cap.release()
cv2.destroyAllWindows()
