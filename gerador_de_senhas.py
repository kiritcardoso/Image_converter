import string
import random

# Mensagem para o usuário
opcao = input('Você gostaria de receber uma senha de:\n1. Letras\n2. Números\n3. Misto\nEscolha o número correspondente: ')

# Lógica para definir o conjunto de caracteres com base na escolha
if opcao == '1':  # Letras
    caracteres = string.ascii_letters
elif opcao == '2':  # Números
    caracteres = string.digits
elif opcao == '3':  # Misto (letras e números)
    caracteres = string.ascii_letters + string.digits
else:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
    exit()

# Geração da senha
tamanho = int(input("Qual o tamanho da senha? "))
senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

print(f"Sua senha gerada é: {senha}")
