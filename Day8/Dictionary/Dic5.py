# WAP to check the number of occurrence of each characters present in a string in python using Dictionry

word = input("Enter the word: ")
new_dic = {}
for i in word:
    new_dic[i] = new_dic.get(i,0)+1
for k,v in new_dic.items():
    print(k,"Occured",v,"times")