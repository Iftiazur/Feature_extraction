import cv2
import numpy as np


def load_image(image_path):
    """Load the image"""
    image = cv2.imread(image_path)
    return image


def extract_edges(image):
    """Extract first and second order edges using convolution"""
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply first order edge kernel
    first_order_kernel = np.array([[-1, 0, 1],
                                   [-1, 0, 1],
                                   [-1, 0, 1]])
    first_order_edges = cv2.filter2D(gray, -1, first_order_kernel)

    # Apply second order edge kernel
    second_order_kernel = np.array([[1, 2, 1],
                                    [0, 0, 0],
                                    [-1, -2, -1]])
    second_order_edges = cv2.filter2D(gray, -1, second_order_kernel)

    # Threshold the edges
    _, first_order_edges_thresh = cv2.threshold(first_order_edges, 50, 255, cv2.THRESH_BINARY)
    _, second_order_edges_thresh = cv2.threshold(second_order_edges, 50, 255, cv2.THRESH_BINARY)

    # Overlap the binary edges on the original image
    overlapped_image = image.copy()
    overlapped_image[first_order_edges_thresh == 255] = [0, 0, 255]  # Red for first order edges
    overlapped_image[second_order_edges_thresh == 255] = [0, 255, 0]  # Green for second order edges

    return overlapped_image


def main():
    # Step 1: Load the image
    image_path = 'sample_img.jpg'
    image = load_image(image_path)

    # Step 2: Extract first and second order edges
    overlapped_edges = extract_edges(image)

    # Step 3: Display the result
    cv2.imshow('Edges', overlapped_edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
