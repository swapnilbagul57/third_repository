n = int(input("Enter any number :-  "))

for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

'''OUTPUT   
Enter any number :-  5
* 
* * 
* * * 
* * * * 
* * * * * 

'''
print("\n")
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        print("x", end=" ")
    for j in range(i+1):
        print("x", end=" ")
    print()
