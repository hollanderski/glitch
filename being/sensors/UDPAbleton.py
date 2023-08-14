import socket
import sys
from struct import unpack
import time
import rtmidi # https://spotlightkid.github.io/python-rtmidi/
from midioutwrapper import MidiOutWrapper
from rtmidi.midiutil import open_midioutput
import numpy as np

# todo : deal with range boundary error
from scipy.interpolate import interp1d
soil_map = interp1d([8000,13000],[0,127])
bend_map = interp1d([2000,7500],[127,0])


# Soil moiture data : number that ranges from -32768 to 32767 on the 16-bit ADS1115 
'''

Gain = 2/3
8K (water/ moist pot)
17K (air)
13K (dry pot)

Gain = 1

13-15k (moist pot) 
26K (air) 

'''

# Utils functions 

# Send CC message to Ableton

def modulateMusic(val, cc=3):
    mw.send_control_change(cc, val)


# Play MIDI note 

def playNote():
    mv.send_message(note_on)
    time.sleep(0.5) 
    mv.send_message(note_off)


import threading

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def toy_music():
    set_interval(playNote, 3)




# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
host, port = '0.0.0.0', 65000
server_address = (host, port)

print(f'Starting UDP server on {host} port {port}')
sock.bind(server_address)


midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

# here we're printing the ports to check that we see the one that loopMidi created. 
# In the list we should see a port called "loopMIDI port".
print(available_ports)

# Attempt to open the port
if available_ports:
    mout = midiout.open_port(1)
else:
    midiout.open_virtual_port("My virtual output")

note_on = [0x90, 60, 112]
note_off = [0x80, 60, 0]


mw = MidiOutWrapper(mout, ch=1)



while True:
    # Wait for message
    message, address = sock.recvfrom(4096)

    x, y, z = unpack('3f', message)

    soil_moisture = soil_map(x)
    soil_moisture = int(np.round(soil_moisture))
    print(x, soil_moisture)
    modulateMusic(soil_moisture, cc=4)

    bend = bend_map(y)
    bend = int(np.round(bend))
    print(y, bend)
    modulateMusic(bend, cc=3)




