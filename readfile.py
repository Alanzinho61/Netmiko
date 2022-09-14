from netmiko import ConnectHandler

with open('routerinfo.txt') as f:
    info=f.read().split(':')


print(info)
#for i in info:
router={
    'host':info[0],
    'username':info[1],
    'password':info[2],
    'secret':info[3],
    'device_type':info[4],
    'verbose':info[5]
}

con=ConnectHandler(**router)
result=con.send_command('show ip interface e0/0')
print(result)