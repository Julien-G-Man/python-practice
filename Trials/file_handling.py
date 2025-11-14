file = open('Trials/companies.txt', 'r+')
data  = file.read()
print(data)
data = file.write('Nvidia ')
print(data)


file.close()