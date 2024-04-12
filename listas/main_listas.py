# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 11:46:56 2024

@author: elisa
"""

import sys
from array_ordered_positional_list import ArrayOrderedPositionalList
from linked_ordered_positional_list import LinkedOrderedPositionalList 

class Film():
    def __init__(self, director: str, title: str, release_year: int, score: float):
        self._director = director
        self._title = title
        self._release_year = release_year
        self._score = score

    
    @property
    def director(self):
        """
        Gets the director of the film.
        Returns
        -------
        str
            El nombre (apellido y nombre) del director de la película.
        """
        return self._director

    @director.setter
    def director(self, value: str):
        """
        Set the name of the director.

        Parameters
        ----------
        value : str 
            The new name of the director of the film.

        Raises
        ------
        ValueError
            If the provided value is an empty string.
        """
        if isinstance(value, str) and len(value) != 0:
            self._director = value
        else:
            raise ValueError("The name of the director must be a non empty string")
          
            
    @property
    def title(self):
        """
        Gets the title of the film.
        Returns
        -------
        str
            The title of the film.
        """
        return self._title

    @title.setter
    def title(self, value: str):
        """
        Set the title of the film.

        Parameters
        ----------
        value : str 
            The new title of the film.

        Raises
        ------
        ValueError
            If the provided value is an empty string.
        """
        if isinstance(value, str) and len(value) != 0:
            self._title = value
        else:
            raise ValueError("The title of the film must be a non empty string")
            
    @property
    def release_year(self):
        """
        Gets the release year of the film. 

        Returns
        -------
        int
            The year when the film was released.
        """
        return self._release_year

    @release_year.setter
    def release_year(self, value: int):
        """
        Set the release year of the film.

        Parameters
        ----------
        value : int  
            The new year when the film was released.

        Raises
        ------
        ValueError
            If the provided value is not a positive integer.
        """
        if isinstance(value, int) and value >= 0:
            self._release_year = value
        else:
            raise ValueError("The release year must be a positive integer")
            
            
    @property
    def score(self):
        """
        Gets the score of the film. 

        Returns
        -------
        float
            The score that was given to the film.
        """
        return self._score

    @score.setter
    def score(self, value: float):
        """
        Set the score of the film.

        Parameters
        ----------
        value : float  
            The new score that was given to the film.

        Raises
        ------
        ValueError
            If the provided value is not a positive float.
        """
        if isinstance(value, float) and value >= 0:
            self._score = value
        else:
            raise ValueError("The score must be a positive float")
            
            
    def __ge__(self, other: "Film"):
        
        if self.director == other.director:
            if self.release_year == other.release_year:
                return self.title >= other.title
            else:
                return self.release_year >= other.release_year
        else:
            return self.director >= other.director
        
    def __gt__(self, other: "Film"):
        
        if self.director == other.director:
            if self.release_year == other.release_year:
                return self.title > other.title
            else:
                return self.release_year > other.release_year
        else:
            return self.director > other.director
    

def create_film(films_text):
    
    film_list = LinkedOrderedPositionalList()
    films = films_text.split("\n")
    for line in films:
        film_info = line.split(';')
        print(film_info)
        director, title, release_year, score = film_info
        print(director, title, release_year, score)
        film = Film(director, title, release_year, score)
        film_list.add(film)
    print("[", end=" ")
    for x in film_list:
        print(x.title, end=", ")
    print("]")
        

def main():
    """
    The main function that reads from a file and starts the simulation.
    """

    with open(sys.argv[1]) as f:
        # With strip(), we ensure that there are no additional spaces, tabs, or newline characters present in the file.
        
        films_text = f.read().strip()
        print(films_text)
        create_film(films_text)


if __name__ == '__main__':
    main()
