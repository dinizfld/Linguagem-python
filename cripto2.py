def encrypt(text, shift):
    result = ""
    # percorre cada letra no texto
    for i in range(len(text)):
        char = text[i]
        # verifica se a letra é uma letra do alfabeto
        if char.isalpha():
            # encontra o novo valor da letra com base no deslocamento
            new_char_code = ord(char) + shift
            # verifica se a nova letra é maiúscula ou minúscula
            if char.isupper():
                new_char = chr((new_char_code - 65) % 26 + 65)
            else:
                new_char = chr((new_char_code - 97) % 26 + 97)
        else:
            # mantém caracteres não-alfabéticos iguais
            new_char = char
        result += new_char
    return result

def decrypt(text, shift):
    # inverte o deslocamento para decifrar o texto
    return encrypt(text, -shift)
