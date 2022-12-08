import requests

url_test = "https://test811.pythonanywhere.com/raspost_test"
url_test_local = "http://127.0.0.1:8000/raspost_test"
url_water_temp = "https://test811.pythonanywhere.com/raspost_water_temp"
url_water_high = "https://test811.pythonanywhere.com/raspost_water_high"
url_risk_map = "https://test811.pythonanywhere.com/raspost_risk_map"

def test():
  data = {"title":"test-RaspberryPi", "text": "contents"}
  rp = requests.post(url_test, data=data)
  print(rp)

def temp():
  data = {"RaspberryPi_Name":"test-RaspberryPi", "celsius": 10.0, "fahrenheit": 50.0}
  rp = requests.post(url_water_temp, data=data)
  print(rp)

test()
temp()