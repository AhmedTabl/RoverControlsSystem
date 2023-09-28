import socket
import pygame

# Initialize pygame and the controller
pygame.init()
controller = pygame.joystick.Joystick(0)
controller.init()

# Define the IP address and port of your receiver code
server_ip = "127.0.0.1"  # Replace with the actual IP address
server_port = 12345  # Replace with the actual port number

# Create a socket for communication
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Controller Buttons Index values
BUTTON_X = 0
BUTTON_O = 1
BUTTON_TRIANGLE = 2
BUTTON_SQUARE = 3
BUTTON_L1 = 4
BUTTON_R1 = 5
BUTTON_L2 = 6
BUTTON_R2 = 7
BUTTON_SHARE = 8
BUTTON_OPTIONS = 9
BUTTON_L3 = 10
BUTTON_R3 = 11
BUTTON_PS = 12
BUTTON_TOUCHPAD = 13


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
                print("Sent Drive Command:", drive_command)

            elif event.type == pygame.JOYBUTTONDOWN:
                # Read button presses
                button = event.button

                if button == BUTTON_X:
                    print("lol")

        # Perform other actions and send additional control commands here
        # ...

except KeyboardInterrupt:
    # Clean up and close the socket
    client_socket.close()
