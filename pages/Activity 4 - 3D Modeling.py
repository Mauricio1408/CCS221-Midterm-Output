#activity 4 - 3d Modeling

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay

st.title("Midterm Output in CC201")
st.header('Activity 4 - 3D Modeling')
st.subheader('Cube')

figure = plt.figure(figsize= (8,8))
#plotting function
def _plt_basic_object_(points):
    #plots a basic object, assuming its convex is not too high

    tri = Delaunay(points).convex_hull

    # fig = plt.figure(figsize = (8, 8))
    ax = figure.add_subplot(111, projection='3d')
    S = ax.plot_trisurf(points[:,0], points[:,1], points[:,2], triangles = tri, shade = True, cmap=cm.rainbow, lw = 0.5)

    ax.set_xlim3d(-5, 5)
    ax.set_ylim3d(-5, 5)
    ax.set_zlim3d(-5, 5) 

#translating function
def translate_obj(points, amount):
    return tf.add(points, amount)

#rotating function
def rotate_obj(points, angle):
    rotation_matrix = tf.stack([
                                [tf.cos(angle), tf.sin(angle), 0],
                                [-tf.sin(angle), tf.cos(angle), 0],
                                [0, 0, 1]
                                ])
    rotate_object = tf.matmul(tf.cast(points, tf.float32), tf.cast(rotation_matrix, tf.float32))

    return rotate_object


#cube function
def _cube_(bottom_lower=(0,0,0), side_length = 5):
    #create cube starting from the given bottom-lower point (lowest x, y, z values)

    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower, 
        bottom_lower + [0, side_length, 0],
        bottom_lower + [side_length, side_length, 0],
        bottom_lower + [side_length, 0, 0],
        bottom_lower + [0, 0, side_length],
        bottom_lower + [0, side_length, side_length],
        bottom_lower + [side_length, side_length, side_length],
        bottom_lower + [side_length, 0, side_length],
        bottom_lower,
    ])

    return points


init_cube_ = _cube_(side_length=3)
points1 = tf.constant(init_cube_, dtype=tf.float32)

# sliders for translation
st.sidebar.header('Input Values Here')
st.sidebar.subheader('Cube')
x_cube = st.sidebar.slider ('x for cube:', -10, 10, 1)
y_cube = st.sidebar.slider ('y for cube:', -10, 10, 2)
z_cube = st.sidebar.slider ('z for cube:', -10, 10, 2)
rotation_angle_cube = st.sidebar.number_input ('Angle of Rotation for Cube', min_value=-360.0, max_value=360.0, value=0.0, step=0.01)

translation_amount = tf.constant([x_cube, y_cube, z_cube], dtype=tf.float32)
translated_cube = translate_obj(points1, translation_amount)
rotated_cube = rotate_obj(translated_cube, rotation_angle_cube)

cube_ = _plt_basic_object_(rotated_cube)
st.pyplot(figure)

#sphere
st.subheader('Sphere')
ax = figure.add_subplot(111, projection='3d')
ax.set_aspect('equal')
ax.set_xlim3d(-5, 5)
ax.set_ylim3d(-5, 5)
ax.set_zlim3d(-5, 5)
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = 1 * np.outer(np.cos(u), np.sin(v))
y = 1 * np.outer(np.sin(u), np.sin(v))
z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))
    
elev = 100.0
rot = 80.0 / 180 * np.pi
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b', linewidth=0, alpha=0.5)
    #calculate vectors for "vertical" circle
a = np.array([-np.sin(elev / 180 * np.pi), 0, np.cos(elev / 180 * np.pi)])
b = np.array([0, 1, 0])
b = b * np.cos(rot) + np.cross(a, b) * np.sin(rot) + a * np.dot(a, b) * (1 - np.cos(rot))
ax.plot(np.sin(u),np.cos(u),0,color='k', linestyle = 'dashed')
horiz_front = np.linspace(0, np.pi, 100)
ax.plot(np.sin(horiz_front),np.cos(horiz_front),0,color='k')
vert_front = np.linspace(np.pi / 2, 3 * np.pi / 2, 100)
ax.plot(a[0] * np.sin(u) + b[0] * np.cos(u), b[1] * np.cos(u), a[2] * np.sin(u) + b[2] * np.cos(u),color='k', linestyle = 'dashed')
ax.plot(a[0] * np.sin(vert_front) + b[0] * np.cos(vert_front), b[1] * np.cos(vert_front), a[2] * np.sin(vert_front) + b[2] * np.cos(vert_front),color='k')

ax.view_init(elev = elev, azim = 0)

st.pyplot(figure)


