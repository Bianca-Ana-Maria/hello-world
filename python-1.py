#1
x = 7                                                          Output:
y = 8
z = 0
result1 = x == y
result2 = y > x
result3 = z < x + 2
result4= result1 and result2                                     
print(result4)                                                    = False
print(not (True and False or True))                               = False

#2
x = input('Name: ')
if x == 'Bianca':
    print('You are great!')
elif x == 'Dragos':
    print('You are big')
elif x == 'Andrei':
    print('You are small')
else:
    print('You are ok')


#3
x = [4, True, 'hi']
y = 'hello'
print(len(x), len(y))                                             = 3, 5
x.append('hello')       
print(x)                                                          = [4, True, 'hi' , 'hello']
print(x.pop(0))                                                  
print(x)                                                          = [True, 'hi' , 'hello']
x[2] = 'car'
print(x)                                                          = [True, 'hi' , 'car']

#4
for i in range(10, -1, -1):                                       = 10  9  8  7  6  5  4  3  2  1  0
    print(i)

x = [3,6,8,45,32,5]
for i, element in enumerate(x):
    print(i, element)                                             = 0 3        1 6       2 8      3 45      4 32      5 5
                                                             



