import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.transform import Rotation as R
import matplotlib.animation as animation
import pandas as pd
from skspatial.objects import Line, Sphere
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Simulation | Top Gear",
    initial_sidebar_state="expanded"
)

st.title("Simulation")

ENV_CONFIG_FILE = "data/test_env_config.csv"
TRAJ_FILE = "data/test_traj.csv"
INPUT_FILE = "data/test_input.csv"
LINK_LEN = 100
PI = np.pi
ANGLE_MAX = PI/2
VELOCITY_MAX = 3.0
ACC_MAX = 3.0

df = pd.read_csv(TRAJ_FILE)
df_env = pd.read_csv(ENV_CONFIG_FILE)
df_input = pd.read_csv(INPUT_FILE)

collision_txt = st.empty()
wall_collision_txt = st.empty()
obstacle_col_txt = st.empty()
angle_exceed_txt = st.empty()
velocity_exceed_txt = st.empty()
acc_exceed_txt = st.empty()
start_point_txt = st.empty()

def collision_check(p1, p2, center, radius):
    # p1 and p2 are the ends of the line segment representing a link
    # Conditions for collision
    # intersection points lie between the two link ends
    # returns
    # 1 = Intersects with sphere
    # 0 = Free Path
    # 2 = Intersects with Wall
    # 3 = Intersects with Wall and Sphere

    sphere = Sphere(center, radius)
    line = Line(p1, p2)
    point_a = []
    point_b = []
    collision_type = 0

    if p1[0] <=0 or p2[0] <=0:
        #Link crosses/touches the wall
        collision_type = 2

    try:
        point_a, point_b = sphere.intersect_line(line)
        point_a, point_b = np.array(point_a), np. array(point_b)
        
        #Check if the point lies between the two points given
        if np.inner(p1-point_a, p2-point_a) < 0 or np.inner(p1-point_b, p2-point_b) < 0:
            #intersects
            if collision_type == 2:
                #Intersects both wall and sphere
                collision_type = 3

            else:
                collision_type = 1
            
            return collision_type
        else:
            #does not intersects
            return collision_type
    except:
        return collision_type
        
        

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

