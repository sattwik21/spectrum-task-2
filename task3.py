def split(A):
  list1=[]
  list2=[]
  for i in A:
   if(i%2==0):
     list2.append(i)
   else:
     list1.append(i)
  print("List1:",list1)
  print("List2:",list2)

A=list()
n=int(input("Enter size of list:"))
print("Enter integers:")
for i in range(int(n)):
 k=int(input(" "))
 A.append(k)
split(A)
