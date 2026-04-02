import re

def tokenizar(texto):
    padrao = r'\w+|[^\w\s]'
    tokens = re.findall(padrao, texto, re.UNICODE)
    return tokens

with open("livro.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

tokens = tokenizar(conteudo)

print(tokens)