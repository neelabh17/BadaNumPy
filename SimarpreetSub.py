def reverse(s):
     if len(s) == 0:
         return s
     else:
         return reverse(s[1:]) + s[0]

def subtract(s1,s2):
     s3=""
     carry=0
     dummy=0
     if len(s1)>=len(s2):
         for i in range(len(s1)):

         #print(s3)
         #print(carry)
             if i>=len(s2):
                 dummy=int(s1[len(s1)-1-i])-carry
                 if dummy>=0:
                     s3+=str(dummy)
                     carry=0
                 else:
                     s3+=str(10+dummy)
                     carry= ((-1*dummy)//10)+1
             else:
                 dummy=int(s1[len(s1)-1-i])-int(s2[len(s2)-1-i])-carry
                 if dummy>=0:

                     s3+=str(dummy)
                     carry=0
                 else:
                     s3+=str(10+dummy)
                     carry= ((-1*dummy)//10)+1
     if carry!=0:
         return subtract(s2,s1)
     else:
         return s3


#https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/

s1=input()
s2=input()


print(reverse(subtract(s1,s2)))
