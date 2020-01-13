#Binary Converter 1
#Rowbottom
#Sept 26 2019
#Program converts decimal numbers into binary

#declare variables to store place values for 8 bits and initialize to zero
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0

#Get decimal number from User and store in value variable
val = int(input("enter in a number to convert"))
#store integer divsion of dividing by 128
a = val // 128
#store modulus of 128 into original value variable
val = val % 128
#store integer divsion of dividing by 64
#store modulus of 64 into original value variable
#store integer divsion of dividing by 32
#store modulus of 32 into original value variable
#store integer divsion of dividing by 16
#store modulus of 16 into original value variable
#store integer divsion of dividing by 8
#store modulus of 8 into original value variable
#store integer divsion of dividing by 4
#store modulus of 4 into original value variable
#store integer divsion of dividing by 2
#store modulus of 2 into original value variable
#store integer divsion of dividing by 1
#store modulus of 1 into original value variable
#store concatenation of all digits into a string output variable
#report output variable

#declare ariables to store place values for 8 bits and initialize to zero
a = 0 #ones;
b = 0 #twos
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0 #128s

#Get decimal number from User and store in value variable
val = int(input("Type in a decimal number to convert\n The values should be from 0-255 \n"))

##one after another from largest to smallest 
#store integer divsion of dividing by 128
h = val//128
#store modulus of 128 into original value variable
val %= 128
#val = val % 128
#store integer divsion of dividing by 64
g = val//64
#store modulus of 128 into original value variable
val%=64

#store integer divsion of dividing by 32
f = val//32
#store modulus of 32 into original value variable
val%=32

#store integer divsion of dividing by 16
e = val//16

#store modulus of 16 into original value variable
val%=16

#store integer divsion of dividing by 8
d = val//8

#store modulus of 8 into original value variable
val%=8

#store integer divsion of dividing by 4
c = val//4

#store modulus of 4 into original value variable
val%=4

#store integer divsion of dividing by 2
b= val//2

#store modulus of 2 into original value variable
val%=2

#store integer divsion of dividing by 1
a = val//1

#store modulus of 1 into original value variable
val%=1
#store cancatenation of all digits into a string output variable
output = str(h)+str(g)+str(f)+str(e)+str(d)+str(c)+str(b)+str(a)

#report output variable
print("The binary equivalent is ", output)
