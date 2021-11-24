a = '321'
print(type(a))
# '' is used. So it is a string, if only no then int

b = 321
print (type(b))
# type() class is int

c = 7.21
print(type(c))
print( )
# type() <class is float>

# EXPLICIT TYPE FUNCTION CONVERSION :
# To convert one type class to another, type the new class then ( old input class ) ex: to convert int to float - float(fun_int)
#Convert int to float :
num_int = 21
num_float = float(num_int)
print(num_float)
print("Datatype class of num_float is :", type(num_float))
# <class float'>

# converting string to int & int to float
a = '21'
b = int(a)
c = float(b)
print(a,b,c)
print( type(a) , type(b) , type(c) )

# int and float to str
a = 12
b = float(a)
c = str(b)
print (b,c)
print(type(c))

a = '21.3'
b = float(a)
d = int(b)
c = str(d)
print(c)
# We cannot convert '' decimals directly to int, float -> int