from netmiko import ConnectHandler

#create and return netmiko connection 
def connect_device(device_details):
    result = ConnectHandler(**device_details)
    return result

# send command using connection, recieve the output, return it as string
def execute_command(connection, command):
    output = connection.send_command(command)
    return output


