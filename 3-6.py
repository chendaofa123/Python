names=['Tom','Jine','Collins','Red']
print(names[1]+' can not keep the appointment')
names[1]='Grous'
print('\nI found a bigger table')
names.insert(0,'Blue')
names.insert(2,'Elizabeth')
names.append('Trump')
for name in names:
    print('\n'+name+',I hope to have dinner with you ')
