import sys

# ******* First we collect all PO numbers stored in the file POList.txt *********

f = open("POList.txt")

x = f.readline()

i = 1

PONumbers = []

while i < len(x):

    PONumbers.append(x[i:i+4])

    i = i + 6
               
f.close()

# ********* Next we collect data from POs, GRNs and Invoices. *********

Continue = "Y"

while Continue in ["Yes", "yes", "y", "Y"]:
    PO = {}
    Invoice = {}
    GRN = {}
# Prompt the user for a PO number.

    PONumber = input("Enter PO number: ")
    print("\n")

# Check that it is a valid PO number.

    while PONumber not in PONumbers:
        
        print("That PO number doesn't exist.\n\n")
        
        PONumber = input("Enter a valid PO number or type 'Quit': ")
        print("\n\n")

        if PONumber in ['quit', 'Quit']:

            sys.exit()
    
# If PO valid we begin collecting data from PO file.

    f = open("PO" + PONumber + ".txt", "r+")

# Creating an empty dictionary.



    for x in f:

# Looks for lines that start with the word "Type".

        if x[0:4] == "Type":

# i = 7 ensures that the programme starts reading the given line from the 7th
# character; namely the first letter of the item to be read.

            i = 7

# The next while loop collects all characters until the first - appears. That is
# it copies the name of the item.

            while x[i] != "-":
                i = i + 1

# Once name of item is collected, we give it the temporary Python name of Item.
# Next we continue reading the line to find the price. The price will start with
# £ symbol and end with an empty space ' '.

            Item = x[6:i]
            
            while x[i] != "£":
                i = i + 1
                
            j = i + 1
            
            while x[i] != ' ':
                i = i + 1
                
# Once we know were the price starts and ends on the line, we read the last
# character of the line (i.e., quantity) and save them as the value of the key
# Item in our dictionary.

            PO[Item] = (float(x[j:i]),int(x[len(x)-2]))
            
    f.close()

# Collecting data from GRN file, if it exists! We ommit the comments.

    
    try:
        f = open("GRN" + PONumber + ".txt", "r+")

        for x in f:

            if x[0:4] == "Type":
                i = 7

                while x[i] != "-":       
                    i = i + 1

                Item = x[6:i]

                GRN[Item] = int(x[len(x) - 2])

        f.close()

    except:

        print("There is no GRN for the given PO.\n\n")
        
# Collecting data from Invoice, if it exists.

    try:

        f = open("INVOICE" + PONumber + ".txt", "r+")

        for x in f:

            if x[0:4] == "Type":
                i = 7

                while x[i] != "-":       
                    i = i + 1

                item = x[6:i]

                while x[i] != "£":
                    i = i + 1

                
                Invoice[item] = float(x[i+1:len(x) - 1])


        f.close()

    except:

        print("* There is no Invoice for the given PO.\n\n")


# ***** AFTER DATA COLLECTION WE FOCUS ON 3-WAY CHECKING ******

# Comparing PO with GRN, if the latter exists.

    if GRN != {}:
        
        missingItems = []

        extraItems = []

        wrongQuantity = []
        
        for item in PO:

            if item not in GRN:

                missingItems.append(item)

            elif PO[item][1] != GRN[item]:

                wrongQuantity.append(item)

        if missingItems != []:
            
            print("* The following items are missing from the GRN: \n\n")

            print(str(missingItems) + "\n\n")


        if wrongQuantity != []:
              
            print("* PO and GRN quantities do not match for the following items: \n\n")

            print(str(wrongQuantity) + "\n\n")

        
        for item in GRN:

            if item not in PO:

                extraItems.append(item)
                
        if extraItems != []:
            
            print("* The following GRN items are missing from the PO: \n\n")

            print(str(extraItems) + "\n\n")

            
# Compare GRN quantity vs Invoice, both directions.

    if Invoice != {} and GRN != {}:

        receivedNotInvoiced = []

        invoicedNotReceived = []

        for item in GRN:

            if item not in Invoice:

                receivedNotInvoiced.append(item)

        for item in Invoice:

            if item not in GRN:

                invoicedNotReceived.append(item)

        if invoicedNotReceived != []:

            print("* The following invoiced items do not appear in the GRN:\n\n")

            print(str(invoicedNotReceived) + "\n\n")


        if receivedNotInvoiced != []:
            
            print("The following item have been received and not invoiced: \n\n")

            print(str(receivedNotInvoiced) + "\n\n")

            
    elif GRN == {}:

        print("GRN is empty. \n\n")

# Comparing PO with Invoice, if the latter exists. Also, check if Inoviced for items
# not ordered.

    if Invoice != {}:

        incorrectPrice = []

        notOrdered = []

        for item in Invoice:

            if item not in PO:

                notOrdered.append(item)

            elif round(float(PO[item][0])*int(PO[item][1]),2) != round(float(Invoice[item]),2):
              
                incorrectPrice.append(item)

        if incorrectPrice != []:

            print("* The Invoice amount for the following does not match the POs:\n\n")

            print(str(incorrectPrice) + "\n\n")


        if notOrdered != []:

            print("* The following invoiced items do not appear in the PO:\n\n")

            print(str(notOrdered) + "\n\n")


    else:

         print("Invoice is empty.\n\n")


    Continue = input("Would you like to process another transaction? Y/N ")
    print("\n\n")
          
