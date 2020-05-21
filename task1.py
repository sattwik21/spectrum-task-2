def fun1(a,b):
  def fun2():
    s = a+b
    return s
  c = fun2()
  return c + 5
a = int(input("enter value of a:"))
b = int(input("enter value of b:"))
result = fun1(a,b)
print(result)
