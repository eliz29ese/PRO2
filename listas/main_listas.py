# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 11:46:56 2024

@author: elisa
"""

import sys
from array_ordered_positional_list import ArrayOrderedPositionalList
from linked_ordered_positional_list import LinkedOrderedPositionalList 
import pandas


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
            
    def print_film(self):
        return(f"{self.director}; {self.title}; {self.release_year}; {self.score}")
            
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
        
        
class Film_Manager():
    
    def __init__(self):
        self.film_list = LinkedOrderedPositionalList()
        
    @property
    def film_list(self):
        """
        Gets the director of the film.
        Returns
        -------
        str
            El nombre (apellido y nombre) del director de la película.
        """
        return self._film_list

    @film_list.setter
    def film_list(self, value: list):
        """
        Set the ordered list of films.

        Parameters
        ----------
        value : str 
            The new ordered list of films.

        Raises
        ------
        ValueError
            If the provided value is not a list of Film elements.
        """
        if isinstance(value, LinkedOrderedPositionalList):
            self._film_list = value
        else:
            raise ValueError("The name of the director must be a non empty string")
        for film in self._film_list:
            if not isinstance(film, "Film"):
                raise TypeError("Elements of film_list must be Films")

    def create_film(self, films_text):
        data_film_list = []
        films = films_text.split("\n")
        for line in films:
            film_info = line.split('; ')
            print(film_info)
            director, title, release_year, score = film_info
            print(director, title, release_year, score)
            film = Film(director, title, int(release_year), float(score))
            data_film_list.append([film.director, film.title, film.release_year, film.score])
            self.film_list.add(film)
        print("[", end=" ")
        for x in self.film_list:
            print(x.print_film(), end="\n")
        print("]")
        return(data_film_list)
        
    def user_menu(self):
        try:
           option = int(input("Choose one of the following options: \n 1) All platform movies \n 2) Movies directed by a director \n 3) Movies released in a year\n - Press any other key to exit\n"))
           while option != 0 and option in (1,2,3):
               if option == 1:
                   for film in self.film_list:
                       print(film.print_film())
                       
               elif option == 2:
                    author = input("Autor de las películas que desea consultar: \n")
                    for film in self.film_list:
                        if film.director == author:
                            print(film.print_film())
               elif option == 3:
                   year = input("Año de estreno de las películas que desea consultar: \n")
                   
                   if isinstance(year, int):
                        for film in self.film_list:
                            if film.release_year == int(year):
                                print(film.print_film())
                   else:
                        print("Please enter a valid year")

               option = int(input("\nChoose one of the following options: \n 1) All platform movies \n 2) Movies directed by a director \n 3) Movies released in a year\n - Pulse 0 to exit\n"))
             
           print("Exiting..")
           
        except:
            print("Exiting..")
      
    def pandas_stats(self, data_film_list:list):
        data = pandas.DataFrame(data_film_list, columns=["Director", "Films", "Release year", "Score"])
        group_col = "Director"
        target_col = "Films"
        single_stats = data.groupby(group_col).agg({target_col: ["count"]})
        print('\n', "*"*37, '\n', "          Number of films     ", '\n',  "*"*37)
        print(single_stats, "\n")
        
        group_col = "Director"
        target_col = "Score"
        single_stats = data.groupby(group_col).agg({target_col: ["mean"]})
        print('\n', "*"*37, '\n', "      Mean score for director   ", '\n',  "*"*37)
        print(single_stats, "\n")
        
        group_col = "Release year"
        target_col = "Score"
        single_stats = data.groupby(group_col).agg({target_col: ["mean"]})
        print('\n', "*"*37, '\n', "    Mean score for release year ", '\n',  "*"*37)
        print(single_stats, "\n")
           
      
def main():
    """
    The main function that reads from a file and starts the simulation.
    """

    with open(sys.argv[1], encoding="utf-8") as f:
        # With strip(), we ensure that there are no additional spaces, tabs, or newline characters present in the file.
        
        films_text = f.read().strip()
        print(films_text)
        manager = Film_Manager()
        data_film_list = manager.create_film(films_text)
        manager.pandas_stats(data_film_list)
        manager.user_menu()

if __name__ == '__main__':
    main()
