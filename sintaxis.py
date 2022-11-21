import ply.yacc as sintactico
import datetime
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





#OPERACION ASIGNACION



# Inicio Aporte Pedro Bajana
def p_declaradores(p):
  '''declaradores : INT
                  | CONST
                  | VAR
                  | BOOL
                  | FINAL
                  | STRING'''
# Fin Aporte Pedro Bajana
# Inicio Aporte Aaron Franco
def p_tipodato(p):
  '''tipodato : INTEGER
              | CADENA
              | FLOAT
              | VARIABLE
              | valoresverdad
              | negativo
            '''
# Fin Aporte Aaron Franco
# Inicio Aporte  Pedro Bajana
def p_negativo(p):
    '''
    negativo : RESTA INTEGER
              | RESTA FLOAT
    '''
# Fin Aporte  Pedro Bajana
# Inicio Aporte Aaron Franco
def p_valoresverdad(p):
  '''valoresverdad : TRUE
                   | FALSE'''
# Inicio Aporte Aaron Franco y Pedro Bajana
def p_asignacion(p):
  '''asignacion : declaradores VARIABLE IGUAL tipodato PUNTOCOMA
                  | declaradores VARIABLE IGUAL negativo PUNTOCOMA
                  | BOOL VARIABLE IGUAL valoresverdad PUNTOCOMA'''
# Fin Aporte Aaron Franco y Pedro Bajana




#OPERACION COMPARACION


# Inicio Aporte  Pedro Bajana
def p_comparadores(p):
  '''comparadores : ES_IGUAL
                  | NO_IGUAL
                  | MENOR_QUE
                  | MAYOR_QUE
                  | MENOR_O_IGUAL
                  | MAYOR_O_IGUAL'''

def p_comparacion(p):
  'comparacion : VARIABLE comparadores VARIABLE PUNTOCOMA'
# Fin Aporte  Pedro Bajana







#OPERACION ARITMETICA



# Inicio Aporte Aaron Franco
def p_datonumerico(p):
    '''datonumerico : INTEGER
                    | FLOAT
                    | negativo'''

def p_operador(p):
    '''operador : MAS
                | RESTA
                | MULTIPL
                | DIVISION'''

def p_operacion(p):
    'operacion : datonumerico operador datonumerico PUNTOCOMA'
# Fin Aporte Aaron Franco







#OPERACION IMPRESION

# Inicio Aporte Pedro Bajana
def p_impresion(p):
  'impresion : PRINT LPARENT tipodato RPARENT PUNTOCOMA'
# Inicio Aporte Pedro Bajana






#OPERACION FUNCIONES

# Inicio Aporte Pedro Bajana
def p_declaracionfunciones(p):
  '''declaracionfunciones : INT
                          | DOUBLE
                          | STRING
                          | BOOL'''

def p_funcion(p):
    '''funcion : VOID VARIABLE LPARENT declaracionfunciones VARIABLE RPARENT LLAVEL LLAVER
               | VOID VARIABLE LPARENT  VARIABLE RPARENT LLAVEL LLAVER
               | VOID VARIABLE LPARENT RPARENT LLAVEL LLAVER
               | declaracionfunciones VARIABLE LPARENT  RPARENT LLAVEL RETURN VARIABLE PUNTOCOMA LLAVER
               | declaracionfunciones VARIABLE LPARENT  RPARENT LLAVEL RETURN tipodato PUNTOCOMA LLAVER'''
# Fin Aporte Pedro Bajana









#OPERACION ESTRUCTURAS



# Inicio Aporte Pedro Bajana
def p_declaracionestructura(p):
  '''declaradoresestruras : CONST
                           | VAR
                           | FINAL'''

def p_tipodatoestructura(p):
  '''tipodatoestructura : INTEGER
                        | CADENA
                        | DOUBLE'''
# Fin Aporte Pedro Bajana
# Inicio Aporte Aaron Franco
def p_elementos(p):
  '''elementos : tipodatoestructura
               | tipodatoestructura COMA elementos'''

def p_elementosdiccionario(p):
  '''elementosdiccionario : tipodatoestructura DOSPUNTOS tipodatoestructura
                          | tipodatoestructura DOSPUNTOS tipodatoestructura COMA elementosdiccionario '''
# Fin Aporte Aaron Franco
# Inicio Aporte Pedro Bajana
def p_estructuras(p):
  '''estructuras : declaradoresestruras VARIABLE IGUAL CORCHETE_IZQ elementos CORCHETE_DER PUNTOCOMA
                 | declaradoresestruras VARIABLE IGUAL CORCHETE_IZQ CORCHETE_DER PUNTOCOMA
                 | declaradoresestruras VARIABLE IGUAL LLAVEL elementosdiccionario LLAVER PUNTOCOMA
                 | declaradoresestruras VARIABLE IGUAL MENOR_QUE declaracionfunciones MAYOR_QUE LLAVEL elementos LLAVER PUNTOCOMA'''
# Fin Aporte Pedro Bajana








#OPERACION FOR

# Inicio Aporte Fabrizzio Ontaneda
def p_declaracionesfor(p):
  '''declaracionesfor : VAR
                      | INT
                      | VARIABLE'''

def p_estructura_for(p):
  '''for : FOR LPARENT declaracionesfor VARIABLE IN VARIABLE RPARENT LLAVEL LLAVER
          | FOR LPARENT declaracionesfor VARIABLE IGUAL INTEGER PUNTOCOMA VARIABLE comparadores INTEGER PUNTOCOMA VARIABLE operador operador RPARENT LLAVEL LLAVER'''
# Fin Aporte Fabrizzio Ontaneda









#OPERACION IF


# Inicio Aporte Fabrizzio Ontaneda
def p_if(p):
  '''if : IF LPARENT VARIABLE RPARENT LLAVEL LLAVER
        | IF LPARENT TRUE RPARENT LLAVEL LLAVER
        | IF LPARENT FALSE RPARENT LLAVEL LLAVER
        | IF LPARENT VARIABLE comparadores VARIABLE RPARENT LLAVEL LLAVER
        | IF LPARENT datonumerico comparadores datonumerico RPARENT LLAVEL LLAVER'''
# Fin Aporte Fabrizzio Ontaneda





#OPERACION IF ELSE


# Inicio Aporte Fabrizzio Ontaneda
def p_if_else(p):
  '''if-else : if ELSE LLAVEL LLAVER'''
# Fin Aporte Fabrizzio Ontaneda





#OPERACION WRITE

# Inicio Aporte Fabrizzio Ontaneda
def p_write(p):
  '''write : STDOUT PUNTO WRITE LPARENT tipodato RPARENT PUNTOCOMA'''   
# Fin Aporte Fabrizzio Ontaneda










def p_error(p):
  if p:
    print(
      f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}"
    )
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")




#Crear Log

file1 = open("log.txt","a") 
date_time = datetime.datetime.now()

file1.write("Prueba Realizada el dia: "+ date_time.strftime("%d/%m/%Y")+ " a las: "+ date_time.strftime("%X")+"\n") 

 
# Build the parser
parser = sintactico.yacc()

file = open('./input.dart', 'r')
content = file.read()

lines = 0
for item in content.splitlines():
    lines += 1
    if item:
        gram = parser.parse(item)
        if gram is None:
            print(f"Linea: {str(lines)} | Info: No hay errores!")
            file1.write(f"Linea: {str(lines)} | Info: No hay errores! \n")
        else:
            print(f"Linea: {str(lines)} | Info: {str(gram)}")
            file1.write(f"Linea: {str(lines)} | Info: {str(gram)}")


file.close() 







'''
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





