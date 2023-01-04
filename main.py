import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mplot3d
import numpy as np
import mpl_toolkits.mplot3d.axes3d as axes3d

LINK_LEN = 100

def get_link_coordinates(joint_angles):
    x = [0, LINK_LEN, LINK_LEN*2, LINK_LEN*3, LINK_LEN*4, LINK_LEN*5, LINK_LEN*6, LINK_LEN*7, LINK_LEN*8, LINK_LEN*9]
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    return (x, y, z)
    
def main():
    fig = plt.figure()
    ax = plt.axes(projection="3d")

    #TODO: #1 Implement Forward Kinematics 
    x_line, y_line, z_line = get_link_coordinates(0)

    #TODO: #2 Add spherical obstacles in the form of spherical surface

    for i in range(len(z_line)):
        ax.plot(x_line[i:i+2], y_line[i:i+2], z_line[i:i+2], label="link"+str(i))
    
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()