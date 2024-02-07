import cv2
import string
import os
import tkinter as tk
from tkinter import filedialog

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)
def encrypt_image():
    filename = filedialog.askopenfilename(title="Select Image")
    if filename:
        x = cv2.imread(filename)

        key = key_entry.get()
        text = text_entry.get()

        kl = 0
        tln = len(text)
        z = 0  # decides plane
        n = 0  # number of row
        m = 0  # number of column

        l = len(text)

        for i in range(l):
            x[n, m, z] = d[text[i]] ^ d[key[kl]]
            n = n + 1
            m = m + 1
            m = (m + 1) % 3
            kl = (kl + 1) % len(key)

        cv2.imwrite("encrypted_img.jpg", x)
        os.startfile("encrypted_img.jpg")
        result_label.config(text="Data Hiding in Image completed successfully.")
