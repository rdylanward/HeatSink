#!/usr/bin/env python

from sn3218 import enable, enable_leds, output
import getopt, sys, time, math, automationhat, pigpio

def action_leds(action_level, one, two, three):
    """

    Formats the enable_mask for enabling/disabling LEDs

    Args:
        action_level (int): Level of LEDs  to be actioned
        one (int): Relay one status
        two (int): Relay two status
        three (int): Relay three status

    """
    
    # Initialise parameters
    global enable_mask
    
    # Set the enable_mask and return the value
    if action_level == 1 and one == 1 and two == 0 and three == 0:  # Level 1
        enable_mask = 0b111000000001000000
    elif action_level == 1 and one == 0 and two == 1 and three == 0:
        enable_mask = 0b111000000100000000
    elif action_level == 1 and one == 0 and two == 0 and three == 1:
        enable_mask = 0b111000010000000000
    elif action_level == 1 and one == 1 and two == 1 and three == 0:
        enable_mask = 0b111000000101000000
    elif action_level == 1 and one == 1 and two == 0 and three == 1:
        enable_mask = 0b111000010001000000
    elif action_level == 1 and one == 0 and two == 1 and three == 1:
        enable_mask = 0b111000010100000000
    elif action_level == 1 and one == 1 and two == 1 and three == 1:
        enable_mask = 0b111000010101000000
    elif action_level == 2 and one == 1 and two == 0 and three == 0:  # Level 2
        enable_mask = 0b111000000001000000
    elif action_level == 2 and one == 0 and two == 1 and three == 0:
        enable_mask = 0b111000000100000000
    elif action_level == 2 and one == 0 and two == 0 and three == 1:
        enable_mask = 0b111000010000000000
    elif action_level == 2 and one == 1 and two == 1 and three == 0:
        enable_mask = 0b111000000101000000
    elif action_level == 2 and one == 1 and two == 0 and three == 1:
        enable_mask = 0b111000010001000000
    elif action_level == 2 and one == 0 and two == 1 and three == 1:
        enable_mask = 0b111000010100000000
    elif action_level == 2 and one == 1 and two == 1 and three == 1:
        enable_mask = 0b111000010101000000
    elif action_level == 2 and one == 0 and two == 0 and three == 0:
        enable_mask = 0b011000000000000000
    elif action_level == 3 and one == 1 and two == 0 and three == 0:  # Level 3
        enable_mask = 0b100000000001000000
    elif action_level == 3 and one == 0 and two == 1 and three == 0:
        enable_mask = 0b100000000100000000
    elif action_level == 3 and one == 0 and two == 0 and three == 1:
        enable_mask = 0b100000010000000000
    elif action_level == 3 and one == 1 and two == 1 and three == 0:
        enable_mask = 0b100000000101000000
    elif action_level == 3 and one == 1 and two == 0 and three == 1:
        enable_mask = 0b100000010001000000
    elif action_level == 3 and one == 0 and two == 1 and three == 1:
        enable_mask = 0b100000010100000000
    elif action_level == 3 and one == 1 and two == 1 and three == 1:
        enable_mask = 0b100000010101000000
    elif action_level == 3 and one == 0 and two == 0 and three == 0:
        enable_mask = 0b000000000000000000

    # Enable/Disable LEDs
    enable_leds(enable_mask)
    output([int((math.sin(float(416)/64.0) + 1.0) * 128.0)]*18)

# Enable GPIO and sn3218 access
pi = pigpio.pi()
enable()
enable_mask = 0b000000000000000000

# If the GPIO connection fails, exit the script
if not pi.connected:
    exit()

# Enable/Disable LEDs
action_leds(1, pi.read(13), pi.read(19), pi.read(16))

# Read the commandline arguments
allArguments = sys.argv

# Further arguments
argumentList = allArguments[1:]

# Valid parameters
unixOptions = "1:2:3:a:"
gnuOptions = ["one=", "two=", "three=", "all="]

try:
    arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))
    sys.exit(2)

# Parse the arguments and carry out the actions
for currentArgument, currentValue in arguments:
    if currentArgument in ("-1", "--one"):
        pi.write(13,int(currentValue))
    elif currentArgument in ("-2", "--two"):
        pi.write(19,int(currentValue))
    elif currentArgument in ("-3", "--three"):
        pi.write(16,int(currentValue))
    elif currentArgument in ("-a", "--all"):
        pi.write(13,int(currentValue))
        pi.write(19,int(currentValue))
        pi.write(16,int(currentValue))
    
    # Enable/Disable actioned LEDs
    action_leds(2, pi.read(13), pi.read(19), pi.read(16))

# Disable comms and warn LEDs
action_leds(3, pi.read(13), pi.read(19), pi.read(16))

# Disable the GPIO connection
pi.stop()
