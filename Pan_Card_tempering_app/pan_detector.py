import cv2
from skimage.metrics import structural_similarity as ssim
import imutils

def detect_tampering(original_path, uploaded_path):
    """
    Compare original PAN card with uploaded PAN card
    Return similarity score
    """
    original = cv2.imread(original_path)
    tampered = cv2.imread(uploaded_path)

    if original is None or tampered is None:
        raise ValueError("Image not found or invalid path")

    # Resize images
    original = cv2.resize(original, (250, 160))
    tampered = cv2.resize(tampered, (250, 160))

    # Convert to grayscale
    grayA = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(tampered, cv2.COLOR_BGR2GRAY)

    # Compute SSIM
    score, diff = ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")

    # Optional: contours (just for analysis, not required for Flask score)
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # Draw rectangles on original/tampered (optional)
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(original, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(tampered, (x, y), (x + w, y + h), (0, 0, 255), 2)

    return round(score, 4)  # just return SSIM score for Flask
