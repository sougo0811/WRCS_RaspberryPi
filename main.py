import time
import pump, watertemp, webpost

temp = watertemp.watertemp()
if temp[0] >= 20:
  pump.pump()
rp = webpost.post_water_temp(temp[0],temp[1])
print(rp)