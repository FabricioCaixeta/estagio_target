def verificar_letra_a(texto):
    # Converte o texto para minúsculas para facilitar a contagem
    texto_minusculo = texto.lower()

    # Conta a ocorrência da letra 'a'
    quantidade_a = texto_minusculo.count('a')

    # Verifica se a letra 'a' está presente e imprime o resultado
    if quantidade_a > 0:
        print(f"A letra 'a' ocorre {quantidade_a} vez(es) na string.")
    else:
        print("A letra 'a' não foi encontrada na string.")

# Entrada do usuário
texto_informado = input("Digite uma string: ")

# Chamada da função
verificar_letra_a(texto_informado)
