import ply.lex as lex

# Aporte Aaron Franco

# Inicio de palabras reservadas
reserved = {
# Tipado
"var":"VAR",
"String":"STRING",
"int":"INT",
"bool":"BOOL",
# Estructuras de Control
"if":"IF",
"else":"ELSE",
"while": "WHILE",
"for":"FOR",

}

# Definicion de Tokens

tokens = [

"VARIABLE",





]+list(reserved.values())

t_ignore = ' \t'

# Definiendo token de palabras reservadas
def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VARIABLE')  # Busca por palabras reservadas
    return t
# Definiendo token de error
def t_error(t):
    print("No se ha reconocido '%s'"%t.value[0])
    t.lexer.skip(1)


#Creando Lexer
lexer = lex.lex()
def analizador(data):
  lexer.input(data)
  while True:
    tok = lexer.token()
    if not tok:
      break
    print(tok)
while(True):
    cadena = input(">>: ")
    analizador(cadena)