# Top Gear 2023
![TopGearLogo](/data/full_width.png "title")
## Using the Simulator
* To use the simulator make sure you are connected to the internet.
* Navigate to the Simulations tab using the sidebar on the left.
* Upload the input csv file containing in the specified format.
* Upload the environment configuration file in the specified format.
* Upload the csv file containing the timestamped joint angles in the specified format.
* Individual file upload status will be updated upon successful upload.
* After successful upload of all the files, a message will be shown :green[**All Files Uploaded. Simulating...**], and after a few seconds the line diagram animation of the robotic arm could be seen.


## Indicators and their meaning
:red[Upload File] - Input file not uploaded/Upload unsuccessful
:green[File Uploaded] - File Uploaded successfully
:green[All Files Uploaded. Simulating...] - All required files uploaded files and the webapp has started simulating based on the input
:red[Wall Collision Detected!!] - During simulation of the given trajectory and environment configuration, the links are colliding with the wall present in the YZ plane.
:blue[Link collides with: **N** obstacle(s)] - During simulation of the given trajectory and environment configuration, the links are colliding with **N** number of obstacles while executing the trajectory.

## Formats

## In case of any query