nota1 = int(input('Digite a nota1: '))
nota2 = int(input('Digite a nota 2: '))
nota3 = int(input('Digite a nota 3: '))
nota4 = int(input('Digite a nota 4: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media <= 4:
    print('Aluno reprovado:', media)
elif media < 7:
    print('Aluno de recuperação:', media)
else:
    print('Aluno aprovado:', media)