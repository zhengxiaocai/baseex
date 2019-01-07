# break continue

classmates = ['Tom','Jerry','Curry','Jordan','Jack']
for guy in classmates:
    if guy == 'Jordan':
        break
    print(guy + ' ',end='')


classmates = ['Tom','Jerry','Curry','Jordan','Jack']
for guy in classmates:
    if guy == 'Jordan':
        continue
    print(guy + ' ',end='')
