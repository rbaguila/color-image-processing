# import necessary packages
import numpy as np
import cv2


file_array = [
  ['2.jpg', [60, 55, 75], [80, 255, 255], [80, 90, 120], [255, 173, 157]], 
  ['3.jpg', [60, 55, 75], [80, 255, 255], [120, 100, 125], [255, 173, 133]], 
  ['6.jpg', [60, 55, 75], [80, 255, 255], [20, 133, 77], [255, 173, 127]],
  ['15.jpg', [60, 50, 50], [85, 255, 255], [10, 135, 120], [255, 155, 220]],
  ['33.jpg', [60, 55, 75], [80, 255, 255], [90, 100, 120], [225, 155, 130]],
  ['35.jpg', [60, 55, 75], [80, 255, 255], [55, 140, 100], [225, 165, 127]],
  ['38.jpg', [60, 55, 75], [80, 255, 255], [10, 133, 77], [255, 173, 127]],
  ['N3.jpg',[60, 30, 40], [85, 255, 255], [10, 120, 121], [160, 135, 135]],
  ['N24.jpg',[60, 55, 75], [80, 255, 255], [15, 120, 130], [135, 135, 140]], 
  ['N26.jpg',[60, 55, 75], [80, 255, 255], [10, 120, 129], [125, 135, 140]], 
]

# loading images
#img = cv2.imread("2.jpg")

# getting color range
#green = np.uint8([[[107,150,85 ]]])
#green = np.uint8([[[179,196,123 ]]])
#hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
#print hsv_green

#pig = np.uint8([[[155,162,189 ]]])
#hsv_pig = cv2.cvtColor(pig,cv2.COLOR_BGR2YCR_CB)
#print hsv_pig

# looping all file input
for files in file_array:
  filename = files[0]
   
  #getting green tag
  img_color = cv2.imread(filename)
  lower_green = np.array(files[1],np.uint8)
  upper_green = np.array(files[2],np.uint8)
  img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)
  mask = cv2.inRange(img_hsv, lower_green, upper_green)
  #cv2.imwrite('output/tagnotprocessed_'+files[0], mask)
  kernel = np.ones((15,15), 'uint8')	
  mask = cv2.erode(mask,kernel,iterations=2)
  mask = cv2.dilate(mask,kernel,iterations=2)
  mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel,iterations=3)

  cv2.imwrite('output/tag_'+files[0], mask)
  #getting pig using 
  gray = cv2.cvtColor(img_color,cv2.COLOR_BGR2GRAY)
  img_ycrcb = cv2.cvtColor(img_color, cv2.COLOR_BGR2YCR_CB)
  ycrcb_min = np.array(files[3])
  ycrcb_max = np.array(files[4])
  img_ycrcb = cv2.inRange(img_ycrcb, ycrcb_min, ycrcb_max)
  kernel = np.ones((5,5), 'uint8')
  opening = cv2.morphologyEx(img_ycrcb,cv2.MORPH_OPEN,kernel, iterations = 2)
  cv2.imwrite('output/pig_'+files[0], opening)

# green mark
#lower_green = np.array([60, 55, 75],np.uint8)
#upper_green = np.array([80, 255, 255],np.uint8)
#img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#mask = cv2.inRange(img_hsv, lower_green, upper_green)

# assign a rectangle kernel size for cleaning
#kernel = np.ones((20,20), 'uint8')	
#mask = cv2.erode(mask,kernel,iterations=2)
#mask = cv2.dilate(mask,kernel,iterations=2)
#mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel,iterations=3)
#cv2.imwrite('output/green.jpg', mask)


#pig
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#im_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
#skin_ycrcb_mint = np.array((0, 133, 77))
#skin_ycrcb_maxt = np.array((255, 173, 127))
#skin_ycrcb = cv2.inRange(im_ycrcb, skin_ycrcb_mint, skin_ycrcb_maxt)
#cv2.imwrite('output/dunno.jpg', skin_ycrcb)
#noise removal
#kernel = np.ones((20,20),np.uint8)
#skin_ycrcb = cv2.erode(skin_ycrcb,kernel,iterations=1)
#skin_ycrcb = cv2.dilate(skin_ycrcb,kernel,iterations=2)
#opening = cv2.morphologyEx(skin_ycrcb,cv2.MORPH_OPEN,kernel, iterations = 1)
#cv2.imwrite('output/pig.jpg', opening)
