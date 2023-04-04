def mylists():
    contadorsuperlargooficial = 0
    for i in range(20):
        contadorsuperlargooficial += 1


class MiClase:
    def __init__(self):
        self.nombrevariablemuylargolarguisimo = None

    def mi_metodo(self, resultado):
        self.nombrevariablemuylargolarguisimo = resultado

# es un caso adicional por que muestra que solo tira error cuando se define una variable larga y no cuando se llama 
# a esta mas adelante para hacer operaciones, ya que dejarian de ser del tipo Assign
# por el mismo motivo si se levanta el warning las dos veces que se asigna un valor en las lines 9 y 12.
# CORRECTO
# expectedWarnings = [Warning('VariableLongName', 2, 'variable contadorsuperlargooficial has a long name'),            -> CORRECTO
#                     Warning('VariableLongName', 9, 'variable nombrevariablemuylargolarguisimo has a long name'),
#                     Warning('VariableLongName', 12, 'variable nombrevariablemuylargolarguisimo has a long name')]


# POSIBLES RESULTADOS PERO QUE SERIAN INCORRECTOS
# expectedWarnings = [Warning('VariableLongName', 2, 'variable contadorsuperlargooficial has a long name'),
#                     Warning('VariableLongName', 4, 'variable contadorsuperlargooficial has a long name'),
#                     Warning('VariableLongName', 9, 'variable nombrevariablemuylargolarguisimo has a long name')] -> ESTO HUBIESE SIDO UNA VERSION INCORRECTA

# expectedWarnings = [Warning('VariableLongName', 2, 'variable contadorsuperlargooficial has a long name'),
#                       Warning('VariableLongName', 12, 'variable nombrevariablemuylargolarguisimo has a long name')] -> ESTO HUBIESE SIDO UNA VERSION INCORRECTA

# expectedWarnings = [Warning('VariableLongName', 2, 'variable contadorsuperlargooficial has a long name'),
#                     Warning('VariableLongName', 4, 'variable contadorsuperlargooficial has a long name'),
#                     Warning('VariableLongName', 9, 'variable nombrevariablemuylargolarguisimo has a long name',
#                     Warning('VariableLongName', 12, 'variable nombrevariablemuylargolarguisimo has a long name'))] -> ESTO HUBIESE SIDO UNA VERSION INCORRECTA