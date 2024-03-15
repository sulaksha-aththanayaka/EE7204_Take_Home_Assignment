import cv2
import numpy as np

def spatial_average(image, neighborhood_size):
    # Define kernel for averaging
    kernel = np.ones((neighborhood_size, neighborhood_size), dtype=np.float32) / (neighborhood_size * neighborhood_size)

    # Perform 2D convolution with the image and the kernel
    averaged_image = cv2.filter2D(image, -1, kernel)

    return averaged_image

def main():
    # Load the image
    image = cv2.imread('input_image2.jpg')

    # Check if image is loaded successfully
    if image is None:
        print("Error: Could not open or find the image.")
        return

    # Perform spatial averaging with different neighborhood sizes
    neighborhood_sizes = [3, 10, 20]
    i = 2
    for size in neighborhood_sizes:
        averaged_image = spatial_average(image, size)

        # Display the averaged image
        cv2.imshow(f'Averaged Image ({size}x{size} neighborhood)', averaged_image)

        # Generate output filename
        output_filename = f'output_image{i}.jpg'

        # Save the averaged image
        cv2.imwrite(output_filename, averaged_image)
        i += 1
        cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
