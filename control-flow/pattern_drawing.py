prompt = int(input("Enter the size of the pattern: "))
line = 1

while line < prompt:
   
   line +=1
   for i in range(1,prompt + 1):
        print("*", end="")

        for i in range(1, line -1):
            print("*", end="") 
        
print()     
     