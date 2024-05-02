# -*- coding: utf-8 -*-
"""
Santrich Escalona, Elizabet
(elizabet.santrich.escalona@udc.es)
Rodríguez Polín, Isabel
(isabel.rodriguezp@udc.es)
"""

class Course:
    """
    Clase que representa los objetos Course, cursos de unas academias que incluten su nombre, duración, número de estudiantes, nivel y precio.
    Esta clase permite la comparácion de sus objetos, necesaria para la ordenación de los cursos.
    
    Attributes
    ----------
    name : str
        The name of the course.
    duration : float
        The duration of the course (hours).
    students : int
        The number of students enrolled in the course.
    level : str
        The level of the course.
    language : str
        The language of the course.
    price : float
        The price of the course.

    Methods
    -------
    Dunder methods:
        __str__(self) -> str:
           Devuelve un string con los atributos del curso.

        __eq__(self, other: Film) -> bool:
           Compara si los cursos son iguales: si tienen el mismo nombre, idioma y nivel.
        
       
    """
    def __init__(self, name: str, duration: float, students: int, level: str, language: str, price: float):
        """
        Creates a Course with the given attributes.

        Parameters
        ----------
        name : str
            The name of the course.
        duration : float
            The duration of the course (hours).
        students : int
            The number of students enrolled in the course.
        level : str
            The level of the course.
        language : str
            The language of the course.
        price : float
            The price of the course.

        Returns
        -------
        None
        """
        self._name = name
        self._duration = duration
        self._students = students
        self._level = level
        self._language = language
        self._price = price
        self._benefice = self.price*self.duration * self.students
    

    @property
    def name(self):
        """
        Gets the name of the course.

        Returns
        -------
        str
            The name of the course
        """
        return self._name

    @name.setter
    def name(self, value: str):
        """
        Set the name of the course.

        Parameters
        ----------
        value : str
            The new name of the course.

        Raises
        ------
        ValueError
            If the provided value is not a non-empty string.
        """
        if isinstance(value, str) and len(value) != 0:
            self._name = value
        else:
            raise ValueError("The name of the course must be a non-empty string")

    @property
    def duration(self):
        """
        Gets the duration of the course.

        Returns
        -------
        float
            The duration of the course (hours).
        """
        return self._duration

    @duration.setter
    def duration(self, value: float):
        """
        Set the duration of the course.

        Parameters
        ----------
        value : float
            The new hours of the course duration

        Raises
        ------
        ValueError
            If the provided value is not a float greater than 0
        """
        if isinstance(value, float) and value > 0:
            self._duration = value
        else:
            raise ValueError("The hours of duration must be a float greater than 0")

    @property
    def students(self):
        """
        Gets the number of students enrolled in the course.

        Returns
        -------
        int
            The number of students enrolled in the course
        """
        return self._students

    @students.setter
    def students(self, value: int):
        """
        Set the number of students enrolled in the course.

        Parameters
        ----------
        value : int
            The new number of students enrolled in the course.

        Raises
        ------
        ValueError
            If the provided value is not a non-negative integer.
        """
        if isinstance(value, int) and value >= 0:
            self._students = value
        else:
            raise ValueError("Number of students must be a non-negative integer")

    @property
    def level(self):
        """
        Gets the level of the course.

        Returns
        -------
        str
            The level of the course
        """
        return self._level

    @level.setter
    def level(self, value: str):
        """
        Set the level of the course.

        Parameters
        ----------
        value : str
            The new level of the course.

        Raises
        ------
        ValueError
            If the provided value is not a non-empty string.
        """
        if isinstance(value, str) and len(value) != 0:
            self._level = value
        else:
            raise ValueError("Level must be a non-empty string")

    @property
    def language(self):
        """
        Gets the language of the course.

        Returns
        -------
        str
            The language of the course
        """
        return self._language

    @language.setter
    def language(self, value: str):
        """
        Set the language of the course.

        Parameters
        ----------
        value : str
            The new language of the course.

        Raises
        ------
        ValueError
            If the provided value is not a non-empty string.
        """
        if isinstance(value, str) and len(value) != 0:
            self._language = value
        else:
            raise ValueError("Language must be a non-empty string")

    @property
    def price(self):
        """
        Gets the price of the course.

        Returns
        -------
        float
            The price of the course
        """
        return self._price

    @price.setter
    def price(self, value: float):
        """
        Set the price of the course.

        Parameters
        ----------
        value : float
            The new price of the course.

        Raises
        ------
        ValueError
            If the provided value is not a non-negative float.
        """
        if isinstance(value, float) and value >= 0:
            self._price = value
        else:
            raise ValueError("Price must be a non-negative float")
            
    @property
    def benefice(self):
        """
        Gets the benefice of the course.

        Returns
        -------
        float
            The benefice of the course
        """
        return self._benefice

    def __str__(self):
        """
        Returns a string representation of the Course.

        Returns
        -------
        str
            A string representing the Course object.
        """
        return f"Name: {self.name}, Duration: {self.duration} hours, Students: {self.students}, Level: {self.level}, Language: {self.language}, Price: {self.price}€"
   
    def __eq__(self, other: "Course"):
        """
        Este método comprueba si el Course es igual (==) al other Course introducido como parámetro, comprobando si los siguientes atributos son iguales en ambos cursos: 
        nombre, language and level. Devueve True si esto ocurre y False en otro caso.
        
        Parameters
        ----------
        other : "Course"
            El Corse que queremos comparar con el que llama a la función, se quiere saber si son iguales.
        Returns
        -------
        boolean
            True if Course == other, and False otherwise.
        """
        if self.name == other.name:
            if self.level == other.level: 
                return self.level == other.level
            else: 
                return self.level == other.level
        else:
            return self.name == other.name

