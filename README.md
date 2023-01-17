# Top Gear 2023
![TopGearLogo](/data/full_width.png "title")
## Using the Simulator
* To use the simulator make sure you are connected to the internet.
* Navigate to the Simulations tab using the sidebar on the left.
* Upload the input csv file containing in the specified [format](#formats).
* Upload the environment configuration file in the specified [format](#formats).
* Upload the csv file containing the timestamped joint angles in the specified [format](#formats).
* Individual file upload status will be updated upon successful upload.
* After successful upload of all the files, a message will be shown **All Files Uploaded. Simulating...**, and after a few seconds the line diagram animation of the robotic arm could be seen.


## Indicators and their meaning
* Upload File - Input file not uploaded/Upload unsuccessful
* File Uploaded - File Uploaded successfully
* All Files Uploaded. Simulating... - All required files uploaded files and the webapp has started simulating based on the input
* Wall Collision Test - Checks for collision with the wall in YZ plane.
* Obstacle Collision Test - Checks for collision with the spherical objects
* Link collides with: **N** obstacle(s) - The robot collides with **N** number of obstacles.
* Start point test: Checks whether the planned path has the correct initial position or not.
* Goal point test: Checks whether the planned path reaches to the goal position or not.
* Angle limits test: Checks if angles are in limit specified (-PI/2 to PI/2)
* Velocity limits test: Checks if velocities are in limit specified (-3 to 3) rad/s
* Acceleration limits test: Checks if accelerations are in limit specified (-3 to 3) rad/(s^2)


## In case of any query

## Formats
1. [Test Input CSV Format](/data/test_input.csv)
2. [Test Environment Config CSV Format](/data/test_env_config.csv)
3. [Test Trajectory CSV Format](/data/test_traj.csv)
