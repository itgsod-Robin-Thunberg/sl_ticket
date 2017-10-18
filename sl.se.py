def fares(age, student=False, senior=False):
    if age>=20 and age <65:
        if student==True:
            print "price is 20kr"
        elif senior==True:
            print "price is 20kr"

        else:
            print "price is 30kr"
    elif age <20 and age >65:
        if student==True:
            print "price is 20kr"
        elif senior==True:
            print "price is 20kr"
    else:
        print "price is 20kr"






fares(70)
fares(50)
fares(25,student=True)
fares(15,student=True)