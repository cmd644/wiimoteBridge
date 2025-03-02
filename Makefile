CC = g++ -Wall -std=c11 -pedantic
SOURCES = wiimoteBridge.cpp 
OBJECTS = wiimoteBridge.o 

all: wiimoteBridge

wiimoteBridge: $(OBJECTS)
	$(CC) $(OBJECTS) -o wiimoteBridge

wiimoteBridge.o: wiimoteBridge.cpp
	$(CC) -c wiimoteBridge.cpp -o wiimoteBridge.o

clean:
	rm -f $(OBJECTS) wiimoteBridge wiimoteBridge.out

clean_objects:
	rm -f $(OBJECTS)

run:
	./wiimoteBridge