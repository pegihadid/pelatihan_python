listname = ["Zayn Malik", "Niall Horan", "Louis Tomlinson"]
#print (listname)
    #for variable in listname:
    #print (variable)
print (listname[1])
print (listname[-1])
print (listname[::-1])

#reverse
print (listname[::-1])
listname.reverse()
print(listname)

#number
number = 1 + 2 + 3 / 4.0
print(number)

#modulus
mod = 10 % 3
print (mod)

#perpangkatan
squared = 7 ** 2
cubed = 2 ** 3
print (squared)
print (cubed)

#concade
#tambah string + string
helloworld = "hello" + "" + "world"
print (helloworld)

#using operators with list
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print (all_numbers)

#basic string operations
astring = "Hello World!"
print ("single quotes are '(what's this??)' ")
print (len(astring))
string = "john doe"
print (len(string))

#string formatting
myString = "Luke Skywalker"
myInt = 12
myFloat = 1.8

#reference use index
print ("The string is {0} nad the integer is {1}". format (myString, myInt))
lst = {'name': 'Obi-Wan Kenobi', 'role': 'Jedi Master'}
print ("Welcome {name}, {role}". format (name = lst['name'], role=lst['role']))
print ("Welcom {name}, {role}". format (**lst))
  
#get use index:
astring = "Hello Me!"
print (astring.index("o"))
print (astring.count("1"))
print (astring [3:7])

#split
afewwords = astring.split(" ")
print(afewwords)

#Boolean OPerators
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")
if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

          
#if and else
diajelek = False
diacakep = True
if diacakep is True:
    # do something
    print("alhamdulillah")
    pass
elif diajelek is True: #else if
    #do something else
    print("do skincare")
    pass
else:
    #do another thing
    print("apanih")
    pass






