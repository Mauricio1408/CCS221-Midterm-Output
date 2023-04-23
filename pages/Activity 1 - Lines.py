import streamlit as st
import matplotlib.pyplot as plt

plt.title('Midpoint Line Algorithm')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

st.title('Midterm Output in CC201')
st.sidebar.header("Activity 1")
st.subheader("The Midpoint of the lines is represented by a blue dot")

st.sidebar.subheader("Midpoint line values")
x1 = st.sidebar.slider('x1', 0, 15, 1)
y1 = st.sidebar.slider('y1', 0, 15, 3)
x2 = st.sidebar.slider('x2', 0, 15, 7)
y2 = st.sidebar.slider('y2', 0, 15, 9)

st.subheader("Midpoint Line")

#midpoint
fig = plt.figure()
def MIDPOINT(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    xMid = (x1 + x2)/2
    yMid = (y1 + y2)/2
    #initialize the decision parameter
    d = dy - (dx/2)
    x = x1
    y = y1
    print('x = %s, y = %s' % (x, y))
    #initialize the plotting points
    xcoordinates = [x]
    ycoordinates = [y]

    while(x < x2):
        x += 1
        #East is chosen
        if (d < 0):
            d += dy
        
        #North East is chosen
        else:
            d += (dy - dx)
            y += 1
        
        xcoordinates.append(x)
        ycoordinates.append(y)
        print('x = %s, y = %s' % (x, y))
        print('Midpoint is at', xMid, yMid)
    plt.plot(xcoordinates, ycoordinates)
    plt.plot(int(xMid), int(yMid), 'b.')
    plt.grid()
    plt.scatter(xcoordinates, ycoordinates, color='Red', s=25)
midpoint_fig = MIDPOINT(x1, y1, x2, y2)
st.pyplot(fig)

#BRESENHAM LINE algorithm
st.sidebar.subheader("Bresenham line values")
x1_BRESEHNAM, x2_BRESEHNAM, y1_BRESEHNAM, y2_BRESEHNAM = st.sidebar.slider('x1 for BRESENHAM-LINE', 0, 15, 1),\
                                                st.sidebar.slider('x2 for BRESENHAM-LINE', 0, 15, 4),\
                                                st.sidebar.slider('y1 for BRESENHAM-LINE', 0, 15, 8),\
                                                st.sidebar.slider('y2 for BRESENHAM-LINE', 0, 15, 9)
fig2 = plt.figure()
def BRESENHAMS_LINE(x1, y1, x2, y2, color):
    X_coordinates = [x1]
    Y_coordinates = [y1]
    dx = x2 - x1
    dy = y2 - y1
    Pk = 2*dy-dx 
    for i in range(dx):
        if Pk < 0:
            Pkn = Pk + (2*dy)
            x1 += 1
            Pk = Pkn

        else:
            Pkn = Pk + (2*dy - 2*dx)
            x1 += 1
            y1 += 1

        X_coordinates.append(x1)
        Y_coordinates.append(y1)
        X = (X_coordinates[0], X_coordinates[-1])
        Y = (Y_coordinates[0], Y_coordinates[-1])

    plt.plot(X, Y, 'lightblue', linewidth="1")    
    plt.scatter(X_coordinates, Y_coordinates, color='BLACK', s=25)
    plt.grid()

bresenham_ = BRESENHAMS_LINE(x1_BRESEHNAM, y1_BRESEHNAM, x2_BRESEHNAM, y2_BRESEHNAM, 'b')
st.subheader("Bresenham Line")
st.pyplot(fig2)

#DDA_LINE algorithm
st.subheader("DDA-LINE")
st.sidebar.subheader("DDA-LINE values")
x1_DDALINE, x2_DDALINE, y1_DDALINE, y2_DDALINE = st.sidebar.slider('x1 for DDALINE', 0, 15, 1),\
                                                st.sidebar.slider('x2 for DDALINE', 0, 15, 3),\
                                                st.sidebar.slider('y1 for DDALINE', 0, 15, 7),\
                                                st.sidebar.slider('y2 for DDALINE', 0, 15, 9)

fig3 = plt.figure()
def DDALine (x1, y1, x2, y2, color):
   
    dx = x2 - x1
    dy = y2 - y1

    xMidDDA = (x1 + x2)/2
    yMidDDA = (y1 + y2)/2

    # calculate steps required for generating pixels

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    # calculate increment in x and y for each step
    Xinc = float(dx / steps)
    Yinc = float(dy / steps)

    for i in range(0, int(steps + 1)):
        #Draw pixels 
        x1 += Xinc
        y1 += Yinc
        plt.plot(int(x1), int(y1), color)
        plt.plot(int(xMidDDA), int(yMidDDA), 'b.')
    return fig3

fig3 = DDALine (x1_DDALINE, x2_DDALINE, y1_DDALINE, y2_DDALINE, 'ro')
st.pyplot(fig3)














