alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encypt(texts,shifts,Direction):
    if(Direction == "Palm"):
           shifts *= -1
    Chars = ""
    for letter in texts:
       
       if letter in alphabet : 
           position = alphabet.index(letter)
           newpos = position + shifts
           Chars += alphabet[newpos]
       else :
            Chars+= letter

       
    print(Chars)
    pass

while(True):

    Test = input("Enter Number : ")
    text = "mj@qqt"


    shift = int(input("Type the shift number:\n"))

    encypt(text,shift,Test)

    Check = input("Type 'Yes' if ypu want  to go again").lower()
    
    if(Check ==  "no"): 
       
        break

print("End of Program")
