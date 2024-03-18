number = int(input("Enter The Num: "))
temp = number
rev = 0
while(temp>0):
    dig = temp % 10
    rev = rev*10 + dig
    temp = temp // 10
if(number==rev):
  print("the number is palindrome",rev)
else:
    print("The given number is not palindrome")
