import cv2 as cv
import numpy as np
import math
prev = 0
nap_prev = 0

#video capture:
cam = cv.VideoCapture(0)
if not cam.isOpened():
    print("Cannot open camera")
    exit()

fw = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
fh = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

def find_centroid(canvas, num_active_pixel):
    li = []
    for i in range(500):
        for j in range(500):
            if canvas[i, j][0] == 255:
                num_active_pixel = num_active_pixel+1
                li.append([i, j])
    linp = np.array(li)
    centroid = np.mean(linp, axis = 0)

    return centroid, canvas, num_active_pixel

def ik(x, y, z, elbow='down'):

    # base angle
    theta1 = math.atan2(z, x)

    L1, L2 = 9, 7.5

    # planar coordinates after rotating by -theta1
    r = math.sqrt(x*2+ z*2)
    s = y
    d = math.sqrt(r*2 + s*2)

    D = (d*2 - L1**2 - L2*2) / (2 * L1 * L2)
    if D > 1.0 or D < -1.0:
        raise ValueError("Target unreachable: outside workspace (|D|>1).")

    # choose elbow configuration
    if elbow == 'down':
        sign = 1
    else:
        sign = -1
    theta3 = math.atan2(sign * max(0, math.sqrt(1 - D**2)), D) 

    # shoulder
    phi = math.atan2(s, r)
    psi = math.atan2(L2 * math.sin(theta3), L1 + L2 * math.cos(theta3))
    theta2 = phi - psi

    theta1 *= 180/(math.pi)
    theta2 *= 180/(math.pi)
    theta3 *= 180/(math.pi)
    return theta1, theta2, theta3

z = 0

while True:
    num_active_pixel = 0

    #frame
    ret, frame = cam.read()
    frame = cv.resize(frame, (fw, fh))
    frame = cv.GaussianBlur(frame, (7,7), sigmaX= 1.0)

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    #frame processing
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    ret,img = cv.threshold(gray,80,255,cv.THRESH_BINARY_INV)
    canvas = np.full((500,500,3), (0,0,0), dtype=np.uint8) 

    #contours
    contours, _ = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    if contours:
        our_obj = max(contours, key= cv.contourArea)
        x1, y1, w, h = cv.boundingRect(our_obj)
        cv.drawContours(canvas, [our_obj], -1, (255, 255, 255), -1)

    centroid, canvas, num_active_pixel = find_centroid(canvas, 0)
    
    if num_active_pixel > 0:
        
    
        nap_prev = num_active_pixel
    
        prev = centroid
        x = float(centroid[0])*2/3
        y = float(centroid[1])*2/3
        z = num_active_pixel/500

        theta1, theta2, theta3 = ik(x, y, z, elbow='down')

        #print(theta1, theta2, theta3)
        cv.circle(frame, (int(centroid[1]), int(centroid[0])), 5, (0, 0, 255), -1)
        cv.rectangle(frame, (x1,y1), (x1+w, y1+h), (0,255,255),2)
        cv.putText(frame, f"theta1={theta1: .2f}  theta2={theta2: .2f}  theta3={theta3: .2f}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        

    #show
    cv.imshow('threshold_img', img)
    cv.imshow("canvas", canvas)
    cv.imshow("frame", frame)
    if cv.waitKey(1) == ord('q'):
        break
    


# When everything done, release the capture
cam.release()
cv.destroyAllWindows()