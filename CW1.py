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
