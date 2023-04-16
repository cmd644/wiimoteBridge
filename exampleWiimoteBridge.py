###Copyright 2023 by Charles Descamps###

### This example uses the deprecated Telnet library to connect to a buzzer emulator
### websocket server to 'buzz' in. This is an example of what is possible using
### the cwiid library. You can use the python built in help functions to learn
### more about the compiled library.

# import libraries
import cwiid # THIS ONE IS AWFUL. I WILL NEVER DEAL WITH IT AGAIN.
from telnetlib import Telnet # Hopefully this isn't deprecated yet...
import time # used to sleep

# define global constants
BUTTON_DELAY = 0.2
BUTTON_TELNET_PORT = 9002

# 'import' Wiimotes, press one and two to get it to 'BT Pair Mode'
# remove comment to 'enable' remote.

# need remote addresses, use hcitool scan to get the MAC Address
# of the wiimote, then put the corresponding address into the () of a
# Wiimote object

print("Press 1+2 on Wiimotes to connect.\n")
# I think they have to be connected in the order of their MAC Address list
# but I'm not sure without testing... (other potential method of connecting)
#wiimoteOne = cwiid.Wiimote()
#wiimoteTwo = cwiid.Wiimote()
#wiimoteThree = cwiid.Wiimote()
#wiimoteFour = cwiid.Wiimote()

wiimoteOne = None
wiimoteOneAttempts = 2
wiimoteTwo = None
wiimoteTwoAttempts = 2
wiimoteThree = None
wiimoteThreeAttempts = 2
wiimoteFour = None
wiimoteFourAttempts = 2

# replaces the above with a more robust method of Wiimote connecting.
while not wiimoteOne:
    try:
        wiimoteOne = cwiid.Wiimote()
    except RuntimeError:
        if (wiimoteOneAttempts > 10):
            print("You must connect at least one Wii remote.")
            quit()
            break
        print("\nError connecting Wiimote One")
        print(f"On attempt {wiimoteOneAttempts}\n")
        wiimoteOneAttempts = wiimoteOneAttempts + 1

while not wiimoteTwo:
    try:
        wiimoteTwo = cwiid.Wiimote()
    except RuntimeError:
        if (wiimoteTwoAttempts > 10):
            #quit()
            print("Wiimote Two is not connected, moving on.")
            break
        print("Error connecting Wiimote Two")
        print(f"On attempt {wiimoteTwoAttempts}\n")
        wiimoteTwoAttempts = wiimoteTwoAttempts + 1

while not wiimoteThree:
    try:
        wiimoteThree = cwiid.Wiimote()
    except RuntimeError:
        if (wiimoteThreeAttempts > 10):
            #quit()
            print("Wiimote Three is not connected, moving on.")
            break
        print("Error connecting Wiimote Three")
        print(f"On attempt {wiimoteThreeAttempts}\n")
        wiimoteThreeAttempts = wiimoteThreeAttempts + 1

while not wiimoteFour:
    try:
        wiimoteFour = cwiid.Wiimote()
    except RuntimeError:
        if (wiimoteFourAttempts > 10):
            #quit()
            print("Wiimote Four is not connected, moving on.")
            break
        print("Error connecting Wiimote Four")
        print(f"On attempt {wiimoteOneAttempts}\n")
        wiimoteFourAttempts = wiimoteFourAttempts + 1

# enables button logging
wiimoteOne.rpt_mode = cwiid.RPT_BTN
wiimoteTwo.rpt_mode = cwiid.RPT_BTN
wiimoteThree.rpt_mode = cwiid.RPT_BTN
wiimoteFour.rpt_mode = cwiid.RPT_BTN
# set the Wiimote LEDs
wiimoteOne.led = 1
wiimoteTwo.led = 2
wiimoteThree.led = 3
wiimoteFour.led = 4

