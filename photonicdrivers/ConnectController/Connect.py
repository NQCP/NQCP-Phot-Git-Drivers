

import pygame

# Initialize Pygame
pygame.init()

# Initialize the joystick module
pygame.joystick.init()

# Get count of joysticks
joystick_count = pygame.joystick.get_count()

# Print some information about the connected joysticks
for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    print("Joystick {}:".format(i))
    print("Name:", joystick.get_name())
    print("ID:", joystick.get_id())
    print("Number of axes:", joystick.get_numaxes())
    print("Number of buttons:", joystick.get_numbuttons())
    print("Number of hats:", joystick.get_numhats())
    print("\n")

# Main loop to read input
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get input from the first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    # Read input
    axes = [joystick.get_axis(i) for i in range(joystick.get_numaxes())]
    buttons = [joystick.get_button(i) for i in range(joystick.get_numbuttons())]
    hats = [joystick.get_hat(i) for i in range(joystick.get_numhats())]

    # Print the input
    print("Axes:", axes)
    print("Buttons:", buttons)
    print("Hats:", hats)

    # Add some delay to avoid excessive printing
    pygame.time.delay(10)










