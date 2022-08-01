# LieBiao AND ZiDian
# LieBiao => [] && ZiDian => {}
# => LieBiaoDemo
import ipaddress


hostName = ['R1', 'R2', 'R3', 'S1', 'S2']
print(type(hostName))
print(len(hostName))
print(hostName)
# GenJuXiaBiao HuoQuYuanSu
print(hostName[0])  # First
print(hostName[-1])  # Last
hostName[0] = 'RTR1'  # Change First => RTR1
print(hostName)
del hostName[3]
print(hostName)


# => ZiDianDemo
# Create ZiDian => {}
ipAddress = {"R1": "10.1.1.1", "R2": "10.2.2.1", "R3": "10.3.3.1"}
print(ipAddress)
print(type(ipAddress)) # dict

# Selete item in ZiDian => []
print(ipAddress['R1']) # => 10.1.1.1
# Add new ZiDian Item => ipAddress['Name'] = Value
ipAddress["S1"] = '10.1.1.10'
print(ipAddress)
# Add More Value by one KeyName
ipAddress["R3"] = ["10.3.3.3.1","10.3.3.3.","10.3.3.3.3"]
print(ipAddress)


