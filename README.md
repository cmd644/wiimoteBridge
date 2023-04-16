# wiimoteBridge
Python program for connecting Wiimotes to a computer over Bluetooth.

This program uses python to connect Wiimotes to a computer over Bluetooth using CWiid, bluetooth, etc.

## How to use
### Preparing
On your Linux machine, `git pull https://github.com/azzra/python3-wiimote` to your local machine.
Use `sudo apt-get update && sudo apt-get upgrade && sudo apt-get install -Y libcwiid1 libcwiid-dev automake awk bison flex bluez bluetooth python3`
These commands will install all the packages needed for making this work.
### Installing/Compiling from Source
The Cwiid package must be compiled from source, and is done with Automake. Use the below commands to compile everything needed.
- `cd python3-wiimote`
- `aclocal`
- `autoconf`
- `./configure`
- `make`
- Make sure you have Python3 installed and setup correctly for these next commands
- `sudo make install` will copy the compiled cwiid library into Python's library set
After all this is done, everything is setup and ready to go!
### Using the script
- Use `git pull https://github.com/cmd644/wiimoteBridge` to get the example script for connecting four Wiimotes
- Modify the script with your favorite text editor
- Change into the wiimoteBridge directory
- Start the script with `python3 ./wiimoteBridge.py` to get connecting.
### Why this script exists
Flailing around trying to get a buzzer system working with Wiimotes sucks, and the amount of research that I did to make this work is absolutely horrid. 50+ Chrome tabs later, I had found a way to get Wiimotes interacting with a Raspberry Pi. The Cwiid library that isn't available through apt anymore for some reason, as well as the python3 pip package that SAYS it has cwiid in it DOESN'T work and ISN'T maintained anymore, so I had to do much more research coming up with a functional script that could connect these remotes. All of this work to now share on the Internet for some other poor sap who needs to figure out how to do this, I hope you find this script well.
