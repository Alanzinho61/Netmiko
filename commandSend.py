from netmiko import ConnectHandler

router={'username':'muco',
        'host':'10.1.1.10',
        'device_type':'cisco_ios',
        'password':'1234',
        'secret':'1234',
        'verbose':True}

conn=ConnectHandler(**router)
result=conn.send_command('show arp')
print(result)