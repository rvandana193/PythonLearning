name = 'Sam'
if name == 'John':
    print("Hi John!")
elif name == 'Sam':
    print("Hi Sam!")
else:
    print("What is your name?")


mylist = [1,2,3,4,5,6]
for num in mylist:
    if num%2 == 0:
        print(num)
    else:
        print(f'Odd Number : {num}')


tup = (1,2,3)
for item in tup:
    print(item)


mylist = [(1,2),(3,4),(5,6)]
for item in mylist:
    print(item)
for a,b in mylist:
    print(a)
    print(b)


d={'k1':1,'k2':2,'k3':3}
for item in d.items():
    print(item)
for key,value in d.items():
    print(value)