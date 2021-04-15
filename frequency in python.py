str= "Raj Singh"
re= {}
for i in str:
  if i in re:
     re[i] += 1
else:
     re[i] = 1
print("Count of all characters in str is :\n", str(re))
