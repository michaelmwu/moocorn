import cv2
import numpy as np

def analyze_image(image_path: str) -> dict:
    """
    Analyzes an image to extract color and brightness information.
    """
    try:
        # Read the image
        image = cv2.imread(image_path)
        if image is None:
            return {"error": "Could not read image"}

        # 1. Average Color
        avg_color_per_row = np.average(image, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        avg_color_bgr = [int(c) for c in avg_color]

        # 2. Brightness (Light vs. Dark)
        # Convert to grayscale to calculate brightness
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        brightness = np.mean(gray_image)
        lightness = "dark" if brightness < 128 else "light"

        # 3. Dominant Colors (using K-Means clustering)
        # Reshape the image to be a list of pixels
        pixels = image.reshape((-1, 3))
        pixels = np.float32(pixels)

        # Define criteria and apply kmeans()
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        k = 5  # Number of dominant colors to find
        _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        # Get the dominant colors
        centers = np.uint8(centers)
        dominant_colors = [center.tolist() for center in centers]

        # 4. Color Histogram
        hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        hist = cv2.normalize(hist, hist).flatten()

        return {
            "average_color_bgr": avg_color_bgr,
            "brightness": brightness,
            "lightness": lightness,
            "dominant_colors": dominant_colors,
            "color_histogram": hist.tolist(),
        }

    except Exception as e:
        return {"error": str(e)}
