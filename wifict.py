import network

user = "wifi name"               #wifi name
password = "wifi password"           #wifi Password

n = network.WLAN(network.STA_IF)   #wifi port Configuration
n.active(True)                     #wifi port activation

n.connect(user,password)           #conecting the wifi port with the specified wifi




print('Connection successful')
print(n.ifconfig())               #Details of Connected Wifi




     
  
