def sequencia_fibonacci(limit):
    sequence = [0, 1]
    while sequence[-1] < limit:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence

def esta_na_sequencia(number):
    sequence = sequencia_fibonacci(number)
    if number in sequence:
        return f"O número {number} pertence à sequência de Fibonacci."
    else:
        return f"O número {number} NÃO pertence à sequência de Fibonacci."


# Entrada do usuário
numero_informado = int(input("Informe um número: "))
resultado = esta_na_sequencia(numero_informado)
print(resultado)
