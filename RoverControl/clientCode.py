import socket
import pygame

# Initialize pygame and the controller
pygame.init()
controller = pygame.joystick.Joystick(0)
controller.init()

# Define the IP address and port of your receiver code
server_ip = "127.0.0.1"
server_port = 12345

# Create a socket for communication
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Controller Buttons Index values
BUTTON_X = 0
BUTTON_O = 1
BUTTON_SQUARE = 2
BUTTON_TRIANGLE = 3
BUTTON_SHARE = 4
BUTTON_PS = 5
BUTTON_OPTIONS = 6
BUTTON_L3 = 7
BUTTON_R3 = 8
BUTTON_L1 = 9
BUTTON_R1 = 10
D_UP = 11
D_DOWN = 12
D_LEFT = 13
D_RIGHT = 14

TRIGGER_THRESHOLD = 0.1

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                # Read analog joystick values (left stick)
                left_x = controller.get_axis(0)
                left_y = controller.get_axis(1)

                # Read analog joystick values (right stick)
                right_x = controller.get_axis(2)
                right_y = controller.get_axis(3)

                # Scale joystick positions to PWM values (0 to 255)
                left_pwm = int((left_y + 1) * 127.5)  # Scale to 0-255
                right_pwm = int((right_y + 1) * 127.5)  # Scale to 0-255

                # Create and send Drive Command packet
                drive_command = f"D_{left_pwm}_{right_pwm}"
                client_socket.sendto(drive_command.encode(), (server_ip, server_port))

                # Print the sent packet
                #print("Sent Drive Command:", drive_command)

                if event.axis == 4:  # L2
                    if event.value > TRIGGER_THRESHOLD:
                        print("L2 trigger is pressed")

                elif event.axis == 5:  # R2
                    if event.value > TRIGGER_THRESHOLD:
                        print("R2 trigger is pressed")

            elif event.type == pygame.JOYBUTTONDOWN:
                # Read button presses
                button = event.button

                if button == BUTTON_R3:
                    print("lol")



except KeyboardInterrupt:
    # close the socket
    client_socket.close()
