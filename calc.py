#tip calculator
def tip():

    n = float(input("Enter price in Kenya shillings: "))
    if n >= 3000.00:
        t = n * 0.30
    else:
        t = n * 0.10
    print(t)

tip()






