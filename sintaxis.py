import ply.yacc as sintactico
from lexico import tokens

# Inicio Aporte Aaron Franco
def p_sentencias(p):
    '''sentencias : asignacion
                  | comparacion
                  | operacion
                  | impresion
                  | funcion
                  | estructuras
                  | for
                  | if
                  | if-else
                  | write
                   '''
#Fin Aporte Aaron Franco
#Inicio Aporte Pedro Bajana
def p_asignacion(p):
  '''asignacion : declaradores VARIABLE IGUAL tipodato PUNTOCOMA
                  | declaradores VARIABLE IGUAL negativo PUNTOCOMA'''

def p_comparacion(p):
  'comparacion : VARIABLE comparadores VARIABLE PUNTOCOMA'
#Fin Aporte Pedro Bajana
#Inicio Aporte Aaron Franco
def p_operacion(p):
    'operacion : datonumerico operador datonumerico PUNTOCOMA'
def p_impresion(p):
  'impresion : PRINT LPARENT tipodato RPARENT PUNTOCOMA'



#Inicio Aporte Pedro Bajana
def p_funcion(p):
    '''funcion : VOID VARIABLE LPARENT declaracionfunciones VARIABLE RPARENT LLAVEL LLAVER
               | VOID VARIABLE LPARENT  VARIABLE RPARENT LLAVEL LLAVER
               | VOID VARIABLE LPARENT RPARENT LLAVEL LLAVER
               | declaracionfunciones VARIABLE LPARENT  RPARENT LLAVEL RETURN VARIABLE PUNTOCOMA LLAVER
               | declaracionfunciones VARIABLE LPARENT  RPARENT LLAVEL RETURN tipodato PUNTOCOMA LLAVER'''

def p_estructuras(p):
  '''estructuras : declaradoresestruras VARIABLE IGUAL CORCHETE_IZQ tipodatoestructura CORCHETE_DER PUNTOCOMA
             | declaradoresestruras VARIABLE IGUAL LLAVEL tipodato DOSPUNTOS tipodato LLAVER PUNTOCOMA
             | declaradoresestruras VARIABLE IGUAL MENOR_QUE declaracionfunciones MAYOR_QUE LLAVEL tipodato LLAVER PUNTOCOMA'''
#Fin Aporte Pedro Bajana

#Inicio Aporte Fabrizzio Ontaneda
def p_estructura_for(p):
  '''for : FOR LPARENT declaradores VARIABLE IN VARIABLE RPARENT LLAVEL LLAVER
          | FOR LPARENT declaradores VARIABLE IGUAL INTEGER PUNTOCOMA VARIABLE comparadores INTEGER PUNTOCOMA VARIABLE operador operador RPARENT LLAVEL LLAVER'''
def p_if(p):
  '''if : IF LPARENT VARIABLE RPARENT LLAVEL LLAVER
        | IF LPARENT TRUE RPARENT LLAVEL LLAVER
        | IF LPARENT FALSE RPARENT LLAVEL LLAVER
        | IF LPARENT VARIABLE comparadores VARIABLE RPARENT LLAVEL LLAVER
        | IF LPARENT datonumerico comparadores datonumerico RPARENT LLAVEL LLAVER'''

def p_if_else(p):
  '''if-else : if ELSE LLAVEL LLAVER'''

def p_write(p):
  '''write : STDOUT PUNTO WRITE LPARENT tipodato RPARENT PUNTOCOMA'''

#Fin Aporte Fabrizzio Ontaneda

#Inicio Aporte Pedro Bajana
def p_tipodato_funciones(p):
  '''declaracionfunciones : INT
                       | DOUBLE
                       | STRING
                       | BOOL'''



def p_tipodatoestructura(p):
  '''tipodatoestructura : INTEGER
              | CADENA
              | DOUBLE'''
#Fin Aporte Pedro Bajana
#Inicio Aporte Aaron Franco
def p_datonumerico(p):
    '''datonumerico : INTEGER
                    | DOUBLE'''
def p_operador(p):
    '''operador : MAS
                | RESTA
                | MULTIPL
                | DIVISION'''
#Fin aporte Aaron Franco
#Inicio Aporte Pedro Bajana
def p_comparadores(p):
  '''comparadores : ES_IGUAL
                  | NO_IGUAL
                  | MENOR_QUE
                  | MAYOR_QUE
                  | MENOR_O_IGUAL
                  | MAYOR_O_IGUAL'''
def p_declaradores(p):
  '''declaradores : INT
                  | CONST
                  | VAR
                  | BOOL
                  | FINAL
                  | STRING'''
def p_declaracionestructura(p):
  '''declaradoresestruras : CONST
                           | VAR
                           | FINAL'''

def p_negativo(p):
    '''
    negativo : RESTA INTEGER
              | RESTA FLOAT
    '''
#Fin Aporte Pedro Bajana
#Inicio Aporte Aaron Franco
def p_tipodato(p):
  '''tipodato : INTEGER
              | CADENA
              | FLOAT
              | VARIABLE
            '''
#Fin Aporte Aaron Franco




def p_error(p):
  if p:
    print(
      f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}"
    )
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")


# Build the parser
parser = sintactico.yacc()


def validaRegla(s):
  result = parser.parse(s)
  print(result)

while True:
  try:
    s = input('calc > ')
  except EOFError:
    break
  if not s: continue
  validaRegla(s)