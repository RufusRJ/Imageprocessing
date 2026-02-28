# Fourier Transform Image Processing Project

## 📖 Overview
This project demonstrates the implementation of **2D Fourier Transform** in image processing using Python.  
It provides a GUI-based visualization tool that shows how an image is transformed from the spatial domain to the frequency domain and then reconstructed after filtering.

---

## 🎯 Objectives
- Apply 2D Fourier Transform on an image
- Visualize the magnitude spectrum
- Apply High-Pass Filtering in the frequency domain
- Reconstruct the enhanced image using Inverse Fourier Transform
- Display pixel matrices for comparison

---

## 🧠 Theory

The 2D Discrete Fourier Transform (DFT) is defined as:

F(u,v) = Σ Σ f(x,y) e^(-j2π(ux/M + vy/N))

Where:
- f(x,y) → spatial domain image
- F(u,v) → frequency domain representation
- M, N → image dimensions

The Inverse DFT is:

f(x,y) = Σ Σ F(u,v) e^(j2π(ux/M + vy/N))

---

## ⚙️ Features

- Upload image using file dialog
- Display:
  - Original Image
  - Fourier Magnitude Spectrum
  - Enhanced Image (High-Pass Filtered)
- Show top 5×5 pixel matrices below each image
- Step-by-step transformation visualization
- GUI-based interface using Tkinter

---

## 🛠️ Technologies Used

- Python
- NumPy
- OpenCV
- Matplotlib
- Tkinter

---

## 📂 How to Run

1. Install required libraries:

pip install numpy opencv-python matplotlib

2. Run the project:

python fourier_transform_project.py

3. Click "Upload Image"
4. Select an image file (.jpg, .png, .bmp)

---

## 🔍 Output Explanation

1. Original Image  
   - Spatial domain representation (pixel values)

2. Magnitude Spectrum  
   - Frequency domain representation
   - Bright center → Low frequencies
   - Outer regions → High frequencies

3. Enhanced Image  
   - Result after applying High-Pass Filter
   - Edges become more prominent

---

## 📊 Learning Outcome

- Understanding of spatial vs frequency domain
- Implementation of DFT and Inverse DFT
- Application of frequency domain filtering
- Visualization of pixel matrix transformations

---

## 👨‍💻 Author

Rufus Nicholas Ebenezer  
Image Processing Project
