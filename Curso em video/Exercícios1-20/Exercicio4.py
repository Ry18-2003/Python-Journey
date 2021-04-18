obj = input('Escreva algo: ')

print(f'A classe primitiva do que você escreveu é: {type(obj)}\n'
    f'Se ele é alfanúmerico: {obj.isalnum()}\n'
    f'Se é apenas alfabetico {obj.isalpha()} \n'
    f'Se é apenas númerico: {obj.isnumeric()}\n'
    f'Se tem apenas espaços: {obj.isspace()}\n'
    f'Se está apenas em letras maiusculas: {obj.isupper()}\n'
    f'Se está em apenas letras minusculas:{obj.islower()}\n'
    f'Se está capitalizado: {obj.istitle()}')
