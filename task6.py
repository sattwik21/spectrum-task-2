def add(a,b):
  return(a+b)
def sub(a,b):
  return(a-b)
def mul(a,b):
  return(a*b)
def div(a,b):
  return(a/b)

print("1.Add, 2.Subtract,3.Multiply, 4.Division")
while(True):
 choice = input(" Enter Choice:1/2/3/4:")
 if choice in ('1','2','3','4'):
    c= float(input("First no <=4:"))
    d= float(input("Second no <=4:"))
    if choice == '1':
      print(c,"+",d,"=",add(c,d))
    elif choice == '2':
      print(c,"-",d,"=",sub(c,d))
    elif choice == '3':
      print(c,"*",d,"=",mul(c,d))
    elif choice == '4':
      print(c,"/",d,"=",div(c,d))
    break
 else:
     print("INVALID")
