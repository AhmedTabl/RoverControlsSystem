import socket
import pygame

# Define the IP address and port of receiver code
server_ip = "127.0.0.1"
server_port = 12345

# Create a socket for communication
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.connect((server_ip,server_port))

# Initialize pygame and the controller
pygame.init()
controller = pygame.joystick.Joystick(0)
controller.init()


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

TRIGGER_THRESHOLD = 0.001
button_states = [False] * controller.get_numbuttons()

gantry = 0
spin = 0
wrist_right = 0
wrist_left = 0
cam1x = 90
cam1y = 90
cam2x = 90
cam2y = 90
shoulder = 0
claw = 0

isReverseCam1y = False
isReverseCam2y = False
isReverseCam1x = False
isReverseCam2x = False
isReverseOptions = False
isReverseShare = False
isReverseClaw = False



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
                drive_command = f"D_{left_pwm}_{right_pwm}_{left_pwm}_{right_pwm}_{left_pwm}_{right_pwm}"
                client_socket.send(drive_command.encode())


                if event.axis == 4:  # L2

                    if event.value > TRIGGER_THRESHOLD:
                        gantry = int((event.value + 1) * 63.5) #pwm 0 -> 127
                        print(f"{gantry}")


                elif event.axis == 5:  # R2

                    if event.value > TRIGGER_THRESHOLD:
                        gantry = int((event.value + 1) * 64 + 127) #pwm 127 -> 255

            if event.type == pygame.JOYBUTTONDOWN:

                button_pressed = event.button

                button_states[button_pressed] = True  # Set the button state to pressed

                if button_pressed == BUTTON_L1: #L1
                    if spin > 10:
                        spin = spin - 10

                elif button_pressed == BUTTON_R1: #R1
                    if spin < 245:
                        spin = spin +10

                if button_pressed == D_UP:
                    if not isReverseCam1y:
                        cam1y += 5
                        if cam1y >= 180:
                            isReverseCam1y = True
                    else:
                        cam1y -= 5
                        if cam1y <= 0:
                            isReverseCam1y = False

                elif button_pressed == D_DOWN:
                    if not isReverseCam2y:
                        cam2y += 5
                        if cam2y >= 180:
                            isReverseCam2y = True
                    else:
                        cam2y -= 5
                        if cam2y <= 0:
                            isReverseCam2y = False

                elif button_pressed == D_RIGHT:
                    if not isReverseCam1x:
                        cam1x += 5
                        if cam1x >= 180:
                            isReverseCam1x = True
                    else:
                        cam1x -= 5
                        if cam1x <= 0:
                            isReverseCam1x = False

                elif button_pressed == D_LEFT:
                    if not isReverseCam2x:
                        cam2x += 5
                        if cam2x >= 180:
                            isReverseCam2x = True
                    else:
                        cam2x -= 5
                        if cam2x <= 0:
                            isReverseCam2x = False


                elif button_pressed == BUTTON_OPTIONS:
                    if not isReverseOptions:
                        wrist_right += 5
                        if wrist_right >= 255:
                            isReverseOptions = True
                    else:
                        wrist_right -= 5
                        if wrist_right <= 0:
                            isReverseOptions = False

                elif button_pressed == BUTTON_SHARE:
                    if not isReverseShare:
                        wrist_left += 5
                        if wrist_left >= 255:
                            isReverseShare = True
                    else:
                        wrist_left -= 5
                        if wrist_left <= 0:
                            isReverseShare = False

                elif button_pressed == BUTTON_X:
                    if 0 < shoulder <= 255:
                        shoulder -= 5

                elif button_pressed == BUTTON_TRIANGLE:
                    if 0 <= shoulder < 255:
                        shoulder += 5

                elif button_pressed == BUTTON_O:
                    if not isReverseClaw:
                        claw += 5
                        if claw >= 255:
                            isReverseClaw = True
                    else:
                        claw -= 5
                        if claw <= 0:
                            isReverseClaw = False

            # Create and send Arm Command packet
            arm_command = f"A_{shoulder}_{wrist_right}_{wrist_left}_{claw}_{gantry}_{spin}_{cam1x}_{cam1y}_{cam2x}_{cam2y}"
            client_socket.send(arm_command.encode())

except KeyboardInterrupt:
    # close the socket
    client_socket.close()
