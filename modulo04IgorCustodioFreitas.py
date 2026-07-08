'''
Bloco de Comentarios

Módulo 04 - Estrutura de Dados - Listas 

'''


frutas_bonitas = ['maçã', 'banana', 'laranja', 'abacaxi', 'kiwi']

print('🍒' * 40)

print('Bem-vindo ao sistema de listas de frutas bonitas \n ')

print('🍒' * 40)

fruta_escolhida = input('Digite o nome da fruta que deseja colocar:')

frutas_bonitas.append(fruta_escolhida)

print('frutas[0]) # maçã')
print('frutas[1]) # kiwi')
print('frutas[2]) # abacaxi')
print('frutas[3]) # jambu')

print(f'\nFruta adicionada com sucesso! \nA nova lista de frutas bonitas é: {frutas_bonitas}')