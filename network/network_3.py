cpu_usage = 92
memory_usage = 70

print("Checking Device Health...\n")

if cpu_usage > 90:
    print("Critical Alert : High CPU Usage")

elif memory_usage > 85:
    print("Warning : High Memory Usage")

else:
    print("Device Operating Normally")
