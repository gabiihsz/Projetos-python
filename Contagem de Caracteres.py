# Função para contar os caracteres em uma frase
def contar_caracteres(frase):
    contagem = {}  # Dicionário para armazenar a contagem de caracteres
    for caractere in frase:  # Itera sobre cada caractere na frase
        if caractere in contagem:  # Se o caractere já está no dicionário
            contagem[caractere] += 1  # Incrementa a contagem
        else:
            contagem[caractere] = 1  # Caso contrário, inicia a contagem em 1
    return contagem  # Retorna o dicionário com a contagem

# Exemplo de uso
frase = input("Digite uma frase: ")  # Lê uma frase do usuário
resultado = contar_caracteres(frase)  # Chama a função para contar caracteres
print(resultado)  # Exifbe o dicionário resultante