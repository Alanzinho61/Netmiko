from netmiko import  ConnectHandler

def execute(device,command):
    conn=ConnectHandler(**device)
    send_comm=conn.send_command(command)
    print(send_comm)
    conn.disconnect()


cisco={'host':'10.1.1.10',
        'username':'muco',
        'password':'1234',
        'secret':'1234',
        'device_type':'cisco_ios',
        'verbose':True}
execute(cisco,"show ip interface")

linux={'host':'192.168.1.61',
        'username':'kali',
        'password':'146128',
        'secret':'146128',
        'device_type':'linux',
        'verbose':True}
execute(linux,'ifconfig')

# "Pattern not detected: '[\\$\\#]' in output." gave an error