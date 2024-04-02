import cv2
import numpy as np


def load_image(image_path):
    """Load the image"""
    image = cv2.imread(image_path)
    return image


def extract_edges(image):
    """Extract Sobel and Prewitt edges using convolution"""
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Sobel edge detection
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel_edges = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
    sobel_edges = np.uint8(sobel_edges)

    # Apply Prewitt edge detection
    kernel_x = np.array([[-1, 0, 1],
                         [-1, 0, 1],
                         [-1, 0, 1]])
    kernel_y = np.array([[-1, -1, -1],
                         [0, 0, 0],
                         [1, 1, 1]])
    prewitt_x = cv2.filter2D(gray, -1, kernel_x)
    prewitt_y = cv2.filter2D(gray, -1, kernel_y)
    prewitt_edges = np.sqrt(prewitt_x ** 2 + prewitt_y ** 2)
    prewitt_edges = np.uint8(prewitt_edges)

    # Threshold the edges
    _, sobel_edges_thresh = cv2.threshold(sobel_edges, 50, 255, cv2.THRESH_BINARY)
    _, prewitt_edges_thresh = cv2.threshold(prewitt_edges, 50, 255, cv2.THRESH_BINARY)

    # Overlap the binary edges on the original image
    overlapped_image = image.copy()
    overlapped_image[sobel_edges_thresh == 255] = [0, 0, 255]  # Red for Sobel edges
    overlapped_image[prewitt_edges_thresh == 255] = [0, 255, 0]  # Green for Prewitt edges

    return overlapped_image


def main():
    #Load the image
    image_path = 'sample_img.jpg'
    image = load_image(image_path)

    # Extract Sobel and Prewitt edges
    overlapped_edges = extract_edges(image)

    # Result Display
    cv2.imshow('Edges', overlapped_edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
