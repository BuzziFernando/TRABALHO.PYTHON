# ALUNO: FERNANDO BUZZI

import random

memoria = [' '] * 100
opcao = 0
tamanho = 0
letra = ''
for i in range(100):
	if (random.randint(0, 11) >= 5):
		memoria[i] = 'x'
	else:
		memoria[i] = ' '
print(memoria[:20])
print(memoria[20:40])
print(memoria[40:60])
print(memoria[60:80])
print(memoria[80:])

while (opcao != 4):
	#Menu do programa
	print("1 - Primeira Escolha")
	print("2 - Melhor Escolha")
	print("3 - Pior Escolha")
	print("4 - Sair")
	print("Escolha o algoritmo pelo numero")
	opcao = int(input())
	print("Digite o tamanho da informacao")
	tamanho = int(input())
	print("Digite a letra a ser utilizada")
	letra = input()
	cont = 0
	a = 0
	aux = True
	melhor = 0
	melhorlivre = 101
	maiorlivre = 0
	maior = 0
	if (opcao == 1):
		#passa por todos os itens da memoria
		for a in range(len(memoria)):
			#procura as casas vazias, quando não encontra o contador é zerado
			if memoria[a] != ' ':
				cont = 0
			#quando encontra, o contador soma um
			elif memoria[a] == ' ':
				cont = cont + 1
				#quando o contador tiver o mesmo valor do tamanho, é escrito a letra desejada
				if cont == tamanho:
					#aux recebe falso para não mostrar a informação
					aux = False
					#adiciona a letra a partir da última casa e diminui, irá diminuir o número de vezes do "tamanho"
					for c in range(tamanho):
						memoria[a] = letra
						a = a - 1
					break
		#caso não haja espaço, entrará nesta condição
		if aux:
			print("Não há espaço para armazenar tal informação")
		pass
	else:
		if (opcao == 2):
			#passa por todos os itens da memória
			for b in range(len(memoria)):
				#espaços diferentes de vazio zeram o contador
				if memoria[b] != ' ':
					cont = 0
				#espaços vazios adicionam um ao contador
				elif memoria[b] == ' ':
					cont = cont + 1
					#quando o contador tiver o espaço exatamente necessário já é alocado
					if cont == tamanho and ( b == 99 or memoria[b+1] != ' '  ):
						#adiciona a letra a partir da última casa e diminui, irá diminuir o número de vezes do "tamanho"
						for d in range(tamanho):
							memoria[b] = letra
							b = b - 1
							aux = False
						break
						#caso nao encontre no tamanho exato, irá procurar a alocação que reste menos valores
					elif cont > tamanho and ( b == 99 or memoria[b+1] != ' '  ):
						#lógica do menor para guardar onde está a melhor alocação
						if cont < melhorlivre:
							melhorlivre = cont
							melhor = b
							aux = False
				#quando passar por todas os espaços entra na condição
				if b == 99 and not aux:
					#adiciona a letra a partir da última casa e diminui, irá diminuir o número de vezes do "tamanho"
					for d in range(tamanho):
						memoria[melhor] = letra
						melhor = melhor - 1
						aux = False
			#caso não houver espaço, entrará nesta condição
			if aux:
				print("Não há espaço para armazenar esta informação")
			pass
		else:
			if (opcao == 3):
				#passa por todos os espaços da memória
				for y in range(len(memoria)):
					#caso encontre valores diferentes de vazio, zera o contador
					if memoria[y] != ' ':
						cont = 0
					#se encontra espaços vazios, soma um no contador
					elif memoria[y] == ' ':
						cont = cont + 1
						#quando o contador for maior que ou igual ao tamanho entra na condição
						if cont >= tamanho and ( y == 99 or memoria[y+1] != ' '  ):
							#lógica do maior para guardar onde está e quantos espaços livres têm
							if cont > maiorlivre:
								maiorlivre = cont
								maior = y
								aux = False
					#entrará nessa condição quando passar por todos os valores e encotrar espaço para armazenar
					if y == 99 and not aux:
						#adiciona a letra a partir da última casa e diminui, irá diminuir o número de vezes do "tamanho"
						for d in range(tamanho):
							memoria[maior] = letra
							maior = maior - 1
							aux = False
				#irá entrar nessa condição caso não haja espao vazio
				if aux:
					print("Não há espaço para armazenar esta informação")
				pass
	# Aqui você deve imprimir todo o conteúdo da variável memória
	print(memoria[:20])
	print(memoria[20:40])
	print(memoria[40:60])
	print(memoria[60:80])
	print(memoria[80:])