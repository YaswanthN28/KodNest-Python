def display_invoice_total(price, quantity):
    # Write your code here
    total=price * quantity
    print("Total: ",total)

price = float(input("enter the price: "))
quantity = int(input("enter the quantity: "))

display_invoice_total(price, quantity)