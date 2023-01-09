import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mplot3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import mpl_toolkits.mplot3d.axes3d as axes3d
from scipy.spatial.transform import Rotation as R
import matplotlib.animation as animation


LINK_LEN = 100
PI = np.pi

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.axes.set_xlim3d(left =0, right=9*LINK_LEN)
ax.set_aspect("equal")
line, = ax.plot([], [], [])

def initialize_position():
    joint0_pos = np.array([LINK_LEN*1, 0, 0])
    joint1_pos = np.array([LINK_LEN*2, 0, 0])
    joint2_pos = np.array([LINK_LEN*3, 0, 0])
    joint3_pos = np.array([LINK_LEN*4, 0, 0])
    joint4_pos = np.array([LINK_LEN*5, 0, 0])
    joint5_pos = np.array([LINK_LEN*6, 0, 0])
    joint6_pos = np.array([LINK_LEN*7, 0, 0])
    joint7_pos = np.array([LINK_LEN*8, 0, 0])
    joint8_pos = np.array([LINK_LEN*9, 0, 0])   #End Effector

    joint_pos = np.array([joint0_pos, joint1_pos, joint2_pos, joint3_pos, joint4_pos, joint5_pos, joint6_pos, joint7_pos, joint8_pos])

    return joint_pos

def rotate_vector(vector, axis, radians):
    rotation_vector = radians*axis
    rotation = R.from_rotvec(rotation_vector)
    rotated_vector = rotation.apply(vector)
    return rotated_vector

def update_joint_vectors(joint_vectors, joint_pos):
    for i in range(len(joint_pos)-1):
        joint_vectors[i] = (joint_pos[i+1] - joint_pos[i])
    
    return joint_vectors

def get_link_coordinates(joint_angles):
    joint_axis = np.array([[0., 1., 0.], [0., 0., 1.], [0., 1., 0.], [0., 0., 1.], [0., 1., 0.], [0., 0., 1.], [0., 1., 0.], [0., 0., 1.], [0., 1., 0.]])
    
    joint_pos = initialize_position()

    joint_vector = []
    for i in range(len(joint_pos)-1):
        joint_vector.append(joint_pos[i+1] - joint_pos[i])

    joint_vector = np.array(joint_vector)

    for i in range(len(joint_angles)):
        #rotate all the link vectors (joint(i+1)_pos - joint(i)_pos)
        for j in range(i, len(joint_angles)):
            joint_pos[j+1] = joint_pos[j] + rotate_vector(joint_vector[j], joint_axis[i], joint_angles[i])
        
        joint_vector = update_joint_vectors(joint_vector, joint_pos)
        
        #rotate axis(i+1) to  axis(8)
        for k in range(i+1, len(joint_angles)):
            joint_axis[k] = rotate_vector(joint_axis[k], joint_axis[i], joint_angles[i])
 
    x = [0, joint_pos[0][0], joint_pos[1][0], joint_pos[2][0], joint_pos[3][0], joint_pos[4][0], joint_pos[5][0], joint_pos[6][0], joint_pos[7][0], joint_pos[8][0]]
    y = [0, joint_pos[0][1], joint_pos[1][1], joint_pos[2][1], joint_pos[3][1], joint_pos[4][1], joint_pos[5][1], joint_pos[6][1], joint_pos[7][1], joint_pos[8][1]]
    z = [0, joint_pos[0][2], joint_pos[1][2], joint_pos[2][2], joint_pos[3][2], joint_pos[4][2], joint_pos[5][2], joint_pos[6][2], joint_pos[7][2], joint_pos[8][2]]

    return (x, y, z)

def init():
    joint_pos = initialize_position()
    line.set_data(joint_pos[0], -joint_pos[2], joint_pos[1]) #add initial pose of robot

    return line
    
def animate():
    #1 Implement Forward Kinematics 
    x_line, y_line, z_line = get_link_coordinates([0, 0, 0, 0, 0, 0, 0, 0])
    x_line = np.array(x_line)
    y_line = np.array(y_line)
    z_line = np.array(z_line)
    
    #TODO: #2 Add spherical obstacles in the form of spherical surface

    for i in range(len(z_line)-1):
        ax.plot(x_line[i:i+2], -z_line[i:i+2], y_line[i:i+2], label="link"+str(i))
    
    ax.legend()
    plt.show()
    
    print(x_line, y_line, z_line, sep="\n\n\n")

def main():
    #TODO: #3 Implement Forward Kinematics Animation
    anim = animation.FuncAnimation(fig, animate, )


if __name__ == "__main__":
    main()