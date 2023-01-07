import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mplot3d
import numpy as np
import mpl_toolkits.mplot3d.axes3d as axes3d

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

    joint0_pos = np.array([LINK_LEN, 0, 0])
    joint1_pos = joint0_pos + np.array([LINK_LEN*np.cos(theta0), 0, -LINK_LEN*np.sin(theta0)])
    joint2_pos = np.array([])
    joint3_pos = np.array([])
    joint4_pos = np.array([])
    joint5_pos = np.array([])
    joint6_pos = np.array([])
    joint7_pos = np.array([])

    x = [0, joint0_pos[0], joint1_pos[0], LINK_LEN*3, LINK_LEN*4, LINK_LEN*5, LINK_LEN*6, LINK_LEN*7, LINK_LEN*8, LINK_LEN*9]
    y = [0, joint0_pos[1], joint1_pos[1], 0, 0, 0, 0, 0, 0, 0]
    z = [0, joint0_pos[2], joint1_pos[2], 0, 0, 0, 0, 0, 0, 0]

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