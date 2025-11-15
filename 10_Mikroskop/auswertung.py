import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_threshold(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read image from {image_path}")
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    black_pixels = np.sum(binary == 0)
    total_pixels = binary.size
    percentage = (black_pixels / total_pixels) * 100
    
    plt.figure(figsize=(6, 4))
    
    plt.imshow(binary, cmap='gray')
    plt.title(f'Auto-Thresholded (Otsu)\nCoverage: {percentage:.2f}%')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    return percentage


# Example usage:
if __name__ == "__main__":
    # Replace with your image path
    image_path = "/home/loki/Workspace/Labor/Experimentalphysik2/10_Mikroskop/data/Graphene_20percent.jpg"

    print("Method 2: Automatic threshold (Otsu's method)")
    percentage2 = analyze_with_adaptive_threshold(image_path)
    print(f"Black dot coverage: {percentage2:.2f}%")