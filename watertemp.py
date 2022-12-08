from w1thermsensor import W1ThermSensor, Unit

sensor = W1ThermSensor()

def watertemp():
  temperature_in_celsius = sensor.get_temperature()
  temperature_in_fahrenheit = sensor.get_temperature(Unit.DEGREES_F)
  #print("celsius:    {0:.3f}".format(temperature_in_celsius))
  #print("fahrenheit: {0:.3f}".format(temperature_in_fahrenheit))
  celsius = float(temperature_in_celsius)
  fahrenheit = float(temperature_in_fahrenheit)
  return celsius, fahrenheit