import ply.lex as lex
code =''
# Inicio de palabras reservadas

reserved = {
# Inicio Aporte Aaron Franco
"var":"VAR",
"String":"STRING",
"int":"INT",
"if":"IF",
"else":"ELSE",
"for":"FOR",
"main":"MAIN",
"double":'DOUBLE',

#Fin Aporte Aaron Franco

#Aporte Pedro Bajana
'true':'TRUE',
'print':'PRINT',
'false':'FALSE',
'bool':'BOOL',
'void':'VOID',
'stdin':'STDIN',
'in':'IN',
'as':'AS',
'break':'BREAK',
'continue':'CONTINUE',
'join':'JOIN',
'while':'WHILE',

#Fin Aporte Pedro Bajana

#Aporte Fabrizzio Ontaneda
'return':'RETURN',
'List':'LIST',
'toString':'TOSTRING',
'toInt':'TOINT',
'toDouble':'TODOUBLE',
'write':'WRITE',
'readLineSync':'READLINESYNC',
'parse':'PARSE',
'final':'FINAL',
'const':'CONST',
'stdout':'STDOUT',
'in':'IN',
'map':'MAP',
'set':'SET'
#Fin Aporte Fabrizzio Ontaneda
}

metodos_estructuras = {
    "List": ['join', 'indexOf', 'add', 'length'],
    "Set": ['contains', 'difference', 'union'],
    "Map": ['remove', 'clear', 'containsKey']
}

contador = 0

metodos = {}

for list_func in metodos_estructuras.values():
    for func in list_func:
        metodos[func] = func.upper()
# Definicion de Tokens
tokens = [
#Inicio Aporte Aaron Franco
'FUNCION',
'VARIABLE',
'RESTA',
'MULTIPL',
'CADENA',
'INTEGER',
'FLOAT',
'INCREMENTADOR',
#Fin Aporte Aaron Franco
#Inicio Aporte Pedro Bajana
'LPARENT',
'RPARENT',
'LLAVEL',
'LLAVER',
'IGUAL',
'DIVISION',
'MAS',
'PUNTOCOMA',
'PUNTO',
'DOSPUNTOS',
#Fin Aporte Pedro Bajana
#Inicio Aporte Fabrizzio Ontaneda
'NEGACION',
'AND',
'OR',
'ES_IGUAL',
'NO_IGUAL',
'MENOR_QUE',
'MAYOR_QUE',
'MENOR_O_IGUAL',
'MAYOR_O_IGUAL',
'SALTO_LINEA',
'TABULACION',
'CORCH_IZQ',
'CORCH_DER',
'COMA',
"AUTOINCREMENTO", "AUTODECREMENTO"


#Fin APorte Fabrizzio Ontaneda
]+list(reserved.values())
#Inicio Aporte Aaron Franco
t_ignore = ' \t'
t_RESTA =  r'\-'
t_MULTIPL = r'\*'
t_INCREMENTADOR = r'[a-zA-Z]\+{2}'
#Fin aporte Aaron Franco

#Inicio Aporte Pedro Bajana
t_LPARENT=r'\('
t_RPARENT=r'\)'
t_LLAVEL=r'\{'
t_LLAVER=r'\}'
t_IGUAL=r'='
t_MAS=r'\+'
t_DIVISION = r'/'
t_PUNTOCOMA=r';'
t_PUNTO=r'\.'
t_INTEGER = r'([1-9]\d+|\d)'
t_DOSPUNTOS=r':'
t_AUTOINCREMENTO = r'\+\+'
t_AUTODECREMENTO = r'\-\-'
#Fin Aporte Pedro Bajana

#Inicio Aporte Fabrizzio Ontaneda
t_ES_IGUAL=r'=='
t_NO_IGUAL=r'!='
t_MENOR_QUE=r'<'
t_MAYOR_QUE=r'>'
t_MENOR_O_IGUAL=r'<='
t_MAYOR_O_IGUAL=r'>='
t_AND = r'&&'
t_OR = r'\|\|'
t_SALTO_LINEA=r'/n'
t_NEGACION=r'!'
t_TABULACION=r'/t'
t_CORCH_IZQ= r'\['
t_CORCH_DER= r'\]'
t_COMA=r','


#Fin Aporte Fabrizzio Ontaneda

#Inicio Aporte Aaron Franco
#Definiendo tocken flotante
def t_FLOAT(t):
    r'-?\d+\.\d{1,15}'
    return t

#Definiendo token de cadenas
def t_CADENA(t):
    r'\"[a-zA-Z0-9\!\s]*\"'
    return t
# Definiendo token de palabras reservadas
def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VARIABLE')  # Busca por palabras reservadas
    return t
# Definiendo token de error
def t_error(t):
    print("No se ha reconocido '%s'"%t.value[0])
    t.lexer.skip(1)
# Definiendo token de comentarios
def t_COMMENT(t):
    r'(\/\/.*)'
    pass
#Fin Aporte Aaron Franco

#inicio Aporte Pedro bajaña

#Definiendo token de linea
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno +=len(t.value)



#Inicio Aporte Aaron Franco
#Creando Lexer
lexer = lex.lex()
def analizadorLexico(cadena):
    tokensListR=[]
    # analizador = lex.lex()
    lexer.input(cadena)
    while True:
        tokenR=lexer.token()
        if tokenR!=None:
            tokensListR.append(tokenR)
        else:
            break
    return tokensListR

#Descomentar para usar analizador en tiempo real por consola
'''   
while(True):
    cadena = input(">>: ")
    analizador(cadena)
'''
# Lee el archivo input.txt y el lexer obtendra los tokens respectivos
'''
archivo = open("input.txt","r")
for linea in archivo:
  print(">>" + linea)
  analizador(linea)
  if len(linea) == 0:
    break
'''
#Fin Aporte Aaron Franco