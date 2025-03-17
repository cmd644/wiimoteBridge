###Copyright 2025 by Charles Descamps###

# import libraries
import cwiid # THIS ONE IS AWFUL. I WILL NEVER DEAL WITH IT AGAIN.
import time # used to sleep
import telnetlib

# define global constants
BUTTON_DELAY = 0.2

# 'import' Wiimotes, press one and two to get it to 'BT Pair Mode'
# remove comment to 'enable' remote.

# need remote addresses, use hcitool scan to get the MAC Address
# of the wiimote, then put the corresponding address into the () of a
# Wiimote object

print("Press 1+2 on Wiimotes to connect.\n")
# I think they have to be connected in the order of their MAC Address list
# but I'm not sure without testing... (other potential method of connecting)
#wiimoteOne = cwiid.Wiimote()

wiimoteOne = None
wiimoteOneAttempts = 2

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

# enables button logging
wiimoteOne.rpt_mode = cwiid.RPT_BTN
# set the Wiimote LEDs
wiimoteOne.led = 1

# setup the telnet connection to the wss server
buzzCli = telnetlib.Telnet("127.0.0.1", 8181)

# start the infinite loop to do things
while True:
    # save all button states(which are stored as raw binary)
    wiimoteOneButtons = wiimoteOne.state['buttons']
    # define exit states
    wiimoteOneExitState = wiimoteOneButtons - cwiid.BTN_PLUS - cwiid.BTN_MINUS
    # exit check: press Plus and Minus together
    if(wiimoteOneExitState == 0):
        if(wiimoteOneExitState == 0):
            print("Wiimote One Connection Closing\n")
            wiimoteOne.rumble = 1
            time.sleep(.5)
            wiimoteOne.rumble = 0
            exit(wiimoteOne)
        buzzCli.close()
    # Otherwise, check what buttons are pressed from what remote
    # check button states (Button A pressed or Button B pressed)
    wiimoteOnePressA = wiimoteOneButtons & cwiid.BTN_A
    wiimoteOnePressB = wiimoteOneButtons & cwiid.BTN_B
    if(wiimoteOnePressA or wiimoteOnePressB):
      # DO SOMETHING
      print("Wiimote One Pressed A or B.")
      buzzCli.write(b"/red\n")
    # continues to the next iteration
