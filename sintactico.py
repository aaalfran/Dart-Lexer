import ply.yacc as sintactico
from lexico import tokens


#INICIO APORTES PEDRO BAJAÑA
def p_comparacion(p):
  '''comparaciones : VARIABLE comp VARIABLE PUNTOCOMA
  '''

def p_asignacion(p):
  'asignacion : declaradores VARIABLE IGUAL tipodato PUNTOCOMA'


def p_salida(p):
  'salida : PRINT LPARENT tipodato RPARENT PUNTOCOMA'
def p_funcion(p):
  'funcion : VARIABLE LPARENT argumentos RPARENT PUNTOCOMA'
def p_argumentos(p):
  '''argumentos : VARIABLE
                | tipodato argumentos '''

#INICIO APORTE PEDRO BAJAÑA
def p_tipodato(p):
  '''
  tipodato : INTEGER
            | CADENA
            | DOUBLE
            | VARIABLE


  '''
def p_declaradores(p):
  '''
  declaradores : INT
                | CONST
                | VAR
                | BOOL
                | FINAL
                | STRING
  '''
def p_simnbolos(p):
  '''
  comp : ES_IGUAL
         | NO_IGUAL
         | MENOR_QUE
         | MAYOR_QUE
         | MENOR_O_IGUAL
         | MAYOR_O_IGUAL
  '''
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