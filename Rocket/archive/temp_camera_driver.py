import cv2
vid = cv2.VideoCapture(0)
fps = 10
width = int(vid.get(3))
height = int(vid.get(4))
fourcc = cv2.VideoWriter_fourcc(*'avc1') 
video_writer = cv2.VideoWriter('out.mp4', fourcc, fps, (width, height)) 
i = 0 
while(i < 100):
 
         ret, frame = vid.read()
         video_writer.write(frame)
         i += 1
 
video_writer.release()
vid.release()
cv2.destroyAllWindows()