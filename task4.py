import cv2
import numpy as np

def block_averaging(image, block_size):
    # Get image dimensions
    height, width = image.shape[:2]

    # Calculate number of blocks along rows and columns
    num_blocks_row = height // block_size
    num_blocks_col = width // block_size

    # Initialize a copy of the input image
    averaged_image = np.copy(image)

    # Iterate over each block
    for i in range(num_blocks_row):
        for j in range(num_blocks_col):
            # Calculate block boundaries
            row_start = i * block_size
            row_end = (i + 1) * block_size
            col_start = j * block_size
            col_end = (j + 1) * block_size

            # Extract the block
            block = image[row_start:row_end, col_start:col_end]

            # Calculate the average pixel value of the block
            average_pixel_value = np.mean(block)

            # Replace all pixels within the block with the average value
            averaged_image[row_start:row_end, col_start:col_end] = average_pixel_value

    return averaged_image

def main():
    # Load the image
    image = cv2.imread('input_image1.jpg')

    # Check if image is loaded successfully
    if image is None:
        print("Error: Could not open or find the image.")
        return

    # Perform block averaging for 3x3 blocks
    averaged_image_3x3 = block_averaging(image, block_size=3)
    cv2.imshow('Averaged Image (3x3 Blocks)', averaged_image_3x3)
    cv2.imwrite('output_image7.png', averaged_image_3x3)
    cv2.waitKey(0)

    # Perform block averaging for 5x5 blocks
    averaged_image_5x5 = block_averaging(image, block_size=5)
    cv2.imshow('Averaged Image (5x5 Blocks)', averaged_image_5x5)
    cv2.imwrite('output_image8.png', averaged_image_5x5)
    cv2.waitKey(0)

    # Perform block averaging for 7x7 blocks
    averaged_image_7x7 = block_averaging(image, block_size=7)
    cv2.imshow('Averaged Image (7x7 Blocks)', averaged_image_7x7)
    cv2.imwrite('output_image9.png', averaged_image_7x7)
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
