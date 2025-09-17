
import re

email = "customer123@shop.com"
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

if re.match(pattern, email):
    print("Valid email for customer signup")
else:
    print("Invalid email")

#Start → username (letters, numbers, allowed symbols)
#Must have @
#Valid domain (letters, numbers, dots, dashes)
#Literal dot .
#TLD (2+ letters)
#End


#############################################

text = "Customer placed orders: Order-1001, Order-1002, and Order-1003"
pattern = r"Order-\d+"

#"Order-" followed by one or more digits.
order_ids = re.findall(pattern, text)
print(order_ids)  


###################################################


payment_log = "Payment done using card 4111111111111234"
pattern = r"\d{12}(\d{4})"
#regex matches a 16-digit number, where the first 12 digits are matched, and the last 4 digits are captured for later use
masked = re.sub(pattern, "************\\1", payment_log)
print(masked)  # Payment done using card ************1234

##############################


phone = "9876543210"
pattern = r"^[6-9]\d{9}$"
#Matches a 10-digit mobile number that starts with 6, 7, 8, or 9
if re.match(pattern, phone):
    print("Valid phone number for COD delivery")
else:
    print("Invalid phone number")

###########################


product_list = "Available: SKU-101, SKU-102, SKU-250, SKU-300"
pattern = r"SKU-\d+"

skus = re.findall(pattern, product_list)
print(skus)   # ['SKU-101', 'SKU-102', 'SKU-250', 'SKU-300']

######################################


pincode = "411001"
pattern = r"^\d{6}$"

if re.match(pattern, pincode):
    print("Valid pincode for delivery")
else:
    print("Invalid pincode")

#################################