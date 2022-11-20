import ply.yacc as sintactico
from lexico import tokens

def p_asignacion(p):
  'asignacion : VARIABLE IGUAL tipodato PUNTOCOMA'
def p_salida(p):
  'salida : PRINT LPARENT tipodato RPARENT PUNTOCOMA'
def p_funcion(p):
  'funcion : VARIABLE LPARENT argumentos RPARENT PUNTOCOMA'
def p_argumentos(p):
  '''argumentos : VARIABLE
                | tipodato argumentos '''
def p_tipodato(p):
  '''tipodato : INTEGER
              | VARIABLE'''
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