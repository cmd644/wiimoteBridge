# wiimoteBridge
Python program for connecting Wiimotes to a computer over Bluetooth.

This program uses python to connect Wiimotes to a computer over Bluetooth using CWiid, bluetooth, etc.

## How to use
### Preparing
- On your Linux machine, `git clone https://github.com/azzra/python3-wiimote` to your local machine(if you want to build the Python module from source).
- Use `sudo apt-get update && sudo apt-get upgrade && sudo apt-get install -Y libcwiid1 libcwiid-dev automake awk bison flex bluez bluetooth python3` or `sudo apt-get install -Y libcwiid1 libcwiid-dev bluez bluetooth python3 python3-wiimote` if you choose not to build from source.
- These commands will install all the packages needed for making this work.
### Installing/Compiling from Source
The Cwiid package can be compiled from source, and is done with Automake. Use the below commands to compile everything needed.
- `cd python3-wiimote`
- `aclocal`
- `autoconf`
- `./configure`
- `make`
- Make sure you have Python3 installed and setup correctly for these next commands
- `sudo make install` will copy the compiled cwiid library into Python's library set
- If the second preparation APT install command was done, this section is redundant.
After all this is done, everything is setup and ready to go!
### Using the script
- Use `git clone https://github.com/cmd644/wiimoteBridge` to get the example script for connecting four Wiimotes
- Modify the script with your favorite text editor or use the #RemoteBridge.py scripts if you need a certain number of remotes.
- Change into the wiimoteBridge directory
- Start the script with `python3 ./wiimoteBridge.py` to get connecting.
### Why this script exists
Flailing around trying to get a buzzer system working with Wiimotes sucks, and the amount of research that I did to make this work is absolutely horrid. 50+ Chrome tabs later, I had found a way to get Wiimotes interacting with a Raspberry Pi. The Cwiid library that isn't available through apt anymore for some reason, as well as the python3 pip package that SAYS it has cwiid in it DOESN'T work and ISN'T maintained anymore, so I had to do much more research coming up with a functional script that could connect these remotes. All of this work to now share on the Internet for some other poor sap who needs to figure out how to do this, I hope you find this script well.

### Why this project exists
Documenting my journey on making these Wii Remotes turn themselves into buzzers to work with the [Things with Buzzers Jeopardy/TWB](https://github.com/andygrunwald/things-with-buzzers-jeopardy) project was a bit of a challenge and took a lot of research. Since there is the software buzzer emulation, which as far as I could tell was not meant to be used in this fashion, I decided to not make physical buzzers. I was sent on a quest to figure out how to make these Wii Remotes turn themselves into functional buzzers to play games of Jeopardy with. After struggling with it in 2023, and getting something somewhat working, (I think I was limited to the computing power of the Raspberry Pi available at that time) I was almost ready to give up since my local development version wouldn't connect to the websocket part of the TWB project. I returned a couple of years later when I learned a bit more, figuring I could get something working. After returning to it with some better Raspberry Pi computing power(and fixing my broken code), I was able to get the Wiimotes to connect and function like buzzers. They even work nicely with the TWB project!
