import cv2
import numpy as np

def bgr_to_color_name(bgr_color):
    """
    Convert BGR color values to human-readable color names.
    """
    b, g, r = bgr_color
    
    # Define color ranges (in RGB for easier understanding)
    colors = [
        ("red", [255, 0, 0], 60),
        ("crimson", [220, 20, 60], 50),
        ("maroon", [128, 0, 0], 50),
        ("orange", [255, 165, 0], 60),
        ("coral", [255, 127, 80], 50),
        ("peach", [255, 218, 185], 50),
        ("yellow", [255, 255, 0], 60),
        ("gold", [255, 215, 0], 50),
        ("cream", [255, 253, 208], 50),
        ("green", [0, 255, 0], 60),
        ("lime", [50, 205, 50], 50),
        ("forest green", [34, 139, 34], 50),
        ("olive", [128, 128, 0], 50),
        ("teal", [0, 128, 128], 50),
        ("blue", [0, 0, 255], 60),
        ("navy", [0, 0, 128], 50),
        ("sky blue", [135, 206, 235], 50),
        ("turquoise", [64, 224, 208], 50),
        ("purple", [128, 0, 128], 60),
        ("violet", [238, 130, 238], 50),
        ("lavender", [230, 230, 250], 50),
        ("magenta", [255, 0, 255], 60),
        ("pink", [255, 192, 203], 60),
        ("rose", [255, 0, 127], 50),
        ("brown", [165, 42, 42], 60),
        ("tan", [210, 180, 140], 50),
        ("beige", [245, 245, 220], 50),
        ("black", [0, 0, 0], 80),
        ("charcoal", [54, 69, 79], 50),
        ("white", [255, 255, 255], 80),
        ("ivory", [255, 255, 240], 50),
        ("silver", [192, 192, 192], 50),
        ("gray", [128, 128, 128], 60),
    ]
    
    # Convert BGR to RGB for comparison
    rgb_color = [r, g, b]
    
    # Find the closest color
    min_distance = float('inf')
    closest_color = "unknown"
    
    for color_name, color_rgb, threshold in colors:
        distance = np.sqrt(sum((a - b) ** 2 for a, b in zip(rgb_color, color_rgb)))
        if distance < threshold and distance < min_distance:
            min_distance = distance
            closest_color = color_name
    
    return closest_color

def analyze_image(image_path: str) -> dict:
    """
    Analyzes an image to extract color and brightness information.
    """
    try:
        # Read the image
        image = cv2.imread(image_path)
        if image is None:
            return {"error": "Could not read image"}

        # # 1. Average Color
        # avg_color_per_row = np.average(image, axis=0)
        # avg_color = np.average(avg_color_per_row, axis=0)
        # avg_color_bgr = [int(c) for c in avg_color]

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
        k = 4  # Number of dominant colors to find
        _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        # Get the dominant colors
        centers = np.uint8(centers)
        dominant_colors_bgr = [center.tolist() for center in centers]
        
        # Convert dominant colors to human-readable names
        dominant_color_names = [bgr_to_color_name(color) for color in dominant_colors_bgr]

        # # 4. Color Histogram (commented out for now)
        # hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        # hist = cv2.normalize(hist, hist).flatten()

        return {
            "brightness": brightness,
            "lightness": lightness,
            "dominant_colors": dominant_colors_bgr,
            "dominant_color_names": dominant_color_names,
            # "color_histogram": hist.tolist(),
        }

    except Exception as e:
        return {"error": str(e)}
