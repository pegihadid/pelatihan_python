listname = ["Zayn Malik", "Louis Tomlinson", "Niall Horan","Liam Payne"]
#print (listname)
    #for variable in listname:
    #print (variable)
print (listname[1])
print (listname[-1])
print (listname[::-1])

helloworld = "hello" + "" + "world"
print(helloworld)

#reverse
print (listname[::-1])
listname.reverse()

#python3
print(f"hello(mystring)")

astring = "helloworld!"
print ("single quotes are ' ")
print(len(astring))

astring = "hello world!"
print(astring.index("0"))

astring = "hello world!"
print(astring.count("1"))
print(astring[3:7])

#[start:stop:step]
astring = "Hello World!"
print(astring[3:7:2])

astring = "Hello world!"
print(astring[::-1])
print(astring.upper())
print(astring.lower())

astring = "Hello World!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

#split
astring = "Hello World!"
afewwords = astring.split("")

Conditions
x = 2
print(x == 2)

Boolean operators
name = "John"
age = 23
if name == "John" and age ==23:
    print("Your name is John, and you are also 23 years old.")
if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

The "in" operator:
name = "Luke"
if name in ["Luke","Han"]:
    print("Your name is either Luke.")

#if and else
statement = False
another_statement = True
if Dia jelek is True:
    #do something
    pass
elif another_statement is True:#else if
    #do something else
    pass
else:
    #do another thing 
    pass

