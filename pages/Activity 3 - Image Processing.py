#activity 3 - Image Processing

import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

st.title("Midterm Output in CC201")
st.header("Activity 3 - Image Processing")

st.text('Translation - A process that moves every point a constant')
st.text(' distance in a specified direction.')
st.text('Rotation - In rotation, the object is rotated θ about the origin.')
st.text('Scaling - It is used to alter or change the size of objects. ')
st.text('The change is done using scaling factors.')
st.text('Reflection - It is used to render reflective objects like mirrors')
st.text('and shiny surfaces.')
st.text('Shearing - Shearing deals with changing the shape and size of the 2D')
st.text('object along x-axis and y-axis. It is similar to sliding the layers in')
st.text('one direction to change the shape of the 2D object.')

img_file = st.sidebar.file_uploader('Please input the image path here:', ['png', 'jpg', 'webp', 'jpeg'])

uploaded_img = Image.open(img_file)
uploaded_img = np.array(uploaded_img)

rows, cols, dims = uploaded_img.shape

#function for translation
def translation(img_, rows, cols):

    img_translated = np.float32([[1, 0, 50], 
                                [0, 1, 50],
                                [0, 0, 1]])
    img_translated =  cv2.warpPerspective(img_, img_translated, (cols, rows))

    return img_translated

#function for rotation
def rotation(img_, rows, cols):
    angle = np.radians(10)
    m_rotated = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
                            [np.sin(angle), np.cos(angle), 0],
                            [0, 0, 1]])

    rotated_img = cv2.warpPerspective(img_, m_rotated, (int(cols), int(rows)))
    return rotated_img

#function for scaling
def scaling(img_, rows, cols):
    m_scaling = np.float32([[1.5, 0, 0],
                            [0, 1.8, 0],
                            [0, 0, 1]])
    scaled_img = cv2.warpPerspective(img_, m_scaling, (cols*2, rows*2))
    return scaled_img

#function for reflection
def reflection(img_, rows, cols):
    m_reflection = np.float32([[1, 0, 0],
                               [0, -1, rows],
                               [0, 0, 1]])
    reflected_img = cv2.warpPerspective(img_, m_reflection, (int(cols), int(rows)))
    return reflected_img
    
#function dor shearing
def shear(img_, rows, cols):
    m_shearing = np.float32([[1, 0.5, 0],
                            [0, 1, 0],
                            [0, 0, 1]])
    sheared_img = cv2.warpPerspective(img_, m_shearing, (int(cols*1.5),int(rows*1.5)))
    return sheared_img

figure = plt.figure()

st.sidebar.subheader('Check the boxes to manipulate your Image')

translate_ = st.sidebar.checkbox('Translate')
if translate_:
    uploaded_img = translation(uploaded_img, rows, cols)

rotate_ = st.sidebar.checkbox('Rotate')
if rotate_:
    uploaded_img = rotation(uploaded_img, rows, cols)

scale_ = st.sidebar.checkbox('Scale')
if scale_:
    uploaded_img = scaling(uploaded_img, rows, cols)
    
reflect_ = st.sidebar.checkbox('Flip')
if reflect_:
    uploaded_img = reflection(uploaded_img, rows, cols)

shear_ = st.sidebar.checkbox('Shear')
if shear_:
    uploaded_img = shear(uploaded_img, rows, cols)





st.subheader('Original Image')
st.image(img_file)
st.subheader('Processed Image')
st.image(uploaded_img)

