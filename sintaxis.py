import ply.yacc as sintactico
from lexico import tokens

def p_sentencias(p):
    '''sentencias : asignacion
                  | comparacion
                  | operacion
                  | impresion
                  | for
                  | if
                  | if-else
                  | write
                   '''
def p_sentencias2(p):
    '''sentencias2 : funcion
                   | estructuras'''
def p_sentenciasVarias(p):
  '''sentenciasVarias : sentencias2
                      | sentencias2 sentenciasVarias'''
def p_asignacion(p):
  '''asignacion : declaradores VARIABLE IGUAL tipodato PUNTOCOMA
                  | declaradores VARIABLE IGUAL negativo PUNTOCOMA
                  | BOOL VARIABLE IGUAL valoresverdad PUNTOCOMA'''
def p_declaradores(p):
  '''declaradores : INT
                  | CONST
                  | VAR
                  | BOOL
                  | FINAL
                  | STRING'''
def p_tipodato(p):
  '''tipodato : INTEGER
              | CADENA
              | FLOAT
              | VARIABLE
              | valoresverdad
              | negativo
            '''
def p_negativo(p):
    '''
    negativo : RESTA INTEGER
              | RESTA FLOAT
    '''
def p_valoresverdad(p):
  '''valoresverdad : TRUE
                   | FALSE'''
def p_comparacion(p):
  'comparacion : VARIABLE comparadores VARIABLE PUNTOCOMA'
def p_comparadores(p):
  '''comparadores : ES_IGUAL
                  | NO_IGUAL
                  | MENOR_QUE
                  | MAYOR_QUE
                  | MENOR_O_IGUAL
                  | MAYOR_O_IGUAL'''
def p_operacion(p):
    'operacion : datonumerico operador datonumerico PUNTOCOMA'
def p_datonumerico(p):
    '''datonumerico : INTEGER
                    | FLOAT
                    | negativo'''
def p_operador(p):
    '''operador : MAS
                | RESTA
                | MULTIPL
                | DIVISION'''
def p_impresion(p):
  'impresion : PRINT LPARENT tipodato RPARENT PUNTOCOMA'
def p_funcion(p):
    '''funcion : VOID VARIABLE LPARENT declaracionfunciones VARIABLE RPARENT LLAVEL LLAVER
               | VOID VARIABLE LPARENT  VARIABLE RPARENT LLAVEL LLAVER
               | VOID VARIABLE LPARENT RPARENT LLAVEL LLAVER
               | declaracionfunciones VARIABLE LPARENT  RPARENT LLAVEL RETURN VARIABLE PUNTOCOMA LLAVER
               | declaracionfunciones VARIABLE LPARENT  RPARENT LLAVEL RETURN tipodato PUNTOCOMA LLAVER'''
def p_declaracionfunciones(p):
  '''declaracionfunciones : INT
                          | DOUBLE
                          | STRING
                          | BOOL'''
def p_estructuras(p):
  '''estructuras : declaradoresestruras VARIABLE IGUAL CORCHETE_IZQ elementos CORCHETE_DER PUNTOCOMA
                 | declaradoresestruras VARIABLE IGUAL CORCHETE_IZQ CORCHETE_DER PUNTOCOMA
                 | declaradoresestruras VARIABLE IGUAL LLAVEL elementosdiccionario LLAVER PUNTOCOMA
                 | declaradoresestruras VARIABLE IGUAL MENOR_QUE declaracionfunciones MAYOR_QUE LLAVEL elementos LLAVER PUNTOCOMA'''
def p_declaracionestructura(p):
  '''declaradoresestruras : CONST
                           | VAR
                           | FINAL'''
def p_elementos(p):
  '''elementos : tipodatoestructura
               | tipodatoestructura COMA elementos'''
def p_tipodatoestructura(p):
  '''tipodatoestructura : INTEGER
                        | CADENA
                        | DOUBLE'''
def p_elementosdiccionario(p):
  '''elementosdiccionario : tipodatoestructura DOSPUNTOS tipodatoestructura
                          | tipodatoestructura DOSPUNTOS tipodatoestructura COMA elementosdiccionario '''
def p_estructura_for(p):
  '''for : FOR LPARENT declaracionesfor VARIABLE IN VARIABLE RPARENT LLAVEL LLAVER
          | FOR LPARENT declaracionesfor VARIABLE IGUAL INTEGER PUNTOCOMA VARIABLE comparadores INTEGER PUNTOCOMA VARIABLE operador operador RPARENT LLAVEL LLAVER'''
def p_declaracionesfor(p):
  '''declaracionesfor : VAR
                      | INT
                      | VARIABLE'''
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


'''
file = open('./input.dart', 'r')
content = file.read()

lines = 0
for item in content.splitlines():
    lines += 1
    if item:
        gram = parser.parse(item)
        if gram is None:
            print(f"Linea: {str(lines)} | Info: No hay errores!")
        else:
            print(f"Linea: {str(lines)} | Info: {str(gram)}")
'''