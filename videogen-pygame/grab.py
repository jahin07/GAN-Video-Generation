import cv2
#print(cv2.__version__)
vidcap = cv2.VideoCapture('/Users/jahinmajumdar/Desktop/video.mov')
success,image = vidcap.read()
count = 0
success = True
while success:
    success,image = vidcap.read()
    print 'Read a new frame: ', success
    cv2.imwrite("/Users/jahinmajumdar/Desktop/frames/frame%d.jpg" % count, image)     # save frame as JPEG file
    count += 1
