# Glitch Sensorium

## Plant Pot (Being)
### Wireless stereo music with Ableton + Raspberry Pi + Plant Sensors

#### Electronics Components: 

* Raspberry Pi 3 B+
* [ADC ADS1115](https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/ads1015-slash-ads1115) 
* [YL-69 soil moisture sensor](https://randomnerdtutorials.com/guide-for-soil-moisture-sensor-yl-69-or-hl-69-with-the-arduino/)
* [KY-015 temperature and humidity sensor](https://sensorkit.joy-it.net/fr/sensors/ky-015)
* [Flex sensor](https://cdn.sparkfun.com/assets/9/5/b/f/7/FLEX_SENSOR_-_SPECIAL_EDITION_DATA_SHEET_v2019__Rev_A_.pdf?_gl=1*1aahvmc*_ga*NjcxMTAzMTI2LjE2OTIwMjU5NjI.*_ga_T369JS7J9N*MTY5MjAyNTk2Mi4xLjEuMTY5MjAyNTk4Ni4zNi4wLjA)
* [Stereo Amp 20W MAX9744](https://letmeknow.fr/fr/arduino/2069-stereo-20w-class-d-audio-amplifier-max9744-0701980281716.html)
* 2 speakers : todo add source

#### Software:

* Ableton Live 11
* Max4Live
* ControlChange8
* Kontakt >=5
* Geosonics by Soniccouture
* Python 3.11
* loopMIDI

#### How to
* On the Raspberry Pi : sendSensorUDP.py
* On the computer : UDPAbleton.py
* Then play Ableton
