import cv2
import numpy as np

def rotate_image(image, angle):
    # Get image dimensions
    height, width = image.shape[:2]
    # Calculate the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
    # Apply the rotation to the image
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

def main():
    # Load the image
    image = cv2.imread('input_image3.png')

    # Check if image is loaded successfully
    if image is None:
        print("Error: Could not open or find the image.")
        return

    # Rotate the image by 45 degrees
    rotated_45 = rotate_image(image, 45)
    cv2.imshow('Rotated 45 Degrees', rotated_45)
    # Save the averaged image
    cv2.imwrite('output_image5.png', rotated_45)
    cv2.waitKey(0)

    # Rotate the image by 90 degrees
    rotated_90 = rotate_image(image, 90)
    cv2.imshow('Rotated 90 Degrees', rotated_90)
    # Save the averaged image
    cv2.imwrite('output_image6.png', rotated_90)
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
