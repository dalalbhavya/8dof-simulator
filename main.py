import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mplot3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import mpl_toolkits.mplot3d.axes3d as axes3d
from scipy.spatial.transform import Rotation as R
import matplotlib.animation as animation
import pandas as pd
from skspatial.objects import Line, Sphere

df = pd.read_csv("test_traj.csv")

LINK_LEN = 100
PI = np.pi

def validate_traj(df_env, df_traj):
    pass    

def collision_check(p1, p2, center, radius):
    # Conditions for collision
    # intersection points lie between the two link ends
    sphere = Sphere(center, radius)
    line = Line(p1, p2)
    point_a = []
    point_b = []
    try:
        point_a, point_b = sphere.intersect_line(line)
        point_a, point_b = np.array(point_a), np. array(point_b)
        
        #Check if the point lies between the two points given
        if np.inner(p1-point_a, p2-point_a) < 0 or np.inner(p1-point_b, p2-point_b) < 0:
            #intersects
            return True
        else:
            #does not intersects
            return False
    except:
        return False
        
        

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

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.axes.set_xlim3d(left =0, right=9*LINK_LEN)
ax.set_aspect("equal")
joint_init_pos = initialize_position()
link0, = ax.plot(joint_init_pos[0][:2], -joint_init_pos[2][:2], joint_init_pos[1][:2])
link1, = ax.plot(joint_init_pos[0][1:3], -joint_init_pos[2][1:3], joint_init_pos[1][1:3])
link2, = ax.plot(joint_init_pos[0][2:4], -joint_init_pos[2][2:4], joint_init_pos[1][2:4])
link3, = ax.plot(joint_init_pos[0][3:5], -joint_init_pos[2][3:5], joint_init_pos[1][3:5])
link4, = ax.plot(joint_init_pos[0][4:6], -joint_init_pos[2][4:6], joint_init_pos[1][4:6])
link5, = ax.plot(joint_init_pos[0][5:7], -joint_init_pos[2][5:7], joint_init_pos[1][5:7])
link6, = ax.plot(joint_init_pos[0][6:8], -joint_init_pos[2][6:8], joint_init_pos[1][6:8])
link7, = ax.plot(joint_init_pos[0][7:], -joint_init_pos[2][7:], joint_init_pos[1][7:])

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
    #2 Add spherical obstacles in the form of spherical surface
    
    df_env = pd.read_csv("env_config.csv")
    for i in range(len(df_env.obstacle_id)):
        u = np.linspace(0, 2 * np.pi, 10)
        v = np.linspace(0, np.pi, 10)
        x = df_env.radius[i] * np.outer(np.cos(u), np.sin(v)) + df_env.x[i]
        y = df_env.radius[i] * np.outer(np.sin(u), np.sin(v)) - df_env.z[i]
        z = df_env.radius[i] * np.outer(np.ones(np.size(u)), np.cos(v)) + df_env.y[i]

        # Plot the surface
        ax.plot_surface(x, y, z, color='b')

    return link0, 
    
def animate(i):
    #1 Implement Forward Kinematics 
    x_line, y_line, z_line = get_link_coordinates([df.j0[i], df.j1[i], df.j2[i], df.j3[i], df.j4[i], df.j5[i], df.j6[i], df.j7[i]])
    
    x_line = np.array(x_line)
    y_line = np.array(y_line)
    z_line = np.array(z_line)
    
    link0.set_data(x_line[0:2], -z_line[0:2]); link0.set_3d_properties(y_line[0:2])    
    link1.set_data(x_line[1:3], -z_line[1:3]); link1.set_3d_properties(y_line[1:3])    
    link2.set_data(x_line[2:4], -z_line[2:4]); link2.set_3d_properties(y_line[2:4])    
    link3.set_data(x_line[3:5], -z_line[3:5]); link3.set_3d_properties(y_line[3:5])    
    link4.set_data(x_line[4:6], -z_line[4:6]); link4.set_3d_properties(y_line[4:6])    
    link5.set_data(x_line[5:7], -z_line[5:7]); link5.set_3d_properties(y_line[5:7])    
    link6.set_data(x_line[6:8], -z_line[6:8]); link6.set_3d_properties(y_line[6:8])    
    link7.set_data(x_line[7:], -z_line[7:]); link7.set_3d_properties(y_line[7:])

    return link0, link1, link2, link3, link4, link5, link6, link7 

def main():
    #4 Check for collision free trajectory
    validate_traj(pd.read_csv("env_config.csv"), df)

    #3 Implement Forward Kinematics Animation
    anim = animation.FuncAnimation(fig, animate, init_func=init ,frames=len(np.array(df.time)), interval= 100, blit = True)
    plt.show()

if __name__ == "__main__":
    main()