edad = 16
permiso_padres = True

if edad >= 18:
    print('Puedes obtener la licencia de conducir.')
else:
    if edad >= 16:
        if permiso_padres:
            print('Puedes obtener la licencia con permiso de tus padres.')
        else:
            print('Necesitas el permiso de tus padres para obtener la licencia.')
    else:
        print('Eres demasiado joven para conducir.')

        # Este programa determina si una persona puede obtener la licencia de conducir según su edad y si tiene permiso de sus padres, utilizando condicionales anidados.