

def p_valores(p):
    '''
    valores : valor
            | valor COMA valores
    '''


def p_clave_valor(p):
    '''
      clave_valor : valor DOSPUNTOS valor
    '''


def p_claves_valores(p):
    '''
    claves_valores : clave_valor
                    | clave_valor COMA claves_valores
    '''

def p_cuerpo_lista_STRING(p):
    '''
     cuerpo_lista_string : CADENA
                     | CADENA COMA CADENA
                     | CADENA COMA CADENA COMA cuerpo_lista_string
     '''

def p_cuerpo_lista_INTEGER(p):
    '''
     cuerpo_lista_integer : INTEGER
                     | INTEGER COMA INTEGER
                     | INTEGER COMA INTEGER COMA cuerpo_lista_integer
     '''

def p_cuerpo_lista_DOUBLE(p):
    '''
     cuerpo_lista_double : FLOAT
                     | FLOAT COMA FLOAT
                     | FLOAT COMA FLOAT COMA cuerpo_lista_double
     '''
def p_cuerpo_lista_BOOLEAN(p):
    '''
     cuerpo_lista_boolean : bool
                     | bool COMA bool
                     | bool COMA bool COMA cuerpo_lista_boolean
     '''


#Regla semántica 6 las listas solo poseen un tipo de dato específico
def p_lista(p):
    '''
    lista :  LIST MENOR_QUE STRING MAYOR_QUE VARIABLE IGUAL CORCH_IZQ cuerpo_lista_string CORCH_DER PUNTOCOMA
           | LIST MENOR_QUE INT MAYOR_QUE VARIABLE IGUAL CORCH_IZQ cuerpo_lista_integer CORCH_DER PUNTOCOMA
           | LIST MENOR_QUE DOUBLE MAYOR_QUE VARIABLE IGUAL CORCH_IZQ cuerpo_lista_double CORCH_DER PUNTOCOMA
           | LIST MENOR_QUE BOOL MAYOR_QUE VARIABLE IGUAL CORCH_IZQ cuerpo_lista_boolean CORCH_DER PUNTOCOMA
    '''


# Regla semántica 7 operaciones con strings
def p_concatenacion_string(p):
    '''string : CADENA MAS CADENA'''

def p_repeticion_string(p):
    '''string : CADENA MULTIPL CADENA'''
def p_string_casting_toInt(p):
    '''casting : CADENA PUNTO TOINT LPARENT RPARENT'''
def p_string_casting_toDouble(p):
    '''casting : CADENA PUNTO TODOUBLE LPARENT RPARENT'''
def p_string_casting_toString(p):
    '''casting : INTEGER PUNTO TOSTRING LPARENT RPARENT
                | FLOAT PUNTO TOSTRING LPARENT RPARENT'''




def p_conjunto(p):
    '''
    conjunto : LLAVEL valores LLAVER
              | LLAVEL LLAVER
    '''

def p_mapa(p):
    '''
    mapa : LLAVEL claves_valores LLAVER
        | LLAVEL LLAVER
    '''




def p_estructura_dato(p):
    '''
    estructura_dato : lista
                    | conjunto
                    | mapa
    '''


