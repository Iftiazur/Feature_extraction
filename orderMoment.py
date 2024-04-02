import cv2
import numpy as np
def load_image(image_path):
    """Load the image in grayscale"""
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    return image
def compute_moment_11(image):
    """Compute the (1,1) order moment"""
    moment_11 = np.sum(image * np.indices(image.shape)) / np.sum(image)
    return moment_11
def compute_moment_22(image, moment_11):
    """Compute the (2,2) order moment"""
    moment_22 = np.sum((np.indices(image.shape) - moment_11)**2 * image) / np.sum(image)
    return moment_22

def compute_moment_inertia(image):
    """Compute the moments of inertia"""
    # Compute the central moments
    M = cv2.moments(image)

    # Extract the central moments
    mu20 = M['mu20']
    mu02 = M['mu02']
    mu11 = M['mu11']

    # Ensure that mu11 is not negative
    if mu11 < 0:
        # Correct mu11 using centralized image
        mean_x = M['m10'] / M['m00']
        mean_y = M['m01'] / M['m00']
        shifted_x = np.indices(image.shape)[0] - mean_x
        shifted_y = np.indices(image.shape)[1] - mean_y
        mu11 = np.sum(shifted_x * shifted_y * image) / np.sum(image)

    return mu20, mu02, mu11


def main():
    # Image selection
    image_path = 'sample_img.jpg'
    image = load_image(image_path)

    # (1,1) order moment
    moment_11 = compute_moment_11(image)

    #  (2,2) order moment
    moment_22 = compute_moment_22(image, moment_11)

    # Moment of inertia
    mu20, mu02, mu11 = compute_moment_inertia(image)

    # Result Display
    print("(1,1) order moment:", moment_11)
    print("(2,2) order moment:", moment_22)
    print("Moment of inertia u20:", mu20)
    print("Moment of inertia u02:", mu02)
    print("Moment of inertia u11:", mu11)


if __name__ == "__main__":
    main()
