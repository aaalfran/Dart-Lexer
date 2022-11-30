import ply.yacc as sintactico
from lexico import tokens, code
from sintacticoOp import *
from sintactico import *



def p_all(p):
    '''
    all : simbolos_globales
    '''


def p_simbolo_global(p):
    '''
    simbolo_global : declaracion_asign
                    | funcion
    '''


def p_simbolos_globales(p):
    '''
    simbolos_globales : simbolo_global
                      | simbolo_global simbolos_globales
                      | empty
    '''


def p_empty(p):
    '''
    empty :
    '''


def p_sentencia(p):
    '''
    sentencia : declaracion_var
              | asignacion
              | declaracion_asign
              | operaciones PUNTOCOMA
              | print
              | estructura_control
              | return
              | continue
              | break
    '''


def p_sentencias(p):
    '''
    sentencias : sentencia
                | sentencia sentencias
                | empty
    '''


def p_numero(p):
    '''
    numero : INTEGER
            | FLOAT
    '''


def p_bool(p):
    '''
    bool : TRUE
          | FALSE
    '''


def p_datos(p):
    '''
    datos : numero
          | CADENA
          | bool
    '''


def p_valor(p):
    '''
    valor : datos
          | operaciones
          | VARIABLE
          | estructura_dato
          | indexacion
          | read
          | ejecutar_funcion
          | negativo
          | casting
    '''


def p_negativo(p):
    '''
    negativo : RESTA numero
              | RESTA VARIABLE
              | RESTA indexacion
              | RESTA ejecutar_funcion

    '''


def p_indexacion(p):
    'indexacion : VARIABLE CORCH_IZQ valor CORCH_IZQ'


def p_tipo_dato(p):
    '''
    tipo_dato : BOOL
              | DOUBLE
              | INT
              | STRING
              | VOID
              | LIST
              | SET
              | MAP
    '''


def p_declaradores(p):
    '''
    declaradores : tipo_dato
                  | FINAL
                  | VAR
    '''


def p_declaracion_var(p):
    '''
    declaracion_var : declaradores VARIABLE PUNTOCOMA
    '''


def p_declaracion_asign(p):
    '''
    declaracion_asign : tipo_dato VARIABLE IGUAL valor PUNTOCOMA
                      | FINAL VARIABLE IGUAL valor PUNTOCOMA
                      | VAR VARIABLE IGUAL valor PUNTOCOMA
                      | CONST VARIABLE IGUAL valor PUNTOCOMA
    '''


def p_asignacion(p):
    '''
    asignacion : VARIABLE IGUAL valor PUNTOCOMA
                | VARIABLE CORCH_IZQ valor CORCH_DER IGUAL valor PUNTOCOMA
                | operacion_autoasig PUNTOCOMA
                | declaracion_asign
    '''


def p_print(p):
    'print : PRINT LPARENT valor RPARENT PUNTOCOMA'


def p_cuerpo_estruct(p):
    '''
    cuerpo_estruct : LLAVEL sentencias LLAVER
                    | sentencia
    '''


#Regla semántica al esperar una operación lógica como condición de terminación
def p_for(p):
    '''
    for : FOR LPARENT IGUAL operacion_log PUNTOCOMA operaciones RPARENT cuerpo_estruct
        | FOR LPARENT VARIABLE IN VARIABLE RPARENT cuerpo_estruct
        | FOR LPARENT tipo_dato VARIABLE IN VARIABLE RPARENT cuerpo_estruct
        | FOR LPARENT VAR VARIABLE IN VARIABLE RPARENT cuerpo_estruct
    '''


#Regla semántica al esperar una operación lógica como condición
def p_if(p):
    '''
    if : IF LPARENT operacion_log RPARENT cuerpo_estruct
    '''


#Regla semántica al esperar una operación lógica como condición
def p_if_else(p):
    '''
    if_else : IF LPARENT operacion_log RPARENT cuerpo_estruct ELSE cuerpo_estruct
    '''


#Regla semántica al esperar una operación lógica como condición
def p_while(p):
    '''
    while : WHILE LPARENT operacion_log RPARENT cuerpo_estruct
    '''


def p_estructura_control(p):
    '''
    estructura_control : if
                        | if_else
                        | while
                        | for
    '''


def p_break(p):
    'break : BREAK PUNTOCOMA'


def p_continue(p):
    'continue : CONTINUE PUNTOCOMA'


def p_read(p):
    '''
    read : STDIN PUNTO READLINESYNC LPARENT RPARENT
    '''




def p_return(p):
    '''
    return : RETURN valor PUNTOCOMA
            | RETURN PUNTOCOMA
    '''


def p_arg_funcion(p):
    '''
    arg_funcion : VARIABLE
                | VAR VARIABLE
                | tipo_dato VARIABLE
    '''


def p_args_funcion(p):
    '''
    args_funcion : arg_funcion COMA args_funcion
                  | arg_funcion
                  | empty
    '''


def p_declarar_funcion(p):
    '''
    funcion : tipo_dato VARIABLE LPARENT args_funcion RPARENT LLAVEL sentencias LLAVER
    '''


def p_ejecutar_funcion(p):
    '''
    ejecutar_funcion : VARIABLE LPARENT valores RPARENT
                      | VARIABLE LPARENT RPARENT
    '''


def p_casting(p):
    'casting : LPARENT valor AS tipo_dato RPARENT'


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






