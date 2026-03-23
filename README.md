# IMGorithm — Where Images Meet Algorithms

IMGorithm is a lightweight image processing web application built using Streamlit and OpenCV. It allows users to upload an image, apply various transformations and filters, and instantly preview and download the results. The application focuses on simplicity, speed, and a clean interface while offering multiple computer vision operations in one place.

---

## Overview

This project provides a two-panel interface:

- **Left Panel:** Live image preview  
- **Right Panel:** Controls for applying transformations  

All processing happens locally, ensuring privacy and fast performance without relying on external services.

---

## Features

- Image upload (JPG, PNG, JPEG, WebP)
- Real-time preview of processed images
- Resize images with custom dimensions
- Apply filters:
  - Greyscale
  - Warm tone
  - Sharpen
- Edge detection:
  - Canny
  - Sobel
  - Laplacian
- Blur effects:
  - Gaussian blur
  - Portrait blur (focus effect)
- Brightness and contrast adjustment
- Image rotation:
  - 90° clockwise
  - 90° counterclockwise
  - 180°
- Download processed image as PNG
- Clean glassmorphism-based UI

---

## Tech Stack

- **Frontend/UI:** Streamlit  
- **Backend Processing:** Python  
- **Image Processing:** OpenCV  
- **Numerical Operations:** NumPy  

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/imgorithm.git
cd imgorithm
