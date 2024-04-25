# -*- coding: utf-8 -*-
"""
Santrich Escalona, Elizabet
(elizabet.santrich.escalona@udc.es)
Rodríguez Polín, Isabel
(isabel.rodriguezp@udc.es)
"""
from avl_tree import AVL

class Course:
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

    def __str__(self):
        """
        Returns a string representation of the Course.

        Returns
        -------
        str
            A string representing the Course object.
        """
        return f"Name: {self.name}, Duration: {self.duration} hours, Students: {self.students}, Level: {self.level}, Language: {self.language}, Price: {self.price}€"

def create_course(cursos_text:str, academy:str )-> None:
    tree_A = AVL()
    tree_B = AVL()
    
    cursos = cursos_text.split("\n")
    for line in cursos:
        if not line.startswith('#'):
            curso_info = line.split(',')
            name, duration, students, level, language, price= curso_info 
            curso = Course(name, duration, students, level, language, price)
            if academy == 'A':
                tree_A[curso.name, curso.level, curso.language] = curso
            else: 
                tree_B[curso.name, curso.level, curso.language] = curso
    preorder_indent_BST(tree_A,tree_A.root(),0)
    preorder_indent_BST(tree_B,tree_B.root(),0)

def preorder_indent_BST(T, p, d):
    """Print preorder representation of a binary subtree of T rooted at p at depth d.
       To print aTree completely call preorder_indent_BST(aTree, aTree.root(), 0)"""
    if p is not None:
        # use depth for indentation
        print(2*d*' ' + "(" + str(p.key()) + "," +  str(p.value()) + ")") 
        preorder_indent_BST(T, T.left(p), d+1) # left child depth is d+1
        preorder_indent_BST(T, T.right(p), d+1) # right child depth is d+1
    
cursos_A = input('Ingrese el nombre del archivo donde se encuentran los cursos de la academia A:')  
cursos_B = input('Ingrese el nombre del archivo donde se encuentran los cursos de la academia B:')     
with open(cursos_A, encoding="ISO-8859-1") as f:
     # With strip(), we ensure that there are no additional spaces, tabs, or newline characters present in the file.
    cursos_text = f.read().strip()
    create_course(cursos_text, 'A') 
with open(cursos_B, encoding="ISO-8859-1") as f:
     # With strip(), we ensure that there are no additional spaces, tabs, or newline characters present in the file.
    cursos_text = f.read().strip()
    create_course(cursos_text, 'B')    
