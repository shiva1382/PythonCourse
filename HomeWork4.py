#unintentional infinite loop
MAX = 20
n = 1

while n <= MAX:
  factor = 1
  print(end=str(n)  + ':  ')
  while factor <= n:
    if n % factor == 0:
      print(factor, end='  ')
      factor += 1
      print()
       n +=1
        
        
        
  max_value = int(input("Display primws up tp what value ? "))

value = 2

while value <= max_value:
    is_prime = True
    trial_factor = 2
    while trial_factor < value:
        if value % trial_factor == 0:
            is_prime = False
            break
        trial_factor += 1
    if is_prime:
        print(value,end=" ")
    value += 1
print()      
