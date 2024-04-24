# -*- coding: utf-8 -*-
"""
Santrich Escalona, Elizabet
(elizabet.santrich.escalona@udc.es)
Rodríguez Polín, Isabel
(isabel.rodriguezp@udc.es)
"""

class Course: 
    def __init__(self, name: str, duration: float , students: int, level: str, language: str, price: float):
        """
        Creates a Course with the given attributes.

        Parameters
        ----------
        name : str
            DESCRIPTION.
        duration : float
            DESCRIPTION.
        students : int
            DESCRIPTION.
        level : str
            DESCRIPTION.
        language : str
            DESCRIPTION.
        price : float
            DESCRIPTION.

        Returns
        -------
        None.

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
        if isinstance(value, str) and len(value) != 0 :
            self._name = value
        else:
            raise ValueError("The name of the course must be a non empty string")

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
            If the provided value is not a float grater than 0
        """
        if isinstance(value, str) and len(value) != 0 :
            self._duration = value
        else:
            raise ValueError("The name of the course must be a non empty string")
