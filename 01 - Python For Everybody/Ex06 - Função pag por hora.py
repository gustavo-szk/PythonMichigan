def pagamentohora(hrs, tx):
    if hrs > 40:
        hm = hrs - 40
        hrs = hrs - hm
        prc = ((hm * ( tx * 1.5 )) + (hrs * tx))
    else:
        prc = hrs * tx
    return prc

hrs = float(input("Enter Hours:"))
tx = float(input("Enter Tax:"))

p = pagamentohora(hrs, tx)

print("Pague: ", p)