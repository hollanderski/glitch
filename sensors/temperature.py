import time
import board
import adafruit_dht

# Initialisez le dispositif dht avec la broche de données connectée à la broche 16 (GPIO 23) du Raspberry Pi :
dhtDevice = adafruit_dht.DHT11(board.D23)

# Vous pouvez passer DHT22 use_pulseio=False si vous ne voulez pas utiliser pulseio.
# Cela peut être nécessaire sur un ordinateur monocarte Linux comme le Raspberry Pi,
# mais cela ne fonctionnera pas avec CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

while True:
    try:
        # Imprimer les valeurs via l'interface série
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidity))

    except RuntimeError as error:
        # Les erreurs sont assez fréquentes, les DHT sont difficiles à lire, passez à autre chose.
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)