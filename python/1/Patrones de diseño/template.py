# -*- coding: utf-8 -*-
import abc
"""
    Archivo donde se ejemplifica el patrón de diseño Template

    *   Template method pattern:
            In software engineering, the template method pattern is a behavioral design pattern 
            that defines the program skeleton of an algorithm in a method, called template method,
            which defers some steps to subclasses.[1] It lets one redefine certain steps of an 
            algorithm without changing the algorithm's structure

            Link: https://en.wikipedia.org/wiki/Template_method_pattern

    * Patrón de diseño Template:
            El patrón Template Method (Método Plantilla o Método Modelo en español) es un patrón 
            de diseño enmarcado dentro de los llamados patrones de comportamiento, que se 
            caracteriza por la definición, dentro de una operación de una superclase, de los 
            pasos de un algoritmo, de forma que todos o parte de estos pasos son redefinidos 
            en las subclases herederas de la citada superclase.

            Link: https://es.wikipedia.org/wiki/Template_Method_%28patr%C3%B3n_de_dise%C3%B1o%29

"""

##################################### Uso 1 #################################################
class Algorithm(object):
	__metaclass__ = abc.ABCMeta

	def __init__(self, items):
		self.items = items

	def execute(self):
		self.method_algorithm()

	@abc.abstractmethod
	def method_algorithm(self):
		""" Método que debe sobreescribir la clase hija para implementar el algoritmo """
		pass

class  AlgorithmBubbleSort(Algorithm):
	def method_algorithm(self):
		items_original = list(self.items)
		for i in range(len(self.items)):
			for j in range(len(self.items)-1-i):
				if self.items[j] > self.items[j+1]:
					self.items[j], self.items[j+1] = self.items[j+1], self.items[j]    

		print ("AlgorithmInsertionSort: ")
		print ("Input: ", items_original)
		print ("Output: ", self.items)

class  AlgorithmInsertionSort(Algorithm):
	def method_algorithm(self):
		items_original = list(self.items)
		for i in range(1, len(self.items)):
			j = i
			while j > 0 and self.items[j] < self.items[j-1]:
				self.items[j], self.items[j-1] = self.items[j-1], self.items[j]
				j -= 1

		print ("AlgorithmInsertionSort: ")
		print ("Input: ", items_original)
		print ("Output: ", self.items)
			
list_nums = [1, 5, 3, 0, 9]

bubble_sort = AlgorithmBubbleSort(list_nums)
bubble_sort.execute()

insertion_sort = AlgorithmInsertionSort(list_nums)
insertion_sort.execute()

#Link: http://danishmujeeb.com/blog/2014/01/basic-sorting-algorithms-implemented-in-python

##################################### Uso 2 #################################################


class ObjectTest(object):
	def method_override(self):
		print("\nmethod_override => llamado a método de la clase padre desde la clase hija\n")




obj = ObjectTest()
obj.method_override()



#############################################################################################

class Template(object):
	__metaclass__ = abc.ABCMeta

	def execute(self):
		self.method_override1()
		self.method_override2()

	@abc.abstractmethod
	def method_override1(self):
		""" Método que debe sobreescribir la clase hija """
		pass

	@abc.abstractmethod
	def method_override2(self):
		""" Método que debe sobreescribir la clase hija """
		pass


class TemplateOne(Template):

	def method_override1(self):
		print("\nmethod_override1 => llamado a método de la clase hija desde la clase padre")

	def method_override2(self):
		print("method_override2 => llamado a método de la clase hija desde la clase padre\n")


one = TemplateOne()
one.execute()

##############################################################################################