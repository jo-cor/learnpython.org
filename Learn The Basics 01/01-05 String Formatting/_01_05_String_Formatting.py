name = "Juanito"
print("Que onda %s, comomagres has estado?" % name)

age=13
print("Ese %s, neta tienes %d?" %(name, age))

myList=["a","b","c"]
print("printeando mi lista %s " % myList)

myList.append(name)
myList.append(str(age))
print("my extended list {}".format(myList))

#    %s - String (or any object with a string representation, like numbers)
#    %d - Integers
#    %f - Floating point numbers
#    %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#    %x/%X - Integers in hex representation (lowercase/uppercase)