def validate_traj(df_env, df_traj, df_input):
    # Get all the obstacle data and store them
    obstacles = []
    for obstacle in range(len(df_env.obstacle_id)):
        obstacles.append([df_env.x[obstacle], df_env.y[obstacle], df_env.z[obstacle], df_env.radius[obstacle]])

    # Get all velocity and acceleration values
    velocity_joint = [[],[],[],[],[],[],[],[]]
    acc_joint = [[],[],[],[],[],[],[],[]]

    for a in range(len(df_traj.columns) - 1):
        for b in range(len(df_traj.time) - 1):
            #joint a and instant b
            velocity_joint[a].append((df_traj[df_traj.columns[a+1]][b+1] - df_traj[df_traj.columns[a+1]][b])/(df_traj.time[b+1] - df_traj.time[b]))

    for a in range(len(velocity_joint)):
        for b in range(len(velocity_joint[0]) - 1):
            #joint a and instant b
            acc_joint[a].append((velocity_joint[a][b+1] - velocity_joint[a][b])/(df_traj.time[b+1] - df_traj.time[b]))
        

    # Go over all the trajectory points and see if it collides
    for instant in range(len(df_traj.time)):
        x_line, y_line, z_line = get_link_coordinates([df.j0[instant], df.j1[instant], df.j2[instant], df.j3[instant], df.j4[instant], df.j5[instant], df.j6[instant], df.j7[instant]])
    
        x_line = np.array(x_line)
        y_line = np.array(y_line)
        z_line = np.array(z_line)

        collision_list = []
        wall_collision = False

        #Check for collision
        for i in range(len(x_line)-2):
            p1 = np.array([x_line[i], y_line[i], z_line[i]])
            p2 = np.array([x_line[i+1], y_line[i+1], z_line[i+1]])
            for j in range(len(obstacles)):
                result = collision_check(p1, p2, obstacles[j][:3], obstacles[j][3])
                
                # Collision with only spherical obstacle
                if result == 1 and j not in collision_list:
                    collision_list.append(int(j))

                elif result == 2:
                    wall_collision = True
                
                elif result == 3:
                    wall_collision = True
                    collision_list.append(int(j))

    global wall_collision_txt
    global collision_txt
    global obstacle_col_txt
    global angle_exceed_txt
    global velocity_exceed_txt
    global acc_exceed_txt
    global start_point_txt

    st.markdown("## Summary")
    
    # Trajectory Time Taken
    st.markdown("Flight Time: " + ":blue[" + str(df_traj.time[len(df_traj.time)-1]) + "] seconds")

    if wall_collision:
        wall_collision_txt = st.markdown("Wall Collision Test: :red[Failed]")
    else:
        wall_collision_txt = st.markdown("Wall Collision Test: :green[Passed]")

    if len(collision_list) > 0:
        obstacle_col_txt = st.markdown("Obstacle Collision Test: :red[Failed]")
        collision_txt = st.markdown("Link collides with: " + str(len(collision_list)) + " obstacle(s)")

    else:
        obstacle_col_txt = st.markdown("Obstacle Collision Test: :green[Passed]")


    # TODO:Correct Start Point Test
    for i in range(len(df_input.columns) - 1):
        if abs(df_input[df_input.columns[i+1]][0] - df_traj[df_traj.columns[i+1]][0]) > ANGLE_MAX/100:
            #Wrong start point
            start_point_txt = st.markdown("Start point test: :red[Failed]")
            break
    else:
        #Correct Start Point
        start_point_txt = st.markdown("Start point test: :green[Passed]")



    # TODO:Goal Reached Test


    # Angle Exceeding
    for i in range(len(df.columns) - 1):
        if max(df_traj[df_traj.columns[i+1]]) > ANGLE_MAX or min(df_traj[df_traj.columns[i+1]]) < -ANGLE_MAX:
            angle_exceed_txt = st.markdown("Angle limits test: :red[Failed]")
            break
    else:
        angle_exceed_txt = st.markdown("Angle limits test: :green[Passed]")

    # Velocity Exceeding
    for i in range(len(velocity_joint)):
        if max(velocity_joint[i]) > VELOCITY_MAX or min(velocity_joint[i]) < -VELOCITY_MAX:
            velocity_exceed_txt = st.markdown("Velocity limits test: :red[Failed]")
            break
    else:
        velocity_exceed_txt = st.markdown("Velocity limits test: :green[Passed]")

    # Acceleration Exceeding
    for i in range(len(acc_joint)):
        if max(acc_joint[i]) > ACC_MAX or min(acc_joint[i]) < -ACC_MAX:
            acc_exceed_txt = st.markdown("Acceleration limits test: :red[Failed]")
            break
    else:
        acc_exceed_txt = st.markdown("Acceleration limits test: :green[Passed]")

def main():
    #4 Check for collision free trajectory
    validate_traj(df_env, df, df_input)

    #3 Implement Forward Kinematics Animation
    anim = animation.FuncAnimation(fig, animate, init_func=init ,frames=len(np.array(df.time)), interval= 100, blit = True)
    components.html(anim.to_jshtml(), height=10000)

if __name__ == "__main__":
    #Add Input File
    input_csv = st.file_uploader("Choose Input CSV file", type="csv", accept_multiple_files=False)
    input_file_status = st.empty()
    if input_csv is not None:
        input_file_status = st.markdown(":green[File uploaded]")
    else:
        input_file_status = st.markdown(":red[Upload File]")


    #Add Environment File
    env_config_csv = st.file_uploader("Choose Environment CSV file", type="csv", accept_multiple_files=False)
    env_file_status = st.empty()
    if env_config_csv is not None:
        env_file_status = st.markdown(":green[File uploaded]")
    else:
        env_file_status = st.markdown(":red[Upload File]")


    #Add Trajectory File
    traj_csv = st.file_uploader("Choose Trajectory CSV file", type="csv", accept_multiple_files=False)
    traj_file_status = st.empty()
    if traj_csv is not None:
        traj_file_status = st.markdown(":green[File uploaded]")
    else:
        traj_file_status = st.markdown(":red[Upload File]")


    #File Upload status
    status_txt = st.empty()

    if env_config_csv is not None and traj_csv is not None and input_csv is not None:
        status_txt = st.markdown(":green[All Files Uploaded. Simulating...]")
        df = pd.read_csv(traj_csv)
        df_env = pd.read_csv(env_config_csv)
        df_input = pd.read_csv(input_csv)
        main()