mystring1 = "This One Is Double Quoted"
mystring2 = 'also works single quoted.'

print("a string with single quotes 'like this' and with double quote \"here\"")

print(mystring1.index('One')) #zero based index

print(mystring2.count("o"))

#[] are used like ranges in math which include from that number
print(mystring1[:4])    #this
print(mystring1[5:8])   #one
print(mystring1[-6:])   #quoted = from 6 spaces from the end until the end
print(mystring1[12:-7]) #double = start at 12 until 7 spaces from the end
print(mystring1[:12])   #this one is = from the beginning until 12 spaces
print(mystring1[9]+mystring1[10])  #i+s = is

#slice
#If all three start, stop and step are provided, 
#it generates portion of sequence after index start till stop with increment of index step.
print(mystring1[::-1])    #start:stop:step = all backwards
print("electrodomestico")
print("electrodomestico"[::2])   #all, every two letters
print("electrodomestico"[-9::3])   #domestico, every three letters == dei

print(mystring1.upper())
print(mystring1.lower())

print(mystring1.startswith('This'))
print(mystring2.endswith("aleluya"))

afewwords = mystring1.split(" ")

print("eof")