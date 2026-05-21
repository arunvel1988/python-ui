# STRING
router_name = "CoreRouter"

# INTEGER
active_users = 120

# FLOAT
cpu_usage = 67.5

# BOOLEAN
device_status = True

# LIST
interfaces = ["Gig0/0", "Gig0/1", "Gig0/2"]

# TUPLE
location = ("New York", "Rack-21")

# DICTIONARY
device_info = {
    "ip": "192.168.1.1",
    "vendor": "Cisco"
}

# OPERATORS
total_interfaces = len(interfaces)
remaining_cpu = 100 - cpu_usage

print("Router Name :", router_name)
print("Users Connected :", active_users)
print("CPU Usage :", cpu_usage)
print("Device Status :", device_status)

print("\nInterfaces :", interfaces)
print("Device Location :", location)

print("\nIP Address :", device_info["ip"])
print("Vendor :", device_info["vendor"])

print("\nTotal Interfaces :", total_interfaces)
print("Available CPU :", remaining_cpu)
