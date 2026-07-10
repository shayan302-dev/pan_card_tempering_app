# PAN (Permanent Account Number) Card Tempering Detection

## Description
We will detect tempering of PAN Card using computer vision. This project will help the different organizations in Detecting whether the ID . 
The PAN card provided to them by their employees or customer or anyone is original or not

## Steps
1. Get Image from User
2. Check for size and format of the image
3. Change the shape and size of the image according to the original image
4. Convert the Image in to gray scale
5. Find the Similarity Index of the image
6. Finding the Threshold of the image
7. Finding Contour and grab those contour using imutils
8. Draw a bounding rectangle using these contours
9. plot difference , Threshold original and tempered image
10. Compare all the images and check the similarity score to decide tempering

## Technologies
cv2 
skimage.metrics we import structural_similarity
imutils
from PIL we import Image

## Dataset
I only use a single original PAN Card Picture 

## How to Run
pip install -r requirements.txt
