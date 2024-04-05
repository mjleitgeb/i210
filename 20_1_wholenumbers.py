

nums = []
num = input("Enter a whole number: ")

while num.lower() != 'quit':
   try:
       if int(num) >= 0:
           nums.append(int(num))
           
       else:
           print('Not a whole number')
           
   except Exception as e:
       print("Not a number.")
    
   num = input("Enter a whole number: ") 
nums.sort()
if nums:
    print('Your numbers are', nums)
else:
    print('You have no numbers')
