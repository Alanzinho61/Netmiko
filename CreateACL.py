from netmiko import ConnectHandler

router={'host':'10.1.1.10',
        'username':'muco',
        'password':'1234',
        'secret':'1234',
        'device_type':'cisco_ios',
        'verbose':True}

conn=ConnectHandler(**router)
c=["access-list 101 permit tcp any any eq 80","access-list 101 permit tcp any any eq 443",'access-list 101 deny ip any any']

conn.enable()
o=conn.send_config_set(c)
conn.send_command("show ip  interface")
print(o)