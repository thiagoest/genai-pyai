# Exercícios da Aula Python para IA
# Curso de Especialização em IA Generativa

#exercício 1: Calculadora de IMC
# Programa que calcula o Índice de Massa Corpórea (IMC)

def calcular_imc():
	"""Pergunta peso e altura do usuário e calcula o IMC.

	O IMC é definido como peso/(altura*altura). O resultado é exibido
	na tela com duas casas decimais.
	"""

	try:
		peso = float(input("Digite o seu peso em kg: "))
		altura = float(input("Digite a sua altura em metros: "))
	except ValueError:
		print("Valor inválido. Use números com ponto decimal, por exemplo 1.75")
		return

	if altura <= 0:
		print("Altura deve ser maior que zero!")
		return

	imc = peso / (altura * altura)
	print(f"Seu IMC é: {imc:.2f}")


if __name__ == "__main__":
	calcular_imc()
