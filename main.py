import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mplot3d
import numpy as np
import mpl_toolkits.mplot3d.axes3d as axes3d
from scipy.spatial.transform import Rotation as R


LINK_LEN = 100
PI = np.pi

def rotate_vector(vector, axis, radians):
    rotation_vector = radians*axis
    rotation = R.from_rotvec(rotation_vector)
    rotated_vector = rotation.apply(vector)
    return rotated_vector

def update_joint_vectors(joint_vectors, joint_pos):
    for i in range(len(joint_pos)-1):
        joint_vectors[i] = (joint_pos[i+1] - joint_pos[i])

def get_link_coordinates(joint_angles):
    theta0 = joint_angles[0]
    theta1 = joint_angles[1]
    theta2 = joint_angles[2]
    theta3 = joint_angles[3]
    theta4 = joint_angles[4]
    theta5 = joint_angles[5]
    theta6 = joint_angles[6]
    theta7 = joint_angles[7]

    axis0 = np.array([0, 1, 0])
    axis1 = np.array([0, 0, 1])
    axis2 = np.array([0, 1, 0])
    axis3 = np.array([0, 0, 1])
    axis4 = np.array([0, 1, 0])
    axis5 = np.array([0, 0, 1])
    axis6 = np.array([0, 1, 0])
    axis7 = np.array([0, 0, 1])
    axis8 = np.array([0, 1, 0])
    joint_axis = np.array([[0, 1, 0,], [0, 0, 1], [0, 1, 0,], [0, 0, 1], [0, 1, 0,], [0, 0, 1], [0, 1, 0,], [0, 0, 1], [0, 1, 0,]])
    

    joint0_pos = np.array([LINK_LEN*1, 0, 0])
    joint1_pos = np.array([LINK_LEN*2, 0, 0])
    joint2_pos = np.array([LINK_LEN*3, 0, 0])
    joint3_pos = np.array([LINK_LEN*4, 0, 0])
    joint4_pos = np.array([LINK_LEN*5, 0, 0])
    joint5_pos = np.array([LINK_LEN*6, 0, 0])
    joint6_pos = np.array([LINK_LEN*7, 0, 0])
    joint7_pos = np.array([LINK_LEN*8, 0, 0])
    joint8_pos = np.array([LINK_LEN*9, 0, 0])   #End Effector

    joint_pos = np.array([joint0_pos, joint1_pos, joint2_pos, joint3_pos, joint4_pos, joint5_pos, joint6_pos, joint7_pos, joint7_pos, joint8_pos])
    joint_vector = []
    for i in range(len(joint_pos)-1):
        joint_vector.append(joint_pos[i+1] - joint_pos[i])

    joint_vector = np.array(joint_vector)

    for i in range(len(joint_angles)):
        #rotate all the link vectors (joint(i+1)_pos - joint(i)_pos)
        for j in range(i, len(joint_angles)):
            joint_pos[j+1] = joint_pos[j] + rotate_vector(joint_vector[j], joint_axis[i], joint_angles[i])
        update_joint_vectors(joint_vector, joint_pos)
        #rotate axis(i+1) to  axis(8) 

    joint1_pos = joint0_pos + rotate_vector(joint_vector[0], axis0, theta0)
    joint2_pos = joint1_pos + rotate_vector(joint_vector[1], axis0, theta0)


    x = [0, joint0_pos[0], joint1_pos[0], joint2_pos[0], joint3_pos[0], joint4_pos[0], joint5_pos[0], joint6_pos[0], joint7_pos[0], joint8_pos[0]]
    y = [0, joint0_pos[1], joint1_pos[1], joint2_pos[1], joint3_pos[1], joint4_pos[1], joint5_pos[1], joint6_pos[1], joint7_pos[1], joint8_pos[1]]
    z = [0, joint0_pos[2], joint1_pos[2], joint2_pos[2], joint3_pos[2], joint4_pos[2], joint5_pos[2], joint6_pos[2], joint7_pos[2], joint8_pos[2]]

    x = [0, joint_pos[0][0], joint_pos[1][0], joint_pos[2][0], joint_pos[3][0], joint_pos[4][0], joint_pos[5][0], joint_pos[6][0], joint_pos[7][0], joint_pos[8][0]]
    y = [0, joint_pos[0][1], joint_pos[1][1], joint_pos[2][1], joint_pos[3][1], joint_pos[4][1], joint_pos[5][1], joint_pos[6][1], joint_pos[7][1], joint_pos[8][1]]
    z = [0, joint_pos[0][2], joint_pos[1][2], joint_pos[2][2], joint_pos[3][2], joint_pos[4][2], joint_pos[5][2], joint_pos[6][2], joint_pos[7][2], joint_pos[8][2]]


    return (x, y, z)
    
def main():
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.set_aspect("equal")

    #TODO: #1 Implement Forward Kinematics 
    x_line, y_line, z_line = get_link_coordinates([PI/4, 0, 0, 0, 0, 0, 0, 0])
    x_line = np.array(x_line)
    y_line = np.array(y_line)
    z_line = np.array(z_line)
    
    #TODO: #2 Add spherical obstacles in the form of spherical surface

    for i in range(len(z_line)):
        ax.plot(x_line[i:i+2], -z_line[i:i+2], y_line[i:i+2], label="link"+str(i))
    
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()