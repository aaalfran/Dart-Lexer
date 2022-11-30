


def p_operador_mat(p):
    '''
    operador_mat : MAS
                  | RESTA
                  | MULTIPL
                  | DIVISION

    '''


def p_operando_mat(p):
    '''
    operando_mat : numero
                  | VARIABLE
                  | indexacion
                  | negativo
                  | ejecutar_funcion
                  | casting_num
    '''


# Regla semántica operando numérico
def p_casting_num(p):
    '''
    casting_num : LPARENT valor AS INT RPARENT
                  | LPARENT valor AS DOUBLE RPARENT
    '''


def p_operacion_mat_sin_par(p):
    '''
    operacion_mat_sin_par : operando_mat operador_mat operacion_mat
                          | VARIABLE operador_mat operacion_mat
    '''


def p_operacion_mat_con_par(p):
    '''
    operacion_mat_con_par : LPARENT operacion_mat_sin_par RPARENT
    '''


# Regla semántica al esperar un operando numérico
def p_operacion_mat_pos(p):
    '''
    operacion_mat_pos : operacion_mat_con_par
                      | RESTA operacion_mat_con_par
                      | operacion_mat_con_par operador_mat operacion_mat_pos
                      | operacion_mat_sin_par
                      | operando_mat
    '''


def p_operacion_mat_neg(p):
    '''
    operacion_mat_neg : RESTA operacion_mat_con_par
                      | RESTA operacion_mat_con_par operador_mat operacion_mat_pos
    '''


def p_operacion_mat(p):
    '''
    operacion_mat : operacion_mat_pos
                  | operacion_mat_neg
    '''


def p_operador_comp_orden(p):
    '''
    operador_comp_orden : MAYOR_QUE
                  | MENOR_QUE
                  | MENOR_O_IGUAL
                  | MAYOR_O_IGUAL
    '''


def p_operando_comp_orden(p):
    '''
    operando_comp_orden : operacion_mat
                        | numero
                        | VARIABLE
                        | indexacion
                        | ejecutar_funcion
                        | negativo
    '''


# Regla semántica al esperar un operando numérico
def p_operacion_comp_orden_sin_par(p):
    '''
    operacion_comp_orden_sin_par : operando_comp_orden operador_comp_orden operando_comp_orden
    '''


def p_operacion_comp_orden_con_par(p):
    '''
    operacion_comp_orden_con_par : LPARENT operacion_comp_orden_sin_par RPARENT
    '''


def p_operacion_comp_orden(p):
    '''
    operacion_comp_orden : operacion_comp_orden_sin_par
                        | operacion_comp_orden_con_par
    '''


#eq = equivalencia
def p_operando_comp_eq(p):
    '''
    operando_comp_eq : numero
                    | bool
                    | CADENA
                    | operacion_mat
                    | operacion_comp_orden
                    | operacion_comp_con_par
                    | indexacion
                    | ejecutar_funcion
                    | VARIABLE
                    | operacion_log_con_par
                    | negativo
                    | LPARENT valor AS BOOL RPARENT
    '''


def p_operador_comp_eq(p):
    '''
    operador_comp_eq : IGUAL
                    | NO_IGUAL
    '''


def p_operacion_comp_eq(p):
    '''
    operacion_comp_eq : operando_comp_eq operador_comp_eq operando_comp_eq
    '''


def p_operacion_comp_sin_par(p):
    '''
    operacion_comp_sin_par : operacion_comp_eq
                    | operacion_comp_orden
    '''


def p_operacion_comp_con_par(p):
    '''
    operacion_comp_con_par : LPARENT operacion_comp_sin_par RPARENT
    '''


def p_operacion_comp(p):
    '''
    operacion_comp : operacion_comp_con_par
                    | operacion_comp_sin_par
    '''


def p_operadores_log(p):
    '''
    operadores_log : AND
                    | OR
    '''


def p_operandos_log(p):
    '''
    operandos_log : operacion_comp
                    | operacion_log_not
                    | VARIABLE
                    | bool
                    | ejecutar_funcion
                    | indexacion
    '''


def p_operacion_log_sin_par(p):
    '''
    operacion_log_sin_par : operandos_log operadores_log operacion_log
                          | operandos_log
    '''


def p_operacion_log_con_par(p):
    '''
    operacion_log_con_par : LPARENT operacion_log_sin_par RPARENT
    '''


def p_operando_log_not(p):
    '''
    operando_log_not : bool
                    | operacion_log_con_par
                    | VARIABLE
    '''


def p_operacion_log_not_sin_par(p):
    '''
    operacion_log_not_sin_par : NEGACION operando_log_not
    '''


def p_operacion_log_not_con_par(p):
    '''
    operacion_log_not_con_par : LPARENT NEGACION operando_log_not RPARENT
    '''


def p_operacion_log_not(p):
    '''
    operacion_log_not : operacion_log_not_sin_par
                        | operacion_log_not_con_par
    '''


# Regla semántica al esperar un valor booleano como operandos
def p_operacion_log(p):
    '''
    operacion_log : operacion_log_con_par
                  | operacion_log_con_par operadores_log operacion_log
                  | operacion_log_sin_par
                  | operacion_log_not
                  | operandos_log
    '''


def p_operacion_unaria(p):
    '''
    operacion_unaria : VARIABLE AUTOINCREMENTO
                      | VARIABLE AUTODECREMENTO
                      | AUTOINCREMENTO VARIABLE
                      | AUTODECREMENTO VARIABLE
    '''


def p_operaciones(p):
    '''
    operaciones : operacion_mat
                | operacion_log
                | operacion_unaria
                | operacion_autoasig
    '''


def p_operacion_autoasig(p):
    '''operacion_autoasig : VARIABLE operador_mat IGUAL operacion_mat'''
