
def subtract(s1,s2):
     if len(s2)>len(s1):
        s1,s2=s2,s1

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
                     s3=str(dummy)+s3
                     carry=0
                 else:
                     s3=str(10+dummy)+s3
                     carry= ((-1*dummy)//10)+1
             else:
                 dummy=int(s1[len(s1)-1-i])-int(s2[len(s2)-1-i])-carry
                 if dummy>=0:

                     s3=str(dummy)+s3
                     carry=0
                 else:
                     s3=str(10+dummy)+s3
                     carry= ((-1*dummy)//10)+1
     if carry!=0:
         return subtract(s2,s1)
     else:
         return s3

def add(s1,s2):
    s3=""
    carry=0
    if len(s2)>len(s1):
        s1,s2=s2,s1


    if len(s1)>=len(s2):
        for i in range(len(s1)):

        #print(s3)
        #print(carry)
            if i>=len(s2):
                s3= str((carry+int(s1[len(s1)-1-i]))%10)+s3
                carry=(carry+int(s1[len(s1)-1-i]))//10
            else:
                s3= str((carry+int(s1[len(s1)-1-i])+int(s2[len(s2)-1-i]))%10)+s3
                carry=(carry+int(s1[len(s1)-1-i])+int(s2[len(s2)-1-i]))//10
    return(str(carry)+s3)

s1=input()
s2=input()

print(subtract(s1,s2))
print(add(s1,s2))
