# Script for generating POs, GRNs and Invoices. It also generates a file with a list of all PO numbers.
# This is useful when performing 3-way checks.

import random

POs = list(range(1000,10000))

Stationary = (("Office Paper", 2.79),("Royal Mail Stamps", 0.25),
              ("Ballpoint Pen Red x 10", 1.50), ("Ballpoint Pen Blue x 10", 1.50),
              ("Ballpoint Pen Black x 10", 1.50), ("Envelopes x 100", 2.99),
              ("Hole Puncher", 3.49), ("Dividers x 100", 0.99), ("Document Wallet", 0.50),
              ("Marker Red x 3", 1.50),("Marker Blue x 3", 1.50), ("Marker Black x 3", 1.50),
              ("Notepad", 1.99), ("Marker Red x 3", 1.50), ("Batteries AA x 16", 1.89),
              ("Highlighter 4 Colours", 1.59), ("Sticky Notes", 1.99), ("Office Chair", 29.99),
              ("Stapler Small", 11.99), ("Stapler Large", 25.99), ("Ink Cartridge Black", 35.99),
              ("Ink Cartriage Colour", 45.99), ("USB Memory Stick 16 GB", 5.99),
              ("USB Memory Stick 32 GB", 7.99), ("External Hard Drive 1 TB", 55.99),
              ("External Hard Drive 2 TB", 65.99), ("External Hard Drive 500 MB", 35.99))
OrderSize = list(range(5,20))
ItemNumbers = list(range(1,10))
Months = ("January", "February", " March", "April", "May", "June", "July", "August", "September", "October",
         "November", "December")
Days = list(range(1,20))
Suppliers = ("Cabbodle Office Supplies", "Warrens Office Supply", "Fusion Office Ltd", "Staples UK",
             "Ryman", "UK Office Direct")

i = 0
POList = []
while i <= 10:

# PO Here

    a = random.choice(POs)
    POList.append(a)
    FileName = "PO" + str(a) + ".txt"
    f = open(FileName, 'w+')
    OrderVolume = random.choice(OrderSize)
    OrderType = random.sample(Stationary, k = OrderVolume)
    Order = {}
    Day = random.choice(Days)
    Month = str(random.choice(Months))
    Supplier = random.choice(Suppliers)
    for y in OrderType:
        Order[y] = random.choice(ItemNumbers)
    f.write("PO Number: " + str(a))
    f.write('\n')
    f.write('\n')
    f.write("Supplier: " + Supplier)
    f.write('\n')
    f.write('\n')
    f.write("Delivery Date: " + str(Month) + " " + str(Day))
    f.write('\n')
    f.write('\n')
    f.write("ORDER DETAILS: ")
    f.write('\n')
    f.write('\n')
    for x in Order:
        f.write("Type: " + str(x[0]) + " - " + " Price p.u.: £" + str(x[1]) + " - " + "Quantity: " + str(Order[x]))
        f.write("\n")
    f.close()

 #   print("Order")
 #   print(Order)
 #   print(" ")
    
# GRN Here

    FileName = "GRN" + str(a)+ ".txt"
    f = open(FileName, 'w+')
    Received = {}
    for y in Order:
        Received[y[0]] = Order[y]
    f.write("PO Number: " + str(a))
    f.write('\n')
    f.write('\n')
    f.write("GRN: " + str(a) + "01")
    f.write('\n')
    f.write('\n')
    f.write("Date: " + Month + " " + str(Day))
    f.write('\n')
    f.write('\n')
    f.write("RECEIVED: ")
    f.write('\n')
    f.write('\n')
    for x in Received:
        f.write("Type: " + str(x) + " - " + " Quantity: " + str(Received[x]))
        f.write("\n")
    f.close()
    
#    print("GRN")
#    print(Received)
#    print(" ")
    
# Invoice Here

    FileName = "INVOICE" + str(a)  + ".txt"
    f = open(FileName, 'w+')
    Invoice = {}
    for y in Order:
        Invoice[y] = round(Received[y[0]]*y[1],2)
    f.write("Invoice from " + Supplier)
    f.write('\n')
    f.write('\n')
    f.write("PO Number: " + str(a))
    f.write('\n')
    f.write('\n')
    f.write("Invoice Date: " + Month + " " +  str(Day+1))
    f.write('\n')
    f.write('\n')
    f.write("Date by which payment: " + Month + " " + str(Day+4))
    f.write('\n')
    f.write('\n')
    f.write("Invoice Number: " + str(random.choice(POs)))
    f.write('\n')
    f.write('\n')
    f.write("PURCHASED: ")
    f.write('\n')
    f.write('\n')
    for x in Invoice:
        f.write("Type: " + str(x[0]) + " - " + "Amount: £" + str(Invoice[x]))
        f.write("\n")
    f.close()
    i = i + 1
 #   print("Invoice")
 #   print(Invoice)
    
# PO List

FileName = 'POList'  + ".txt"
f = open(FileName, 'w+')
f.write(str(POList))
f.close()

