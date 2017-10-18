def fares(age, student=False, senior=False):
    if age>=20 and age <65:
        if student==True:
            return "price is 20kr"
        elif senior==True:
            return "price is 20kr"

        else:
            return "price is 30kr"
    elif age <20 and age >65:
        if student==True:
            return "price is 20kr"
        elif senior==True:
            return "price is 20kr"
    else:
        return "price is 20kr"





print fares(70,senior=True)
print fares(70)
print fares(50)
print fares(25,student=True)
print fares(15,student=True)