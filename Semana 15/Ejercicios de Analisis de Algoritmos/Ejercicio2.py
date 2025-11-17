# 2. Analice los siguientes algoritmos usando la Big O Notation:

def print_numbers_times_2(numbers_list):
	for number in numbers_list:
		print(number * 2)
		
#* Respuesta:
#? La complejidad es O(n), donde n es la longitud de numbers_list. Esto se debe a que el ciclo recorre todos los elementos de la lista una vez.


def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:
		for element_b in list_b:
			if element_a == element_b:
				return True
				
	return False

#* Respuesta:
#? La complejidad es O(n * m), donde n es la longitud de list_a y m es la longitud de list_b


def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)):
		print(list_to_print[index])
		
#* Respuesta:
#? Este algoritmo es O(1) porque el ciclo utiliza una operacion constante para determinar cuantos ciclos recorrera, los cuales como maximo seran 10 sin importar el tamaño de la lista


def generate_list_trios(list_a, list_b, list_c):
	result_list = []
	for element_a in list_a:
		for element_b in list_b:
			for element_c in list_c:
				result_list.append(f'{element_a} {element_b} {element_c}')
				
	return result_list 

#* Respuesta:
#? La complejidad algoritmica es O(n**3) por la cantidad de iteraciones anidadas que tiene, aunque si los tamaños de las listas varian entonces seria O(n*m*p), donde cada letra es la longitud de cada lista



#! ***EXTRAS***
# EJERCICIO 1

# Version 1
def manual_add(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

#? Este algoritmo recorre todos los numeros desde 1 hasta n, por lo que su complejidad es O(n), donde n es el valor de entrada, ya que el algoritmo recorrera n numeros.


# Version 2
def add_formula(n):
    return n * (n + 1) // 2

#? Este algoritmo no tiene bucles ni iteraciones, solo realiza unas pocas operaciones aritmeticas de complejidad O(1), la operacion mas compleja de la funcion es O(1) por lo que la complejidad total del algoritomo en Big O es O(1)

#? Si n = 1,000,000 usaria la version 2 porque tiene una complejidad O(1), lo que permite calcular el resultado en tiempo constante. Mientras que la version 1 por ser un numero tan grande tomaria mucho mas tiempo al ser de complejidad O(n)


# EJERCICIO 2

def linear_search(my_list, target):
    for item in my_list:
        if item == target:
            return True
    return False

def binary_search(my_list, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

#? La complejidad del linar_search, como lo dice su nombre tiene una complejidad linear O(n), donde n es el tamaño de la lista y en el peor de los casos se recorre toda la lista.
#? Se debe usar cuando no se tiene informacion sobre el orden de los elenmentos en la lista a recorrer

#? La complejidad de binary_search, es O(log n), ya que en cada iteracion el algoritmo va dividiendo la lista a la mitad, y esto recuce el numero de elementos que deben ser revisados.
#? Este tipo de busqueda es sumamente util y eficiente en listas ordenadas.

#? Si la lista no esta ordenada, no podemos usar binary_search ya que esto solo funciona con listas ordenadas, si no esta ordenada, la busqueda binaria no dividiria correctamente y es altamente probable que no se encuentre el objetivo. Mientras que linear_search si funcionaria si aunque la lista no este ordenada.


# EJERCICIO 3

def print_all_pairs(my_dict):
    for key1 in my_dict:
        for key2 in my_dict:
            print(f"{key1}-{key2}")

#? La funcion tiene dos bucles anidados y ambos iteran sobre todas las claves del mismo iterable en este caso my_dict, el numero de iteraciones es n * n = n²

#? La duracion para un millon de claves seria considerable pero no hay una duracion fija ya que esto depende de las capacidades de cada procesador, pero aun con un buen procesador si pasamos convertimos n² = (1,000,000)² = 1,000,000,000,000 nos da un numero bastante grande.