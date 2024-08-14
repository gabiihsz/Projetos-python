# Função para contar os caracteres em uma frase
def contar_caracteres(frase):
    contagem = {}
    for caractere in frase:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1
    return contagem


# Função para encontrar o maior e menor valor em um dicionário
def maior_menor_valor(dicionario):
    if not dicionario:
        return None, None

    maior = max(dicionario.values())
    menor = min(dicionario.values())
    return maior, menor


# Programa principal
frase = input("Digite uma frase: ")
resultado = contar_caracteres(frase)
print("Contagem de caracteres:", resultado)

maior_valor, menor_valor = maior_menor_valor(resultado)
print(f"Maior valor: {maior_valor}, Menor valor: {menor_valor}")