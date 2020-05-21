s = input("Enter a string:")
words = s.split()
l = []
u = []
for char in s:
 if char.islower():
  l.append(char)
 else:
  u.append(char)
new_string = ''.join(l + u)
print("\n arranging characters giving precedence to lowercase:")
print(new_string)
