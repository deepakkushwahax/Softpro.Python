new_tuples = eval(input("Enter the tuples: "))
#new_tuples = (10,20,30)
ln = len(new_tuples)
sum = 0

for i in new_tuples:
    sum = sum + i
    
print("The sum of Tuples: ",sum) 
print("Avg of Tuples: ",sum/ln) 