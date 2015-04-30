# -*- coding: utf-8 -*-

"""
    Archivo donde se ejemplifica la inyección de datos mediante la utilización
    de decoradores en Python.

    *   Función de orden superior:
            En Matemática o Informática funciones de orden superior son funciones que cumplen una de dos:

                - Tomar una o más funciones como entrada
                - Devolver una función como salida

            Link: https://es.wikipedia.org/wiki/Funci%C3%B3n_de_orden_superior

    *   Definición de Decorador:
            Un decorador es una función ‘d’ que recibe como argumento otra función ‘a’ y 
            retorna una nueva función ‘b’. La nueva función ‘b’ es la función ‘a’ decorada con ‘d’.

            def d(a):
                def b():
                    return a
                return b

            Link: http://www.juanjoconti.com.ar/2008/07/11/decoradores-en-python-i/

"""

def dec1(function):
    """ Decorador que se encarga de agregar un número a la lista de argumentos """
    def wrapper(*args):
    	l = list(args)
    	l[0].append(25)
        return function(*l)
    return wrapper

def dec2(function):
    """ Decorador que se encarga de agregar un dato al dict que recibe como argumento"""
    def wrapper(**kwargs):
    	kwargs['c'] = 25
        return function(**kwargs)
    return wrapper

def dec3(function):
    """ Decorador que se encarga de agregar un nombre a la petición <request> recibida como argumento """
    def wrapper(request):
    	request['user'] = u'Elio Rincon'
        return function(request)
    return wrapper

#######################################################################################

@dec1
def suma_uno(*args):
    """ 
        Función decorada 1:
            Se encarga de sumar una lista de argumentos

        Input: [1, 2, 3, 4, 5, 25]
        Output: 40
    """
    print sum(*args)

# suma_uno = dec1(suma_uno)
#######################################################################################

@dec2
def suma_dos(**kwargs):
    """ 
        Función decorada 1:
            Se encarga de sumar una lista de argumentos

        Input: [1, 2, 3, 4, 5]
        Output: 15
    """
    print suma_dict(**kwargs)

def suma_dict(**d):
    """ Función encargada de sumar los valores en dict """
    return sum([i for i in d.itervalues()])

#suma_dos = dec2(suma_dos)
#######################################################################################


def my_view(request):
	print "Nombre: ", request['user']

my_view = dec3(my_view)
#######################################################################################

suma_uno([1, 2]) # suma_dos(*args)


suma_dos(a = 1, b = 2, r = 3) # suma_dos(**kwargs)


my_view({}) # suma_dos(request)

