#quizz 1 - translation

import numpy as np
import cv2
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
st.title("Midterm Output in CC201")
st.header('Quiz 1 -  Translation')
st.text('This is the first quiz from CCS-221: Computer Graphics and Visual Computing')
st.text('On the sidebar, please input the values for Bx, By, Tx, and Ty')

#getting the image from the user
img_ = st.sidebar.file_uploader('Upload Image here:', ['png', 'jpg', 'jpeg', 'webp'])

img_upload = Image.open(img_)
img_upload = np.array(img_upload)
rows, cols, dims = img_upload.shape

def translation(obj, rows, cols, Bx, By):

    img_translated = np.float32([[1, 0, Bx], 
                                [0, 1, By],
                                [0, 0, 1]])
    img_translated =  cv2.warpPerspective(obj, img_translated, (cols, rows))

    return img_translated

Bx_old = st.sidebar.slider('Value of Bx', 0, 500, 10)
By_old = st.sidebar.slider('Value of By', 0, 500, 10)

Tx = st.sidebar.slider('Value of Tx', 0, 500, 30)
Ty = st.sidebar.slider('Value of Ty', 0, 500, 30)

Bx_new = Bx_old + Tx
By_new = By_old + Ty

original_img = translation(img_upload, rows, cols, Bx_old, By_old)
translated_img = translation(img_upload, rows, cols, Bx_new, By_new)

st.subheader('Original Image')
st.image(original_img)

st.subheader('Translated Image')
st.image(translated_img)