from netmiko import ConnectHandler
import getpass

# user_pass=getpass.getpass("kullanici giris sifresi:")
# enable_pass=getpass.getpass("yetkilis giris sifresi:")
router={'host':'10.1.1.10',
        'username':'muco',
        'password':'1234',
        'secret':'1234',
        'device_type':'cisco_ios',
        'verbose':True}


sifrem=router.get("secret")
sifre=getpass.getpass()
if sifre ==sifrem:
    conn = ConnectHandler(**router)
    conn.enable()
    a=conn.find_prompt()[:-1]
    print(a)

else:
    print(" sifre yanlis")
