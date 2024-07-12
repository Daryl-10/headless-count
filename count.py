import cv2
import numpy as np
import time
import datetime
# import pyautogui

def count_pink_markers(image_path, min_area=10, max_area=100):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define range of pink color in HSV
    lower_pink = np.array([140, 50, 180])
    upper_pink = np.array([170, 255, 255])
    
    # Threshold the HSV image to get only pink colors
    mask = cv2.inRange(hsv, lower_pink, upper_pink)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter contours based on area
    valid_contours = [cnt for cnt in contours if min_area < cv2.contourArea(cnt) < max_area]
    
    # Visualization
    vis_image = image.copy()
    cv2.drawContours(vis_image, valid_contours, -1, (0, 255, 0), 2)
    
    return len(valid_contours), vis_image

def adjust_areas(image_path):
    cv2.namedWindow('Adjust Areas')
    cv2.createTrackbar('Min Area', 'Adjust Areas', 10, 500, lambda x: None)
    cv2.createTrackbar('Max Area', 'Adjust Areas', 100, 1000, lambda x: None)

    while True:
        min_area = cv2.getTrackbarPos('Min Area', 'Adjust Areas')
        max_area = cv2.getTrackbarPos('Max Area', 'Adjust Areas')
        
        count, vis_image = count_pink_markers(image_path, min_area, max_area)
        
        cv2.putText(vis_image, f'Count: {count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Adjust Areas', vis_image)
        
        key = cv2.waitKey(1) & 0xFF

        # Run the following when NOT using Docker Container for screenshot of dot counts
        # ct stores current date
        # ct = datetime.datetime.now().date()
        # colored_dots = "colored_dots_{}.png".format(ct) 
        # pyautogui.screenshot(colored_dots)
        # print("Screenshot Image saved")

        time.sleep(1)
        break
    


    cv2.destroyAllWindows()
    return min_area, max_area
 
# Usage
# image_path = 'path/to/your/image.png'
# num_dots = count_colored_dots(image_path)
# archived functions below
# def count_pink_circles(image_path):
#     # Read the image
#     image = cv2.imread(image_path)
    
#     # Convert BGR to HSV
#     hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
#     # Define range of pink color in HSV
#     lower_pink = np.array([225, 48, 225])
#     upper_pink = np.array([245, 60, 255])
    
#     # Threshold the HSV image to get only pink colors
#     mask = cv2.inRange(hsv, lower_pink, upper_pink)
    
#     # Apply morphological operations to remove noise
#     kernel = np.ones((5,5), np.uint8)
#     mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
#     mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
#     # Detect circles using Hough Circle Transform
#     circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, dp=1.5, minDist=3,
#                                param1=90, param2=0.8, minRadius=1, maxRadius=15)
    
#     # If circles are found
#     if circles is not None:
#         circles = np.uint16(np.around(circles))
#         num_circles = len(circles[0])
#         print(f"Number of colored dots: {num_circles}")
#         print("Circles: ", circles)
#         return len(circles[0])
#     else:
#         return 0

# def count_pink_markers(image_path):
#     # Read the image
#     image = cv2.imread(image_path)
    
#     # Convert BGR to HSV
#     hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
#     # Define range of pink color in HSV
#     lower_pink = np.array([140, 50, 180])
#     upper_pink = np.array([170, 255, 255])
    
#     # Threshold the HSV image to get only pink colors
#     mask = cv2.inRange(hsv, lower_pink, upper_pink)
    
#     # Find contours
#     contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
#     # Filter contours based on area
#     min_area = 10  # Minimum area of a marker
#     max_area = 30  # Maximum area of a marker
#     valid_contours = [cnt for cnt in contours if min_area < cv2.contourArea(cnt) < max_area]
#     print("Valid markers: ", valid_contours)
#     return len(valid_contours)
