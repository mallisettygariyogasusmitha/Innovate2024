currency = {"USD": 580, "GBP":700, "CAD": 400, "EUR": 650, "CHF": 450, "YEN":200}


print('''Welcome to your currency converter App

         For USD conversion to Naira type USD,
         For GBP conversion to Naira type GBP,
         For CAD conversion to Naira type CAD,
         For EUR conversion to Naira type EUR,
         For CHF conversion to Naira type CHF,
         For YEN conversion to Naira type YEN,*''')


signs = input('Type the currency you want to convert to: ').upper()
amount = float(input('Enter the amount you want to convert: '))

if signs =="USD" or signs =="GBP" or signs =="CAD" or signs =="EUR" or signs =="CHF" or signs =="YEN":
    conversion = amount * currency[signs]
    print("The conversion of {}{} to naria is NGN {}".format(signs,amount, conversion))
else:
    print("You have entered a wrong value for the conversion")
