from netmiko import ConnectHandler

router={'host':'10.1.1.20',
        'username':'muco',
        'password':'1234',
        'secret':'1234',
        'device_type':'cisco_ios',
        'verbose':True}

conn=ConnectHandler(**router)
conn.enable()
a=conn.send_config_from_file("rip.txt")
print(a)
conn.disconnect()