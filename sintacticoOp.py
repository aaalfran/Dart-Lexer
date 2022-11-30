

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


def p_lista(p):
    '''
    lista : CORCH_IZQ valores CORCH_DER
          | CORCH_IZQ CORCH_DER
    '''






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


