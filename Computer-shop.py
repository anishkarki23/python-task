print("=======Computer Bazar==========")
print("1.Dell (Rs 20000) 2.Toshiba (Rs 30000) 3. Mac (Rs 50000) ")

option = int(input("Enter option:"))

dell_price = 0
toshiba_price = 0
mac_price = 0
qt = 0
delivery_price = 0
plastic_price = 0
gift_price = 0
bag_price = 0
tax_amt= 0

if option == 1:
    qt = int(input("Enter Quantity"))
    dell_price += qt * 20000
elif option == 2:
    qt = int(input("Enter Quantity"))
    toshiba_price += qt * 30000
elif option == 3:
    qt = int(input("Enter Quantity"))
    mac_price += qt * 50000
else:
    print("Invalid selection")
    exit()

print("Delivery 1. Home delivery (Rs 1000) 2. Free Delivery")

delivery = int(input("Choose delivery option"))
if delivery == 1:
    delivery_price += 1000
else:
    pass

print("Packing 1. Plastic( Rs 500) 2. bag (Rs 1000) 3. Gift box( Rs 5000) 4.none")

packing = int(input("Enter your option"))

if packing == 1:
    plastic_price += 500
elif packing == 2:
    bag_price += 1000
elif packing == 3:
    gift_price += 5000
else:
    pass

print("Location 1.Ktm (13% tax) 2. BKT (Free) 3. LTP (Free)")
location_option = int(input("Select Location"))

total_price = dell_price+toshiba_price+mac_price
if location_option == 1:
    tax_amt += total_price * 0.13

gt = total_price + tax_amt + delivery_price + plastic_price + bag_price + gift_price

print(f"Quantity: {qt} Total: {total_price} tax : {tax_amt} Grand Total :{gt}")