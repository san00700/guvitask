a = []
n = int(input("\n Enter the Range : "))
i = 0
First = 0
Second = 1 
while(i < n):
  if(i <= 1):
     temp = i
  else:
     temp = First + Second
     First = Second
     Second = temp
print( temp )
a.append(temp)
print(a)
i = i + 1
  
  
