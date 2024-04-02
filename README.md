

# Image Processing Toolbox

This repository contains three Python scripts for performing different image processing tasks using OpenCV and NumPy. The scripts are as follows:

1. **Moment Calculation**
   - File: `moment_calculation.py`
   - Description: Computes various moments of an input grayscale image, including the (1,1) and (2,2) order moments, as well as the moment of inertia.
   - Functions:
     - `load_image(image_path)`: Load the image in grayscale.
     - `compute_moment_11(image)`: Compute the (1,1) order moment.
     - `compute_moment_22(image, moment_11)`: Compute the (2,2) order moment.
     - `compute_moment_inertia(image)`: Compute the moments of inertia.
     - `main()`: Load an image, compute moments, and display results.

2. **Edge Detection Using Convolution**
   - File: `edge_detection_convolution.py`
   - Description: Detects edges in an input image using convolution with first and second order edge detection kernels.
   - Functions:
     - `load_image(image_path)`: Load the image.
     - `extract_edges(image)`: Extract first and second order edges using convolution.
     - `main()`: Load an image, extract edges, and display the result.

3. **Edge Detection Using Sobel and Prewitt Operators**
   - File: `edge_detection_operators.py`
   - Description: Detects edges in an input image using Sobel and Prewitt edge detection operators.
   - Functions:
     - `load_image(image_path)`: Load the image.
     - `extract_edges(image)`: Extract Sobel and Prewitt edges using convolution.
     - `main()`: Load an image, extract edges, and display the result.

## Usage
1. Clone the repository:
   ```
   git clone https://github.com/your-username/image-processing-toolbox.git
   ```
2. Navigate to the repository directory:
   ```
   cd image-processing-toolbox
   ```
3. Run any of the scripts using Python:
   ```
   python moment_calculation.py
   python edge_detection_convolution.py
   python edge_detection_operators.py
   ```
### Remmeber to replace the 'sample_img.jpg' with the path of your image
Feel free to explore and experiment with the provided scripts for different image processing tasks!
.
