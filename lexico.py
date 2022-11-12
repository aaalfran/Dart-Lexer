import ply.lex as lex

# Inicio de palabras reservadas

reserved = {
# Inicio Aporte Aaron Franco
"var":"VAR",
"String":"STRING",
"int":"INT",
"if":"IF",
"else":"ELSE",
"for":"FOR",
#Fin Aporte Aaron Franco

#Aport Pedro Bajana
'True':'TRUE',
'print':'PRINT',
'False':'FALSE',
'bool':'BOOL',
'void':'VOID',
'stdin':'STDIN'
#Fin Aporte Pedro Bajana
}



# Definicion de Tokens
tokens = [
#Inicio Aporte Aaron Franco
'VARIABLE',

#Fin Aporte Aaron Franco
#Inicio Aporte Pedro Bajana
'LPARENT',
'RPARENT',
'LLAVEL',
'LLAVER',
'IGUAL',
'DIVISION',
'MAS'
#Fin Aporte Pedro Bajana
]+list(reserved.values())
#Inicip Aporte Aaron Franco
t_ignore = ' \t'

#Fin aporte Aaron Franco
#Inicio Aporte Pedro Bajana
t_LPARENT=r'\('
t_RPARENT=r'\)'
t_LLAVEL=r'\{'
t_LLAVER=r'\}'
t_IGUAL=r'='
t_MAS=r'\+'
t_DIVISION = r'/'
#Fin Aporte Pedro Bajana

#Inicio Aporte Aaron Franco
# Definiendo token de palabras reservadas
def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VARIABLE')  # Busca por palabras reservadas
    return t
# Definiendo token de error
def t_error(t):
    print("No se ha reconocido '%s'"%t.value[0])
    t.lexer.skip(1)
#Fin Aporte Aaron Franco



#Inicio Aporte Aaron Franco
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
#Fin Aporte Aaron Franco