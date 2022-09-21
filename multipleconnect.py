from netmiko import ConnectHandler
devices=["10.1.1.10","10.1.1.20","10.1.1.30"]
for dev in  devices:
        router={'host':dev,
                'username':'muco',
                'password':'1234',
                'secret':'1234',
                'device_type':'cisco_ios',
                'verbose':True}
        conn = ConnectHandler(**router)
        conn.enable()
        a=conn.send_command("show ip interface")
        print(a)
        conn.disconnect()

