import cv2
import sys
import os.path


method = cv2.TM_SQDIFF_NORMED

def check_cli_inputs():
	if len(sys.argv) != 3:
		return False
	return True

def is_valid_file(location):
	if not os.path.isfile(location):
		return False
	if not location.lower().endswith(('.jpg', '.jpeg')):
		return False
	return True


def return_small_large_image(img1, img2):
	if is_valid_file(img1) and is_valid_file(img2):
		first_image = cv2.imread(img1)
		second_image = cv2.imread(img2)

		first_rows,first_cols = first_image.shape[:2]
		second_rows,second_cols = second_image.shape[:2]
		small_image = None
		large_image = None
		if first_rows >second_rows or first_cols > second_cols:
			small_image = second_image
			large_image = first_image
		else:
			small_image = first_image
			large_image = second_image
		return (small_image , large_image)

	else:
		print "Either the file is NOT present or the file is NOT a jpg/jpeg.Please recheck your inputs!"
		sys.exit(-1)

if not check_cli_inputs():
	print "Invalid Number of Arguments!!\n\n"
	print "Input format : "
	print "python is_cropped_image.py file_1.jpg file_2.jpg\n"
	sys.exit(-1)

# Read the images from the file

(small_image , large_image) = return_small_large_image(sys.argv[1] , sys.argv[2])



result = cv2.matchTemplate(small_image, large_image, method)

# We want the minimum squared difference
mn,_,mnLoc,_ = cv2.minMaxLoc(result)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx,MPy = mnLoc

print "(x , y) = (" + str(MPx) + "," + str(MPy) + ")"

print "Cropped Image highlighted in output.jpg"
# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = small_image.shape[:2]

# Step 3: Draw the rectangle on large_image
cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# Display the original image with the rectangle around the match.
cv2.imwrite('output.jpg',large_image)