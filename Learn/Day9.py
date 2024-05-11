import os
def Clear():
    os.system('cls')
Dictionary = {1:80 , 2:60 , 3:50}
Dictionary1 = {4:80 , 5:60 , 6:[10,203]}
List = []
List.append(Dictionary)
List.append(Dictionary1)
       



print(List[1][6][1])
num = int(input("Enter number for cleart Console : "))

if num == 1: Clear()

print("Now clear Console")
print(List[1][6][1])