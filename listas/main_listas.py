
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
            The director's name (last name and first name) of the movie.
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
            If the provided value is not a non  empty string.
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
            If the provided value is not a non empty string.
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
            If the provided value is not a positive float between 0 and 10.
        """
        if isinstance(value, float) and 0<=value<=10:
            self._score = value
        else:
            raise ValueError("The score must be a positive float between 0 and 10")
            
    def print_film(self):
        """
        Function that returns a string with the information of the Film, which is used to examine the data of a movie 
        outside the class.
    
        Returns
        -------
        str
            String containing the data of the Film (director, title, release year and score).
        """
        return(f"{self.director}; {self.title}; {self.release_year}; {self.score}")
            
    def __ge__(self, other: "Film"):
        """
        This method is used to check if a Film is greater than or equal to (>=) another Film provided as a parameter (other). 
        To do this, it starts by comparing the directors based on lexicographical ordering. If there is a tie, it compares by the release year. 
        Finally, if there is another tie, it compares by the title of the Film, as it did with the director. This function returns a boolean value 
        depending on whether the Film calling the function (self) is greater than or equal to the other Film (returning True in this case and False otherwise).
        
        Parameters
        ----------
        other : "Film"
            The Film being compared to the Film used to call the function, wanting to know if the latter is greater than or equal to other.
        
        Returns
        -------
        boolean
            True if Film >= other, and False otherwise.
        """
        
        if self.director == other.director:
            if self.release_year == other.release_year:
                return self.title >= other.title
            else:
                return self.release_year >= other.release_year
        else:
            return self.director >= other.director
        
    def __gt__(self, other: "Film"):
        """
        This method is used to check if a Film is greater than (>) another Film provided as a parameter (other). 
        To do this, it starts by comparing the directors based on lexicographical ordering. If there is a tie, it compares by the release year. 
        Finally, if there is another tie, it compares by the title of the Film, as it did with the director. This function returns a boolean value 
        depending on whether the Film calling the function (self) is greater than the other Film (returning True in this case and False otherwise).
        
        Parameters
        ----------
        other : "Film"
            The Film being compared to the Film used to call the function, wanting to know if the latter is greater than other.
        
        Returns
        -------
        boolean
            True if Film > other, and False otherwise.
        """
        
        if self.director == other.director:
            if self.release_year == other.release_year:
                return self.title > other.title
            else:
                return self.release_year > other.release_year
        else:
            return self.director > other.director
        
    def __eq__(self, other: "Film"):
        """
        This method is used to check if a Film is greater than or equal to (>=) another Film provided as a parameter (other). 
        To do this, it starts by comparing the directors based on lexicographical ordering. If there is a tie, it compares by the release year. 
        Finally, if there is another tie, it compares by the title of the Film, as it did with the director. This function returns a boolean value 
        depending on whether the Film calling the function (self) is greater than or equal to the other Film (returning True in this case and False otherwise).
        
        Parameters
        ----------
        other : "Film"
            The Film being compared to the Film used to call the function, wanting to know if the latter is greater than or equal to other.
        
        Returns
        -------
        boolean
            True if Film >= other, and False otherwise.
        """
        
        if self.director == other.director:
            return self.title == other.title
        else:
            return self.director == other.director
        
        
class Film_Manager():
    """
    Class responsible for managing Films to use their information.
    This class contains an ordered list of films, which will make up its catalog and will be used for various purposes.
    With them, the Film_Manager will be able to create a file with the non-repeated films and an interactive menu can be used
    through which the user can make personalized queries within the catalog.
    
    Usage Example:
        manager = Film_Manager() 
        data_film_list = manager.create_film(films_text)
        manager.pandas_stats(data_film_list)
        manager.user_menu()
    
    Attributes
    ----------
    Class Attributes: 
        film_list: list
            Ordered list containing a series of movies, Film objects, that will be handled by it and used in a catalog.
    
    Methods
    -------
    Public Methods:
        create_film(self, films_text) -> list
            This function creates Film objects from a given text document with the necessary information and is responsible for creating
            its attribute film_list, an ordered list of the movies in its catalog. Returns a list with the data of the movies, used subsequently
            for statistical purposes.
    
        user_menu(self) -> None:
            This function allows the user to make personalized queries through an interactive menu with three options: 1) to consult all the movies
            from the catalog, 2) to consult the movies of a specific director, and 3) to show the movies released in a year given by the user.
        
        pandas_stats(self, data_film_list: list) -> None:
            Calculates and prints statistics based on the movie data in the catalog: number of movies per director, average score per director, and per
            release year.
    
    Private Methods:
        
    Note
    -----
    """

    
    def __init__(self):
        self.film_list = LinkedOrderedPositionalList()
        self.film_unique_list = ArrayOrderedPositionalList()
        
    @property
    def film_list(self):
        """
        Gets the ordered list of the Films.
        Returns
        -------
        str
            The Film ordered list of the catalog.
        """
        return self._film_list

    @film_list.setter
    def film_list(self, value: list):
        """
        Set the ordered list of the Films.

        Parameters
        ----------
        value : str 
            The new ordered list of Films.

        Raises
        ------
        ValueError
            If the provided value is not an ordered list (LinkedOrderedPositionalList or ArrayOrderedPositionalList) of Film objects.
        """
        #or Array??????????????
        if isinstance(value, LinkedOrderedPositionalList) or isinstance(value, ArrayOrderedPositionalList):
            self._film_list = value
        else:
            raise ValueError("The film list must be a LinkedOrderedPositionalList or a ArrayOrderedPositionalList")
        for film in self._film_list:
            if not isinstance(film, "Film"):
                raise TypeError("Elements of film_list must be Films")
    @property
    def film_unique_list(self):
        """
        Gets the ordered list of the Films.
        Returns
        -------
        str
            The Film ordered list of the catalog.
        """
        return self._film_unique_list
    
    @film_unique_list.setter
    def film_unique_list(self, value: list):
        """
        Set the ordered list of the Films.
    
        Parameters
        ----------
        value : str 
            The new ordered list of Films.
    
        Raises
        ------
        ValueError
            If the provided value is not an ordered list (LinkedOrderedPositionalList or ArrayOrderedPositionalList) of Film objects.
        """
        #or Array??????????????
        if isinstance(value, LinkedOrderedPositionalList) or isinstance(value, ArrayOrderedPositionalList):
            self._film_unique_list = value
        else:
            raise ValueError("The film list must be a LinkedOrderedPositionalList or a ArrayOrderedPositionalList")
        for film in self._film_unique_list:
            if not isinstance(film, "Film"):
                raise TypeError("Elements of film_list must be Films")

    def create_film(self, films_text)->list:
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
            self.film_unique_list.add(film)
        print("[", end=" ")
        for x in self.film_list:
            print(x.print_film(), end="\n")
        print("]")
        return(data_film_list)
        
    def user_menu(self)->None:
        """
        This function prints an interface with three options that the user can choose from:
            - 1) Print the data of all the Films in the catalog, from film_list
            - 2) Print the data of the Films by a certain author introduced by the user
            - 3) Print the data of the Films released in a year introduced by the user
        If the option value is other, the function ends and "Exiting..." is printed. If the author entered is not a string, the user is prompted
        to enter a valid name. If the author returns no movies, it is indicated that none are found in the catalog or it's also possible that the format is not met: first a valid last name, then a valid first name.
        On the other hand, if the year entered in option 3 is not a number and cannot be converted to an integer, it goes from the try block to the except block, where it indicates that a valid year should be entered.
        If the counter, which starts at 0, doesn't change when iterating through film_list and searching for that year or author, it means that no movies in the catalog were released in that year or was filmmed by that author.
        If film_list is empty, it exits the menu and ends the function execution.
        In each of the options, to print the movies, the ordered list film_list is traversed by the film_list iterator and if the condition is met (except for the first case, where all are printed), the print_film() 
        function of the Film is called to display its data.
                
        Returns
        -------
        None
        """

        try:
           option = int(input("Choose one of the following options: \n 1) All platform movies \n 2) Movies directed by a director \n 3) Movies released in a year\n - Press any other key to exit\n"))
           while option in (1,2,3) and len(self.film_list)>0:
               iterador = self.film_list.__iter__()
               if option == 1:
                   for i in range(len(self.film_list)):
                       print(next(iterador).print_film())

               elif option == 2:
                    author_ln = input("Enter the director's last name for the movies you want to consult\n")
                    author_fn = input("Enter the director's first name for the movies you want to consult\n")
                    cnt = 0
                    if author_ln.isalpha() and author_fn.isalpha():
                        for i in range(len(self.film_list)):
                            f = next(iterador)
                            if f.director == f"{author_ln}, {author_fn}":
                                print(f.print_film())
                                cnt+=1
                        if cnt == 0:
                            print(f"No movies directed by {author_ln}, {author_fn} are found in the catalog, or incorrect format: (Last Name, First Name)")
                    else:
                        print("Please enter a valid name")
                        
               elif option == 3:
                   year = input("Enter the release year of the movies you want to consult: \n")             
                   try:
                        cnt = 0
                        for i in range(len(self.film_list)):
                            f = next(iterador)
                            if f.release_year == int(year):
                                print(f.print_film())
                                cnt+=1
                            
                        if cnt == 0:
                            print(f"No movie in the catalog was released in the year {year}")
                   except:
                        print("Please enter a valid year")

               option = int(input("\nChoose one of the following options: \n 1) All platform movies \n 2) Movies directed by a director \n 3) Movies released in a year\n - Press any other key to exit\n"))
             
           if len(self.film_list) == 0:
               print("The film catalog is empty")
           else:
               print("Exiting...")

           
        except:
            print("Exiting...")
    
    def file_writer(self):
        
        print("[", end=" ")
        for x in self.film_unique_list:
            print(x.print_film(), end="\n")
        print("]")
        marker = self.film_unique_list.first()
        
        while marker != self.film_unique_list.last(): 
            
            marker_after = self.film_unique_list.after(marker)
            film_1 = self.film_unique_list.get_element(marker)
            film_2 = self.film_unique_list.get_element(marker_after)
            print(film_1.print_film())
            print(film_2.print_film())
            print('\n')
            if film_1 == film_2:
                print('film_1 igual a film_2')
                if film_1.release_year <= film_2.release_year: 
                    self.film_unique_list.delete(marker)
                else: 
                    self.film_unique_list.delete(marker_after)
                    marker_after = marker
            else: 
                marker = marker_after
                        
                        
        print("[", end=" ")
        for x in self.film_unique_list:
            print(x.print_film(), end="\n")
        print("]")
        

        # Nombre del archivo
        nombre_archivo = "unique_films_file.txt"

        with open(nombre_archivo, "w") as archivo:
            # Escribe el contenido en el archivo 
            for film in self.film_unique_list:
                archivo.write(film.print_film())
                archivo.write('\n')
      
      
    def pandas_stats(self, data_film_list:list)->None:
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
        manager.file_writer()
        manager.pandas_stats(data_film_list)
        manager.user_menu()


if __name__ == '__main__':
    main()
