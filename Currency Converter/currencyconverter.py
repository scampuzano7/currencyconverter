import mycon

print ("A - USD to AUD", "B - USD to EURO", "C - AUD to USD", "D - AUD to EURO", "E - EURO to USD", "F - EURO to AUD")
x = str(input("Enter: "))
y = str(input("Another: "))
if x == "USD" and y == "AUD":
    curOne = float(input("USD: "))
    curTwo = float(input("AUD: "))
    print (mycon.my_function(curOne, curTwo))

elif x == "USD" and y == "EURO":
    curOne = float(input("USD: "))
    curTwo = float(input("EURO: "))
    print (mycon.my_function(curOne, curTwo))


else: 
   print("Butts")
