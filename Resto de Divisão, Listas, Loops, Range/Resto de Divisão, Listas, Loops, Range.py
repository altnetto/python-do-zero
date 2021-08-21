# Resto da divisão e Loops com listas

# O que é um resto de divisão?

print(7 % 5)

# Dada a lista [1,2,3,4,5,6,7,8,9,10], verifica quais desses números é divisível por 2

for i in [1,2,3,4,5,6,7,8,9,10]:
    if i % 2 == 0:
        print(f'O número {i} é divisível por 2.')
        
for i in range(1,11):
    if i % 2 == 0:
        print(f'O número {i} é divisível por 2.')
        
A = [1,2,3,4,5,6,7,8,9,10]

for i in range(0, len(A)+1):
    if i % 2 == 0:
        print(f'O número {i} é divisível por 2.')
        
# Demonstre quais números na seguinte lista são divisíveis por 2, 3 e/ou 5

# range(15)

for i in range(15):
    if i % 2 == 0:
        print(f'O número {i} é divisível por 2.')
    if i % 3 == 0:
        print(f'O número {i} é divisível por 3.')
    if i % 5 == 0:
        print(f'O número {i} é divisível por 5.')
    