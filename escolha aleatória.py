from random import choice, sample
pri = input('Primeiro aluno: ')
seg = input('Segundo aluno: ')
ter = input('Terceiro aluno: ')
qua = input('Quarto aluno: ')
alunos = [pri, seg, ter, qua]
print('O aluno escolhido será: {}.\nE a ordem de apesentação será {}.'.format(choice(alunos), sample(alunos, k = len(alunos))))
