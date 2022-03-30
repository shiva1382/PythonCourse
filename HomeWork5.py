#question 1
import math

x = float(input('Enter The value of Degrees:'))
n = int(input('Enter The number of terms:'))

sine = 0
for i in range(n):
    sign = math.pow(-1, i)
    pi = math.pi
    a = x * (pi / 180)
    sine = sine + (sign * (a ** (2.0 * i)) / math.factorial(2 * i + 1))

print(sine)


#question 2

print('lotfan adad aval ra vared konid')
avali = int(input())

print('lotfan adad aval ra vared konid')
dovomi = int(input())

MagsoomMoshtarak=0

for r in range(2,avali+1) :
 if avali % r ==0 :
   for i in range(2,dovomi+1):
     if dovomi % i ==0 :
      if i==r:
        if i>= MagsoomMoshtarak:
          MagsoomMoshtarak = i
print(MagsoomMoshtarak)


#question 3
for i in range(10000):
    n = len(str(i))
    result = 0
    temp = 0

    while temp > 0:
        digit = temp % 10
        result += digit ** n
        temp //= 10

    if i == result:
        print(i)
        
        
  #question 5
text = str(input("enter text: "))
s = int(input("enter shift: "))
result = ""
for i in range(len(text)):
    char = text[i]
    if char.isupper():
        result += chr((ord(char) + s - 65) % 26 + 65)
    else:
        result += chr((ord(char)
print("")
print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + result)  
                       
                       
 #question 6
sum_number = 0
average_number = 0
a = float(input("enter number: "))
minimum_number = 0
maximum_number = 0
for v in range(1, 19):
    a = float(input("enter number: "))
    sum_number += a
    if a > maximum_number:
        maximum_number = a

    elif a < minimum_number:
        minimum_number = a

print("sum: ", sum_number)
print("maximum: ", maximum_number)
print("minimum", minimum_number)
print("average: ", sum_number/20)                      
