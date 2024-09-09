# Sequência a
def proximo_a():
    sequencia_a = [1, 3, 5, 7]
    proximo = sequencia_a[-1] + 2
    return proximo

# Sequência b
def proximo_b():
    sequencia_b = [2, 4, 8, 16, 32, 64]
    proximo = sequencia_b[-1] * 2
    return proximo

# Sequência c
def proximo_c():
    sequencia_c = [0, 1, 4, 9, 16, 25, 36]
    proximo = (len(sequencia_c)) ** 2
    return proximo

# Sequência d
def proximo_d():
    sequencia_d = [4, 16, 36, 64]
    proximo = (len(sequencia_d) * 2 + 2) ** 2
    return proximo

# Sequência e
def proximo_e():
    sequencia_e = [1, 1, 2, 3, 5, 8]
    proximo = sequencia_e[-1] + sequencia_e[-2]
    return proximo

# Sequência f
def proximo_f():
    sequencia_f = [2, 10, 12, 16, 17, 18, 19]
    proximo = 20  # conforme a lógica de números consecutivos
    return proximo

# Executando as funções
print(f"Próximo número da sequência a: {proximo_a()}")
print(f"Próximo número da sequência b: {proximo_b()}")
print(f"Próximo número da sequência c: {proximo_c()}")
print(f"Próximo número da sequência d: {proximo_d()}")
print(f"Próximo número da sequência e: {proximo_e()}")
print(f"Próximo número da sequência f: {proximo_f()}")
