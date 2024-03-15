import cv2
import numpy as np

def reduce_intensity_levels(image, levels):
    # Calculate the factor for mapping intensity levels
    factor = 256 // levels
    
    # Map intensity levels
    mapped_image = (image // factor) * factor
    
    return mapped_image

def main():
    # Load the image
    image = cv2.imread('input_image1.jpg', cv2.IMREAD_GRAYSCALE)
    
    # Check if image is loaded successfully
    if image is None:
        print("Error: Could not open or find the image.")
        return
    
    # Input desired number of intensity levels
    while True:
        levels = int(input("Enter the desired number of intensity levels (2, 4, 8, ...): "))
        if (levels & (levels - 1) == 0 and levels >= 1 and levels <= 256):
            break
        else:
            print("Please enter a valid power of 2 between 1 and 256 (inclusive).")
    
    # Reduce intensity levels
    reduced_image = reduce_intensity_levels(image, levels)
    
    # Saving the output image
    cv2.imwrite('output_image1.jpg', reduced_image)
    
    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
