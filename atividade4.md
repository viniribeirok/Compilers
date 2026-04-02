# Atividade 4

import re

codigo = "position = initial + rate * 60"

# 1. Compilamos a Regex antecipadamente
regex_compilada = re.compile(r'[a-zA-Z_][a-zA-Z0-9_]*|\d+|[=+\-*]')

tokens = []

# 2. O finditer nos dá um "iterador" que processa um token por vez
for match in regex_compilada.finditer(codigo):
    # match.group() extrai exatamente a string que casou com a regra
    tokens.append(match.group())

print(tokens)