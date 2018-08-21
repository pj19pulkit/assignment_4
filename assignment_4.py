#Q1  Reverse the whole list using list methods.

print("<--solution 1-->")

list=[1,2,3,4,5]
list.reverse()
print(list)

#Q2   Print all the uppercase letters from a string.

print("<--solution 2-->")

string= "PULKIT JOHAR"
for ch in string :
    if ch.isupper():
        print(ch)


#question 3 Split the user input on comma's and store the values in a list as integers.

print("<--solution 3-->")

i=input("enter the input ")
list=[]
list1=i.split(',')
for n in list1:
    list.append(int(n))
print(list)



#Q4 Check whether a string is palindromic or not.

print("<--solution 4-->")


n=int(input("Enter number:")) 
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!",rev) 
else:
    print("The number isn't a palindrome!",rev)



#Q5  Make a deepcopy of a list and write the difference between shallow copy and deep copy.

print("<--solution 5-->")


import copy as c
list1 = [1, 2, [3,5], 4]
list2 = c.deepcopy(list1)
print ("Before deep copying")
print("list1 = ",list1)
print("list2 = ",list2)
list2[2][1] = 125
print ("After deep copying in list2")
print(list2)
print ("After deep copying in list1")
print(list1)
print('\r')
