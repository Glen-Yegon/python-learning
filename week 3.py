def calculate_discount(price, discount_percent):
    if float(discount_percent) >= 0.2:
        final_price = int(price) * (1 - float(discount_percent))
        print("The final price is: " + str(final_price))
    else:
        print("The final price is: " + str(price))
price = input("The price is: ")
discount_percent = input("The discount_percent: ")
calculate_discount(price, discount_percent)
