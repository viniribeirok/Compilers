Relatório de Laboratório 1: Analisador Léxico

Identificação

Instituição: PUC-SP

Curso: Ciência da Computação

Disciplina: Compiladores

Equipe: João Vitor Bittencourt e Vinicius Pereira Ribeiro

Objetivo Principal
O foco deste laboratório foi entender na prática o coração de um analisador léxico (scanner). Exploramos como ele utiliza expressões regulares e autômatos finitos para reconhecer padrões, transformar textos e interpretar códigos.

Resumo das Atividades
1. Simulando um Scanner em Bash
Criamos um script simples em Bash para simular um scanner, observando passo a passo como um código-fonte é percorrido e fatiado em pedaços menores, chamados de tokens.

2. Dominando Expressões Regulares (Regex)
Com o apoio de ferramentas visuais como regexr e regex101, construímos expressões para capturar elementos essenciais da programação:

Identificadores

Números inteiros

Operadores

Espaços em branco

Essa etapa deixou claro como os tokens nascem a partir de padrões bem definidos.

3. Limpeza de Dados com Regex (Find/Replace)
Levamos as expressões regulares para o mundo real. Aplicamos a técnica em arquivos para fazer substituições em massa e limpeza de dados, incluindo a organização de arquivos CSV e a remoção de formatações e trechos indesejados no texto.

4. Construindo um Scanner em Python
Subimos o nível implementando um scanner real na linguagem Python. Utilizando a biblioteca nativa re, o código foi capaz de varrer uma string e identificar seus tokens com precisão.

5. Modelagem com Autômatos Finitos (JFLAP)
Desenhamos a lógica por trás das expressões regulares criando Autômatos Finitos Determinísticos (DFA) e Não Determinísticos (NFA). Modelamos o reconhecimento de números, identificadores e operadores, e realizamos também o processo prático de conversão de um NFA para um DFA.

6. Compiladores vs. Inteligência Artificial
Fizemos um estudo comparativo interessante entre os tokens tradicionais e os tokens de IA (usando o Tokenizer da OpenAI):

Compiladores: Seguem regras rígidas da linguagem (exemplo: a palavra "position" é lida como um único token).

IA (OpenAI): Utiliza o método BPE (Byte Pair Encoding), que quebra a palavra "position" em pedaços menores por uma questão de eficiência estatística.

7. Processamento de Linguagem Natural (Texto Literário)
Desenvolvemos um scanner em Python voltado para a nossa língua. Ele recebeu como entrada um arquivo .txt contendo um livro em português e, usando regex, processou todo o texto para entregar uma lista estruturada de tokens, separando as palavras dos símbolos de pontuação.

Atividade Extra: A IA como Analisador Léxico
Desafiamos uma Inteligência Artificial a escrever um scanner que classificasse tipos gramaticais de palavras (como verbos, artigos, etc.). O resultado foi um código funcional, mas que demonstrou limitações práticas na execução da tarefa.

Discussão e Aprendizados
Um dos grandes insights do laboratório foi perceber os limites da ferramenta. Não é possível mapear completamente a língua portuguesa usando apenas expressões regulares. Idiomas naturais possuem estruturas complexas e ambiguidades que bloqueiam esse tipo de abordagem, exigindo gramáticas mais avançadas (como as gramáticas livres de contexto) para serem processadas corretamente.

Conclusão
O analisador léxico é a porta de entrada de qualquer compilador. Sua missão de varrer o código e transformá-lo em uma sequência estruturada de tokens é a base indispensável para que a máquina consiga, nas etapas seguintes, entender a estrutura gramatical e compilar o programa com sucesso.
