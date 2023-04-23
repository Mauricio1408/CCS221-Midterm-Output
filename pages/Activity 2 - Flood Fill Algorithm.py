import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Midterm Output in CC201")
st.header("Activity 2")

#floodfill algorithm
#numpy array
st.subheader('Flood-fill Algorithm\n')
initial_fig = plt.figure()
two_d_arr = np.array([[1,1,1,1,1,1], 
                      [1,4,0,4,3,1],
                      [1,7,5,5,9,1],
                      [1,4,5,5,3,1],
                      [1,7,5,5,9,1],
                      [1,4,5,5,3,1],
                      [1,7,5,5,9,1],
                      [1,1,1,1,1,1]])

numpy_arr =  plt.imshow(two_d_arr, interpolation = 'none', cmap = 'BrBG')
numpy_arr.set_clim([0,50])
st.subheader('Initial figure:')
st.pyplot(initial_fig)
plt.close(fig=initial_fig)

#inputs
st.sidebar.subheader('Flood-fill:')
x = st.sidebar.number_input('X: (Flood-fill)', min_value=0, max_value=5, step=1, value = 0)
y = st.sidebar.number_input('Y: (Flood-fill)', min_value=0, max_value=5, step=1, value = 0)
c = st.sidebar.number_input('Color: (0-50) (Flood-fill)', min_value=0, max_value=50, step=1, value = 0)
old_c = two_d_arr[x][y]

st.subheader('Result:')

figure = plt.figure()
def change(x_val, y_val, c, old_color):
        x = len(two_d_arr)
        y = len(two_d_arr[0])

        if x_val < 0 or x_val >= x or y_val < 0 or y_val >= y or two_d_arr[x_val][y_val] != old_color:
                return
        
        else:
                two_d_arr[x_val][y_val] = c
                change(x_val + 1, y_val, c, old_color)
                change(x_val - 1, y_val, c, old_color)
                change(x_val, y_val - 1, c, old_color)
                change(x_val, y_val + 1, c, old_color)

def flood_fill(x_val, y_val, c, old_c):
    if old_c == c:
        return
    change (x_val, y_val, c, old_c)
    img = plt.imshow(two_d_arr, interpolation = 'none', cmap = 'BrBG')
    img.set_clim([0,50])    
    plt.colorbar()

fig1 = flood_fill(x, y, c, old_c)
st.pyplot(figure)
