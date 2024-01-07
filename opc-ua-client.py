from opcua import Client
from opcua import ua
import time
url = "opc.tcp://192.168.0.1:4840"
client = Client(url)
client.connect()
print("client connected")


motor_status = client.get_node('ns=3;s="motor1"')
status = motor_status.get_value()
motor_speed = client.get_node('ns=3;s="speed1"')
speed = motor_speed.get_value()
motor_temp = client.get_node('ns=3;s="temp1"')
temp = motor_temp.get_value()



print(status)
print(speed)
print(temp)

print("#"*40)

data_value1 = ua.DataValue(ua.Variant(False, ua.VariantType.Boolean))
motor_status.set_value(data_value1)
status = motor_status.get_value()

data_value2 = ua.DataValue(ua.Variant(2000, ua.VariantType.Int16))
motor_speed.set_value(data_value2)
speed = motor_speed.get_value()

data_value3 = ua.DataValue(ua.Variant(20.88, ua.VariantType.Float))
motor_temp.set_value(data_value3)
temp = motor_temp.get_value()

print(status)
print(speed)
print(temp)

time.sleep(1)

    # Stop the server on program exit
client.close_session()