import re

def classificar(token):
    if re.match(r'[.,!?;]', token):
        return "pontuacao"
    elif token.lower() in ["o", "a", "os", "as", "um", "uma"]:
        return "artigo"
    elif token.lower() in ["eu", "tu", "ele", "ela"]:
        return "pronome"
    elif token.isdigit():
        return "numero"
    elif re.match(r'\w+', token):
        return "palavra"
    else:
        return "??"

def tokenize(texto):
    tokens = re.findall(r'\w+|[.,!?;]', texto)
    return [(t, classificar(t)) for t in tokens]

with open("livro.txt", "r", encoding="utf-8") as f:
    texto = f.read()

resultado = tokenize(texto)

print(resultado)

with open("output_extra.txt", "w", encoding="utf-8") as f:
    f.write(str(resultado))
