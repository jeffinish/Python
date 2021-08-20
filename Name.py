name = input('Digite o seu nome: ')
length_name = len(name)

if length_name < 3:
    print('Seu nome precisa ter pelo menos três letras')
elif length_name > 50:
    print('Seu nome pode ter no máximo 50 letras')
else:
    print('Seu nome é TOP!')
