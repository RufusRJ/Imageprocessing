import numpy as np
import cv2
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ----------------------------
# Create Main Window
# ----------------------------
root = Tk()
root.title("Fourier Transform - Step by Step Visualization")
root.geometry("1200x900")

main_frame = Frame(root)
main_frame.pack()

# ----------------------------
# Upload Function
# ----------------------------
def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
    )

    if not file_path:
        return

    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        return

    show_process(img)

# ----------------------------
# Display Matrix Below Image
# ----------------------------
def display_matrix(parent, matrix, title_text):
    title = Label(parent, text=title_text, font=("Arial", 11, "bold"))
    title.pack()

    text = Text(parent, height=6, width=60)
    text.pack()
    text.insert(END, np.array2string(np.round(matrix[:5,:5],2), separator=', '))
    text.config(state=DISABLED)

# ----------------------------
# Show Processing Steps
# ----------------------------
def show_process(img):

    for widget in main_frame.winfo_children():
        widget.destroy()

    # Fourier Transform
    dft = np.fft.fft2(img)
    dft_shift = np.fft.fftshift(dft)
    magnitude = 20*np.log(np.abs(dft_shift)+1)

    # High Pass Filter
    rows, cols = img.shape
    crow, ccol = rows//2 , cols//2
    mask = np.ones((rows, cols), np.uint8)
    mask[crow-30:crow+30, ccol-30:ccol+30] = 0

    filtered = dft_shift * mask
    f_ishift = np.fft.ifftshift(filtered)
    img_back = np.abs(np.fft.ifft2(f_ishift))

    # ----------------------------
    # Create Matplotlib Figure
    # ----------------------------
    fig, ax = plt.subplots(1,3, figsize=(12,4))

    ax[0].imshow(img, cmap='gray')
    ax[0].set_title("Original Image")
    ax[0].axis('off')

    ax[1].imshow(magnitude, cmap='gray')
    ax[1].set_title("Magnitude Spectrum")
    ax[1].axis('off')

    ax[2].imshow(img_back, cmap='gray')
    ax[2].set_title("Enhanced Image")
    ax[2].axis('off')

    canvas = FigureCanvasTkAgg(fig, master=main_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

    # ----------------------------
    # Matrices Below Each Image
    # ----------------------------
    matrix_frame = Frame(main_frame)
    matrix_frame.pack(pady=10)

    col1 = Frame(matrix_frame)
    col1.pack(side=LEFT, padx=20)

    col2 = Frame(matrix_frame)
    col2.pack(side=LEFT, padx=20)

    col3 = Frame(matrix_frame)
    col3.pack(side=LEFT, padx=20)

    display_matrix(col1, img, "Original Image Pixel Matrix (Top 5x5)")
    display_matrix(col2, magnitude, "Magnitude Spectrum Matrix (Top 5x5)")
    display_matrix(col3, img_back, "Enhanced Image Pixel Matrix (Top 5x5)")

# ----------------------------
# Upload Button
# ----------------------------
upload_btn = Button(root, text="Upload Image", command=upload_image, font=("Arial", 14))
upload_btn.pack(pady=10)

root.mainloop()