# start the infinite loop to do things throughout game
while True:
    # save all button states(which are stored as raw binary)
    wiimoteOneButtons = wiimoteOne.state['buttons']
    wiimoteTwoButtons = wiimoteTwo.state['buttons']
    wiimoteThreeButtons = wiimoteThree.state['buttons']
    wiimoteFourButtons = wiimoteFour.state['buttons']
    # define exit states
    wiimoteOneExitState = wiimoteOneButtons - cwiid.BTN_PLUS - cwiid.BTN_MINUS
    wiimoteTwoExitState = wiimoteTwoButtons - cwiid.BTN_PLUS - cwiid.BTN_MINUS
    wiimoteThreeExitState = wiimoteThreeButtons - cwiid.BTN_PLUS - cwiid.BTN_MINUS
    wiimoteFourExitState = wiimoteFourButtons - cwiid.BTN_PLUS - cwiid.BTN_MINUS
    # exit check: press Plus and Minus together
    if(wiimoteOneExitState == 0 or wiimoteTwoExitState == 0 or wiimoteThreeExitState == 0 or wiimoteFourExitState == 0):
        if(wiimoteOneExitState == 0):
            print("Wiimote One Connection Closing\n")
            wiimoteOne.rumble = 1
            time.sleep(.5)
            wiimoteOne.rumble = 0
            exit(wiimoteOne)
        elif(wiimoteTwoExitState == 0):
            print("Wiimote Two Connection Closing\n")
            wiimoteTwo.rumble = 1
            time.sleep(.5)
            wiimoteTwo.rumble = 0
            exit(wiimoteTwo)
        elif(wiimoteThreeExitState == 0):
            print("Wiimote Three Connection Closing\n")
            wiimoteThree.rumble = 1
            time.sleep(.5)
            wiimoteThree.rumble = 0
            exit(wiimoteThree)
        else:
            print("Wiimote Four Connection Closing\n")
            wiimoteFour.rumble = 1
            time.sleep(.5)
            wiimoteFour.rumble = 0
            exit(wiimoteFour)
    # Otherwise, check what buttons are pressed from what remote
    # check button states (Button A pressed or Button B pressed)
    wiimoteOnePressA = wiimoteOneButtons & cwiid.BTN_A
    wiimoteOnePressB = wiimoteOneButtons & cwiid.BTN_B
    wiimoteTwoPressA = wiimoteTwoButtons & cwiid.BTN_A
    wiimoteTwoPressB = wiimoteTwoButtons & cwiid.BTN_B
    wiimoteThreePressA = wiimoteThreeButtons & cwiid.BTN_A
    wiimoteThreePressB = wiimoteThreeButtons & cwiid.BTN_B
    wiimoteFourPressA = wiimoteFourButtons & cwiid.BTN_A
    wiimoteFourPressB = wiimoteFourButtons & cwiid.BTN_B
    if(wiimoteOnePressA or wiimoteOnePressB):
      # send the telnet ping to the jeopardy websocket color: red
      with Telnet('localhost', BUTTON_TELNET_PORT) as wiimoteOneTN:
        wiimoteOneTN.write(b"/red\n")
    elif(wiimoteTwoPressA or wiimoteTwoPressB):
      # send the telnet ping to the jeopardy websocket color: green
      with Telnet('localhost', BUTTON_TELNET_PORT) as wiimoteTwoTN:
                wiimoteTwoTN.write(b"/green\n")
    elif(wiimoteThreePressA or wiimoteThreePressB):
      # send the telnet ping to the jeopardy websocket color: blue
      with Telnet('localhost', BUTTON_TELNET_PORT) as wiimoteThreeTN:
                wiimoteThreeTN.write(b"/blue\n")
    elif(wiimoteFourPressA or wiimoteFourPressB):
      # send the telnet ping to the jeopardy websocket color: yellow
      with Telnet('localhost', BUTTON_TELNET_PORT) as wiimoteFourTN:
                wiimoteFourTN.write(b"/yellow\n")
    # continues to the next iteration