st.subheader('Rectangular Prism / Cuboid')
#cuboid function
def _cuboid_(bottom_lower=(0,0,0), side_length=5):

    bottom_lower = np.array(bottom_lower)

    points4 = np.vstack([
        bottom_lower, 
        bottom_lower + [0, side_length, 0],
        bottom_lower + [side_length, side_length*2, 0],
        bottom_lower + [side_length, 0, 0],
        bottom_lower + [0, 0, side_length],
        bottom_lower + [0, side_length*2, side_length],
        bottom_lower + [side_length, side_length*2, side_length],
        bottom_lower + [side_length, 0, side_length],
        bottom_lower,
    ])

    return points4


cuboid = _cuboid_(side_length=2)
points4 = tf.constant(cuboid, dtype=tf.float32)

st.sidebar.subheader('Rectangular Prism')
x_Rectangular_Prism = st.sidebar.slider ('x for Rectangular Prism:', -10, 10, 1)
y_Rectangular_Prism = st.sidebar.slider ('y for Rectangular Prism:', -10, 10, 2)
z_Rectangular_Prism = st.sidebar.slider ('z for Rectangular Prism:', -10, 10, 2)
rotation_angle_Rectangular_Prism  = st.sidebar.number_input ('Angle of Rotation for Rectangular Prism', min_value=-360.0, max_value=360.0, value=0.0, step=0.01)

translation_amount2 = tf.constant([x_Rectangular_Prism, y_Rectangular_Prism, z_Rectangular_Prism], dtype=tf.float32)
translated_Rectangular_Prism = translate_obj(points4, translation_amount2)
rotated_Rectangular_Prism = rotate_obj(translated_Rectangular_Prism, rotation_angle_Rectangular_Prism)

cuboid_ = _plt_basic_object_(rotated_Rectangular_Prism)
st.pyplot(figure)


#triangular prism
st.subheader('Triangular Prism ')
def _triangular_prism_(bottom_lower=(0,0,0), side_length=5):

    bottom_lower = np.array(bottom_lower)

    points5 = np.vstack([
        [0, 0, 0], 
        [2, 0, 0],
        [1, -2, 0],
        [0, 0, 5],  
        [2, 0, 5],
        [1, -2, 5],

    ])

    return points5


triangularPrism = _triangular_prism_(side_length=1)
points5 = tf.constant(triangularPrism, dtype=tf.float32)

st.sidebar.subheader('Triangular Prism')
x_Triangular_Prism = st.sidebar.slider ('x for Triangular Prism:', -10, 10, 1)
y_Triangular_Prism = st.sidebar.slider ('y for Triangular_Prism:', -10, 10, 2)
z_Triangular_Prism = st.sidebar.slider ('z for Triangular_Prism:', -10, 10, 2)
rotation_angle_Triangular_Prism  = st.sidebar.number_input ('Angle of Rotation for Triangular_Prism', min_value=-360.0, max_value=360.0, value=0.0, step=0.01)

translation_amount3 = tf.constant([x_Triangular_Prism, y_Triangular_Prism, z_Triangular_Prism], dtype=tf.float32)
translated_Triangular_Prism  = translate_obj(points5, translation_amount3)
rotated_Triangular_Prism  = rotate_obj(translated_Triangular_Prism , rotation_angle_Triangular_Prism )

Triangular_Prism = _plt_basic_object_(rotated_Triangular_Prism )
st.pyplot(figure)



#pyramid
st.subheader('Pyramid')
def _pyramid_(bottom_lower=(-1, -1, -1), side_length=6, p=3):
    bottom_lower = np.array(bottom_lower)

    points3 = np.vstack([
        bottom_lower,
        bottom_lower + [0, side_length, 0],
        bottom_lower + [side_length,side_length, 0],
        bottom_lower + [side_length, 0, 0],
        bottom_lower + [p, p, side_length],
    ])

    return points3

#outputting the pyramid
init_pyramid_ = _pyramid_(side_length=6)
points3 = tf.constant(init_pyramid_, dtype=tf.float32)

st.sidebar.subheader('Pyramid')
x_Pyramid = st.sidebar.slider ('x for Pyramid:', -10, 10, 1)
y_Pyramid = st.sidebar.slider ('y for Pyramid:', -10, 10, 2)
z_Pyramid = st.sidebar.slider ('z for Pyramid:', -10, 10, 2)
rotation_angle_Pyramid  = st.sidebar.number_input ('Angle of Rotation for Pyramid', min_value=-360.0, max_value=360.0, value=0.0, step=0.01)

translation_amount4 = tf.constant([x_Pyramid, y_Pyramid, z_Pyramid], dtype=tf.float32)
translated_Pyramid  = translate_obj(points3, translation_amount4)
rotated_Pyramid  = rotate_obj(translated_Pyramid , rotation_angle_Pyramid )

Pyramid = _plt_basic_object_(rotated_Pyramid )
st.pyplot(figure)