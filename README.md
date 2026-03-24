<div align="center">

```
 ██╗███╗   ███╗ ██████╗  ██████╗ ██████╗ ██╗████████╗██╗  ██╗███╗   ███╗
 ██║████╗ ████║██╔════╝ ██╔═══██╗██╔══██╗██║╚══██╔══╝██║  ██║████╗ ████║
 ██║██╔████╔██║██║  ███╗██║   ██║██████╔╝██║   ██║   ███████║██╔████╔██║
 ██║██║╚██╔╝██║██║   ██║██║   ██║██╔══██╗██║   ██║   ██╔══██║██║╚██╔╝██║
 ██║██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║  ██║██║   ██║   ██║  ██║██║ ╚═╝ ██║
 ╚═╝╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝
```

**Where images meet algorithms — fast, clean, and powerful image processing**

![Python](https://img.shields.io/badge/Python-3.8+-00ffc3?style=for-the-badge&logo=python&logoColor=black)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-00b4ff?style=for-the-badge&logo=streamlit&logoColor=black)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-00ffc3?style=for-the-badge&logo=opencv&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-00b4ff?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-2.0_Stable-00ffc3?style=for-the-badge)

<br/>

![IMGorithm Preview](https://via.placeholder.com/900x400/020b12/00ffc3?text=IMGorithm+Preview)

</div>

---

## ✨ What is IMGorithm?

**IMGorithm** is a sleek, browser-based image processing app built with Streamlit and OpenCV. It gives you a real-time preview panel on the left and a full suite of image tools on the right — no coding required. Upload an image, apply filters, edges, rotations, blur effects, and more — then download the result instantly.

> Designed for developers, designers, students, and anyone who wants pro-grade image processing without touching a terminal.

---

## 🚀 Features

| Category | Tools |
|---|---|
| **Filters** | Greyscale, Warm tone, Sharpen |
| **Edge Detection** | Laplacian, Canny, Sobel |
| **Blur** | Gaussian Blur (adjustable kernel) |
| **Portrait Blur** | Elliptical mask bokeh effect |
| **Brightness & Contrast** | Alpha/beta scaling |
| **Rotation** | 90° CW, 90° CCW, 180° |
| **Resize** | Custom width & height with smart interpolation |
| **Download** | Export processed image as PNG |

---

## 🖥️ Demo

```
┌─────────────────────────────┬─────────────────┐
│                             │  Upload Image   │
│      Live Preview           │  ─────────────  │
│      (sticky, fixed)        │  Filters        │
│                             │  Edges          │
│                             │  Blur           │
│                             │  Brightness     │
│                             │  Rotate         │
│                             │  (scrollable)   │
└─────────────────────────────┴─────────────────┘
```

The preview panel stays **locked in place** while you scroll through the tools on the right — no jumping around.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/imgorithm.git
cd imgorithm
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run imgorithm_app.py
```

Open your browser at `http://localhost:8501` 🎉

---

## 🧩 Requirements

```txt
streamlit>=1.28.0
opencv-python>=4.8.0
numpy>=1.24.0
Pillow>=10.0.0
```

> Or install directly: `pip install streamlit opencv-python numpy Pillow`

---

## 📁 Project Structure

```
imgorithm/
│
├── imgorithm_app.py      # Main application
├── requirements.txt      # Python dependencies
├── README.md             # You are here
└── assets/               # (optional) Screenshots, demo images
```

---

## 🛠️ How It Works

IMGorithm uses a **session state pattern** to track which operation the user last triggered. On each Streamlit re-render:

1. The uploaded image is decoded with **Pillow → NumPy → OpenCV**
2. The active session state key determines which CV2 operation runs
3. The result is displayed live in the left panel
4. A download button exports the processed image as PNG

### Smart Resize Interpolation

```python
# Downscale → INTER_AREA (sharpest for shrinking)
# Upscale   → INTER_CUBIC (best quality for enlarging)
```

### Portrait Blur

Uses an elliptical Gaussian mask to simulate camera bokeh — the subject (center ellipse) stays sharp while the background blurs.

---

## 🎨 UI Design

- **Dark theme** with radial gradient background (`#020b12`)
- **Accent color**: `#00ffc3` (cyan-green) + `#00b4ff` (sky blue)
- **Sticky left panel** — preview stays fixed while tools scroll
- **Custom scrollbar** styled to match the theme
- **Glass-morphism cards** with backdrop blur
- File size limit: **4MB** to keep processing snappy

---

## ⚠️ Limitations

- Maximum upload size: **4MB**
- Processes images in-memory (no server-side storage)
- Portrait blur uses a fixed elliptical mask — not AI face detection
- Warm filter applies a fixed +30 red channel boost

---

## 🔮 Roadmap

- [ ] AI-powered background removal
- [ ] Histogram equalization
- [ ] Batch image processing
- [ ] Side-by-side before/after comparison
- [ ] Custom filter presets
- [ ] EXIF metadata viewer

---

## 🤝 Contributing

Contributions are welcome! Here's how:

```bash
# Fork the repo, then:
git checkout -b feature/your-feature-name
git commit -m "Add: your feature description"
git push origin feature/your-feature-name
# Open a Pull Request
```

Please keep PRs focused — one feature per PR. Bug fixes are always welcome.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ♥ and OpenCV &nbsp;|&nbsp; © 2026 IMGorithm &nbsp;|&nbsp; v2.0 Stable

</div>
