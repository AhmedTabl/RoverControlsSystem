import pygame

# Initialize pygame and the controller
pygame.init()
controller = pygame.joystick.Joystick(0)
controller.init()

threshold = 0.1

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:

                if event.value > threshold:
                    print(f"Axis {event.axis} is pressed")

except KeyboardInterrupt:
    # Clean up and exit
    pygame.quit()
