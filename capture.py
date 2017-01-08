import cv2
import datetime

# Camera 0 is the only camera
camera_port = 0

# Rate of image capture in Hz
rate = 1.0

# Where to save the files
output_dir = "./temp"

# Initialise the cameras
camera = cv2.VideoCapture(camera_port)
 
# Captures a single image from the camera and returns it in PIL format
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = camera.read()
 return im

# Create a display window
cv2.namedWindow('capture')

# Initialise the waitkey return value
c = -1

while c != 1048689: # 1048689 is the 'q' key
  # Take the actual image we want to keep
  camera_capture = get_image()
  
  # Get the current time
  now = datetime.datetime.now()
  
  # Convert from RGB to grayscale
  gray = cv2.cvtColor(camera_capture, cv2.COLOR_RGB2GRAY);
  
  # create a time string and make the filename from it
  t = now.strftime("%Y_%m_%d_%H_%M_%S_%f")
  filename = output_dir + "/" + t + ".png"

  # Save the file
  print "Saving " + filename
  cv2.imwrite(filename, gray)
  
  # Show the image
  cv2.imshow('capture', gray) 
  
  # What the approximate specified wait time
  wait = int(1000/rate)
  c = cv2.waitKey(wait)
  
# Release the camera
del(camera)
