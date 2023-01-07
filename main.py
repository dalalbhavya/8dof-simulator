import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mplot3d
import numpy as np
import mpl_toolkits.mplot3d.axes3d as axes3d
from scipy.spatial.transform import Rotation as R


LINK_LEN = 100
PI = np.pi

def get_link_coordinates(joint_angles):
    theta0 = joint_angles[0]
    theta1 = joint_angles[1]
    theta2 = joint_angles[2]
    theta3 = joint_angles[3]
    theta4 = joint_angles[4]
    theta5 = joint_angles[5]
    theta6 = joint_angles[6]
    theta7 = joint_angles[7]

    joint0_pos = np.array([LINK_LEN*1, 0, 0])
    joint1_pos = np.array([LINK_LEN*2, 0, 0])
    # joint1_pos = joint0_pos + np.array([LINK_LEN*np.cos(theta0), 0, -LINK_LEN*np.sin(theta0)])
    joint2_pos = np.array([LINK_LEN*3, 0, 0])
    joint3_pos = np.array([LINK_LEN*4, 0, 0])
    joint4_pos = np.array([LINK_LEN*5, 0, 0])
    joint5_pos = np.array([LINK_LEN*6, 0, 0])
    joint6_pos = np.array([LINK_LEN*7, 0, 0])
    joint7_pos = np.array([LINK_LEN*8, 0, 0])
    joint8_pos = np.array([LINK_LEN*9, 0, 0])   #End Effector

    joint1_vector = joint1_pos - joint0_pos
    rotation_radians = theta0
    rotation_axis = np.array([0,1,0])
    rotation_vector = rotation_radians*rotation_axis
    rotation = R.from_rotvec(rotation_vector)
    rotated_vector = rotation.apply(joint1_vector)

    joint1_pos = joint0_pos + rotated_vector

    x = [0, joint0_pos[0], joint1_pos[0], joint2_pos[0], joint3_pos[0], joint4_pos[0], joint5_pos[0], joint6_pos[0], joint7_pos[0], joint8_pos[0]]
    y = [0, joint0_pos[1], joint1_pos[1], joint2_pos[1], joint3_pos[1], joint4_pos[1], joint5_pos[1], joint6_pos[1], joint7_pos[1], joint8_pos[1]]
    z = [0, joint0_pos[2], joint1_pos[2], joint2_pos[2], joint3_pos[2], joint4_pos[2], joint5_pos[2], joint6_pos[2], joint7_pos[2], joint8_pos[2]]

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