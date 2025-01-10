# Basic simulated flight script file in order to test out the manual joystick control and attempting to map joystick actions to something in the script.


from pymavlink import mavutil


# Define connection parameters

CONN_STR = 'udp:127.0.0.1:14551'
MESSENGER_PORT = 14552


# Connect to mavlink

connect = mavutil.mavlink_connection(CONN_STR)


# Check if the mavlink is alive (handshake is completed)

connect.wait_heartbeat()


# Implement the mavlink MANUAL_CONTROL Protocol. For more info ....
# See: https://mavlink.io/en/services/manual_control.html
# See: https://mavlink.io/en/messages/common.html#MANUAL_CONTROL


target_system = 0 # System to be controlled
z = 100 # Amount of Z control 

# The idea with this is to test how the system behaves and how fast it moves, etc. 


# See docs for what the parameters mean (I'm not typing allat for a test file)
connect.mav.manual_control_send(target_system, 0, 0, z, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

connect.mav.manual_control_send(target_system, 0, 0, -z, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
