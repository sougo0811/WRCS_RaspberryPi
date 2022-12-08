import requests

url_water_temp = "https://test811.pythonanywhere.com/raspost_water_temp"
url_water_high = "https://test811.pythonanywhere.com/raspost_water_high"
url_risk_map = "https://test811.pythonanywhere.com/raspost_risk_map"

def post_water_temp(celsius,fahrenheit):
  data = {"RaspberryPi_Name":"test-RaspberryPi", "celsius": celsius, "fahrenheit": fahrenheit}
  rp = requests.post(url_water_temp, data=data)
  return rp

