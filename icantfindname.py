from netmiko import ConnectHandler

router={'host':'10.1.1.10',
        'username':'muco',
        'password':'1234',
        'secret':'1234',
        'device_type':'cisco_ios',
        'verbose':True}

conn=ConnectHandler(**router)
prompname=conn.find_prompt()

newname=prompname.strip(">")
print(newname)
result=conn.send_command("show ip interface brief e0/0")
print(result)
with open(f'{newname}.txt',"w") as f:
    f.write(result)