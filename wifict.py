import network,time

user = "vivo 1917"               #wifi name
password = "sivakrish"           #wifi Password

n = network.WLAN(network.STA_IF)   #wifi port Configuration
n.active(True)                     #wifi port activation

n.connect(user,password)           #conecting the wifi port with the specified wifi
time.sleep(5)



print('Connection successful')
print(n.ifconfig())               #Details of Connected Wifi




     
  