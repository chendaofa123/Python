names=['Tom','Jine','Collins','Red']
print(names[1]+' can not keep the appointment')
names[1]='Grous'
print('\nI found a bigger table')
names.insert(0,'Blue')
names.insert(2,'Elizabeth')
names.append('Trump')
print('\nI can only invited two guests to dinner')
i=0
while i<5:
  print('\n'+names.pop(0)+', I am sorry, I can not invite you to dinner')
  i+=1
for name in names:
    print('\n'+name+' You are still invited')
del names[0]
del names[0]
print[names]
