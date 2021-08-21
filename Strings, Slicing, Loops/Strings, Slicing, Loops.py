# trabalhando com strings

a = 'Estudando Python'

print(a)

# acessando a parte de uma string (substring)
print(a[0])

# slicing - cortando as coisas com Python

print(a[10:])

# acessando os itens de forma inversa

print(a[-3:-1])

# inversão de caracteres

print(a[:9:-1])

# Como iterar sobre elementos?
palavra = 'odontologia'

for caractere in palavra:
    if 'o' == caractere:
        print('Olá, eu sou o caractere "o"')
        
        
# verifique quais vogais estão contidas na palavra 'odontologia'
vogais = 'aeiou'
for vogal in vogais:
    if vogal in palavra:
        # print('A vogal',vogal,'está na palavra', palavra)
        print(f'A vogal { vogal } está na palavra {palavra}')