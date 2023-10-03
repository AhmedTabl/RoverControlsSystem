import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_socket.bind(("localhost", 12345))


left_wheel1 = 0
left_wheel2 = 0
left_wheel3 = 0
right_wheel1 = 0
right_wheel2 = 0
right_wheel3 = 0

cam1x = 90
cam1y = 90
cam2x = 90
cam2y = 90

shoulder = 0
wrist_right = 0
wrist_left = 0
claw = 0
gantry = 0
spin = 0

print("Waiting for data...")

while True:
    # Receive data
    data, client_address = server_socket.recvfrom(1024)
    dataRecv = data.decode()

    data_array = dataRecv.split("_")

    if data_array[0] == "D":

        left_wheel1 = data_array[1]
        left_wheel2 = data_array[2]
        left_wheel3 = data_array[3]
        right_wheel1 = data_array[4]
        right_wheel2 = data_array[5]
        right_wheel3 = data_array[6]

        print("{"
              "Drive_Command:\n"
              "\tleft_wheel1: " + left_wheel1 + "\n"
              "\tleft_wheel2: " + left_wheel2 + "\n"
              "\tleft_wheel3: " + left_wheel3 + "\n"
              "\tright_wheel1: " + right_wheel1 + "\n"
              "\tright_wheel2: " + right_wheel2 + "\n"
              "\tright_wheel3: " + right_wheel3 + "\n"
              "}")

    if data_array[0] == "A":

        shoulder = data_array[1]
        wrist_right = data_array[2]
        wrist_left = data_array[3]
        claw = data_array[4]
        gantry = data_array[5]
        spin = data_array[6]

        cam1x = data_array[6]
        cam1y = data_array[7]
        cam2x = data_array[8]
        cam2y = data_array[9]

        print("{"
              "Arm_Command:\n"
              "\tshoulder: " + shoulder + "\n"
              "\twrist_right: " + wrist_right + "\n"
              "\twrist_left: " + wrist_left + "\n"
              "\tclaw: " + claw + "\n"
              "\tgantry: " + gantry + "\n"
              "\tspin: " + spin + "\n"
              "}")

        print("{"
              "Camera_Position\n"
              "\tcam1x: " + cam1x + "\n"
              "\tcam1y: " + cam1y + "\n"
              "\tcam2x: " + cam2x + "\n"
              "\tcam2y: " + cam2y + "\n"
              "}")
