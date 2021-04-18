obj = input('Digite algo: ')
print(f'As informaçoes sobre oq você digitou ({obj}): \n'
      f'A classe: {type(obj)}\n'
      f'Alfanúmerico: {obj.isalnum()}\n'
      f'Númerico: {obj.isnumeric()}\n'
      f'Alfabetico: {obj.isalpha()}\n'
      f'Está tudo em maiusculo: {obj.isupper()}\n'
      f'Está tudo em minusculas: {obj.islower()}\n'
      f'É um número decimal: {obj.isdecimal()}\n'
      f'É composto apenas de espaços: {obj.isspace()}\n'
      f'Tem apenas a primeira letra maiuscula sem espaços: {obj.istitle()}')
