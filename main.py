import random
 
def gameWin(comp,u):
   if comp==u:
       return None
   elif comp=='r':
       if u=='p':
        return True
       elif u=='s':
         return False
   elif comp=='p':
       if u=='s':
        return True
       elif u=='r':
         return False
   elif comp=='s':
       if u=='r':
        return True
       elif u=='p':
         return False
   
     


print("Comp turn:Rock(r),Paper(p) or Scissor(s)")
randNo= random.randint(1,3)
if randNo==1:
  comp='r'
elif randNo==2:
      comp='p'
elif randNo==3:
     comp='s'       
 
u=input("your turn:Rock(r),Paper(p) or Scissor(s)")

a=gameWin(comp,u)                    
if a==None:
    print("The game is a tie")
elif a==True:
    print("you win")    
elif a==False:
   print("Computer wins")   
print("you chose "+u)
print("Computer chose "+ comp)
