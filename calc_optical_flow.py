import cv2
import numpy as np

frame1 = cv2.imread('frame1.png')
frame2 = cv2.imread('frame2.png')
frame3 = cv2.imread('frame3.png')
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)

# print frame1.shape[:2][0]
# print frame1.shape[:2][1]

flow1 = cv2.calcOpticalFlowFarneback(gray1, gray2, 0.5, 3, 15, 5, 5, 1.2, cv2.OPTFLOW_FARNEBACK_GAUSSIAN)
flow2 = cv2.calcOpticalFlowFarneback(gray2, gray3, 0.5, 3, 15, 5, 5, 1.2, cv2.OPTFLOW_FARNEBACK_GAUSSIAN)

# print np.max(flow1)
# print np.max(flow2)
# print np.shape(flow1)
# print np.shape(flow2)

print "flow1.shape is:", flow1.shape, flow1.shape[:2][0], flow1.shape[:2][1]

for i in xrange(0, flow2.shape[:2][0], 20):
    for j in xrange(0, flow2.shape[:2][1], 20):
        # for j, y in enumerate(flow1.shape[:, :, 1]):
        # if np.sqrt(dx**2 + dy**2) > 1:
        # if i%20==0 and j%20==0:
        dy = int(flow2[i, j, 0])
        dx = int(flow2[i, j, 1])
        cv2.line(frame2, (j, i), (j+dy, i+dx), (0,0,255))
        cv2.line(frame3, (j, i), (j+dy, i+dx), (0,0,255))

while 1:
    # cv2.imshow("frame", frame1)
    # cv2.waitKey(0)
    cv2.imshow("frame", frame2)
    cv2.waitKey(0)
    cv2.imshow("frame", frame3)
    cv2.waitKey(0)

cv2.destroyAllWindows()
