import ply.lex as lex

# Aporte Aaron Franco

# Inicio de palabras reservadas
reserved = {
# Tipado
"var":"VAR",
"String":"STRING",
"int":"INT",
"bool":"BOOL",
#Aport Pedro Bajaña
'True':'TRUE',
'print':'PRINT',
'False':'FALSE',
'bool':'BOOL',
'void':'VOID',
# Estructuras de Control
"if":"IF",
"else":"ELSE",
"for":"FOR",


}

# Definicion de Tokens

tokens = [

"VARIABLE",'LPARENT','RPARENT','LLAVEL','LLAVER','IGUAL'





]+list(reserved.values())
t_LPARENT=r'\('
t_RPARENT=r'\)'
t_LLAVEL=r'\{'
t_LLAVER=r'\}'
t_ignore = ' \t'
t_IGUAL=r'='

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