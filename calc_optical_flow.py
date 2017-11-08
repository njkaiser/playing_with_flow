import cv2
import numpy as np

frame1 = cv2.imread('IMG_0050.JPG')
frame2 = cv2.imread('IMG_0089.JPG')
frame3 = cv2.imread('IMG_0131.JPG')
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)

# print frame1.shape[:2][0]
# print frame1.shape[:2][1]

# Python: cv2.calcOpticalFlowFarneback(prev, next, pyr_scale, levels, winsize, iterations, poly_n, poly_sigma, flags[, flow])
    # prev - first 8-bit single-channel input image.
    # next - second input image of the same size and the same type as prev.
    # flow - computed flow image that has the same size as prev and type CV_32FC2.
    # pyr_scale - parameter, specifying the image scale (<1) to build pyramids for each image; pyr_scale=0.5 means a classical pyramid, where each next layer is twice smaller than the previous one.
    # levels - number of pyramid layers including the initial image; levels=1 means that no extra layers are created and only the original images are used.
    # winsize - averaging window size; larger values increase the algorithm robustness to image noise and give more chances for fast motion detection, but yield more blurred motion field.
    # iterations - number of iterations the algorithm does at each pyramid level.
    # poly_n - size of the pixel neighborhood used to find polynomial expansion in each pixel; larger values mean that the image will be approximated with smoother surfaces, yielding more robust algorithm and more blurred motion field, typically poly_n =5 or 7.
    # poly_sigma - standard deviation of the Gaussian that is used to smooth derivatives used as a basis for the polynomial expansion; for poly_n=5, you can set poly_sigma=1.1, for poly_n=7, a good value would be poly_sigma=1.5.
    # flags -
    # operation flags that can be a combination of the following:
    #
    # OPTFLOW_USE_INITIAL_FLOW uses the input flow as an initial flow approximation.
    # OPTFLOW_FARNEBACK_GAUSSIAN uses the Gaussian \texttt{winsize}\times\texttt{winsize} filter instead of a box filter of the same size for optical flow estimation; usually, this option gives z more accurate flow than with a box filter, at the cost of lower speed; normally, winsize for a Gaussian window should be set to a larger value to achieve the same level of robustness.

flow1 = cv2.calcOpticalFlowFarneback(gray1, gray2, 0.5, 3, 50, 5, 7, 1.5, cv2.OPTFLOW_FARNEBACK_GAUSSIAN)
flow2 = cv2.calcOpticalFlowFarneback(gray2, gray3, 0.5, 3, 50, 5, 7, 1.5, cv2.OPTFLOW_FARNEBACK_GAUSSIAN)

# print np.max(flow1)
# print np.max(flow2)
# print np.shape(flow1)
# print np.shape(flow2)

print "flow1.shape is:", flow1.shape#, flow1.shape[:2][0], flow1.shape[:2][1]
print "flow2.shape is:", flow2.shape#, flow2.shape[:2][0], flow2.shape[:2][1]

for i in xrange(0, flow2.shape[:2][0], 20):
    for j in xrange(0, flow2.shape[:2][1], 20):
        # for j, y in enumerate(flow1.shape[:, :, 1]):
        # if np.sqrt(dx**2 + dy**2) > 1:
        # if i%20==0 and j%20==0:
        dy = int(flow2[i, j, 0])
        dx = int(flow2[i, j, 1])
        cv2.line(frame2, (j, i), (j+dy, i+dx), (255,0,0))
        cv2.line(frame3, (j, i), (j+dy, i+dx), (255,0,0))

while 1:
    # cv2.imshow("frame", frame1)
    # cv2.waitKey(0)
    cv2.imshow("frame", frame2)
    cv2.waitKey(0)
    cv2.imshow("frame", frame3)
    cv2.waitKey(0)

cv2.destroyAllWindows()
