from netmiko import ConnectHandler

device = {
    "device_type" : "cisco_ios",
    "ip" : "10.10.10.10",
    "username" : "admin",
    "password" : "admin@123",
    "port" : 22
}

connectdevice = ConnectHandler(**device)
fetch = connectdevice.send_command("show version")
print(fetch)
connectdevice.disconnect()
