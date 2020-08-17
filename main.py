# num=int(input("Enter a number: "))
# if num>30:
#   print(num*3)

# else:
#   print(num+90)

# print("we are done")

# def five_or_three(num):
#   if num==5:
#     return True
#   elif num==3:
#     return True
#   else:
#     return False

def is_divisible_by(num, divisor1, divisor2):
    if num%divisor1==0:
      print(f'This number is divisible by {divisor1}')
    if num%divisor2==0:
      print(f'This number is divisible by {divisor2}')
    if (num%divisor1==0) and (num%divisor2==0):
      print(f'This number is divisible by {divisor1} and {divisor2}')
    else: 
      print(f'This number is not divisible by either {divisor1} or {divisor2}')
      return False


print(is_divisible_by(8,4,2))



    
    
