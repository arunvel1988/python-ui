router_name = "Core-Router-1"
total_memory = 32
used_memory = 18

available_memory = total_memory - used_memory
memory_usage_percentage = (used_memory / total_memory) * 100

print("Device Name :", router_name)
print("Total Memory :", total_memory, "GB")
print("Used Memory :", used_memory, "GB")
print("Available Memory :", available_memory, "GB")
print("Memory Usage :", memory_usage_percentage, "%")
