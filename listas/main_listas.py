# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 23:42:43 2024
 
@author: isabe
"""
 
from array_ordered_positional_list import ArrayOrderedPositionalList
from linked_ordered_positional_list import LinkedOrderedPositionalList 
from typing import Union 
import pandas
 
 
class Film:
    """
    Class representing a Film object, in the implementation these will be stored by an Ordered Positional List.
    
    This class contains methods to manipulate the data of a film: the director, the title, the release year, and the score.
    The class allows comparison of films. These methods are crucial for organizing lists and later, removing duplicate films from one of the lists.

    Attributes
    ----------
    director : str
        The name of the film's director (last name, first name).
    title : str
        The title of the film.
    release_year : int
        The release year of the film.
    score : float
        The average score of the film.

    Methods
    -------
    Public methods: 
        __str__(self) -> str:
            Returns a string containing the concatenated information of the film (each attribute separated by ';').
    
    Dunder methods:
        __ge__(self, other: Film) -> bool:
            Compares if the current film is greater than or equal to another film starting by comparing the director, then the release year, and finally the title.
        
        __gt__(self, other: Film) -> bool:
            Compares if the current film is greater than another film starting by comparing the director, then the release year, and finally the title.
        
        __eq__(self, other: Film) -> bool:
            Compares if the current film is equal to another film based on the director and the title.
    """


    
    def __init__(self, director: str, title: str, release_year: int, score: float):
        """
        Creates a Film with the given attributes.

        Parameters
        ----------
        director : str
            The name of the film's director (last name, first name).
        title : str
            The title of the film.
        release_year : int
            The release year of the film.
        score : float
            The average score of the film.

        Returns
        -------
        None.
        """
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
            The director's name (last name and first name (in that order and separated by comma)) of the movie.
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
            If the provided value is not a non-empty string.
        """
        if isinstance(value, str) and len(value) != 0 :
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
            If the provided value is not a non-empty string.
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
            The new released year of the film.
 
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
            
    def __str__(self):
        """
        Function that returns a string with the information of the Film, which is used to examine the data of a movie 
        outside the class.
        
        Returns
        -------
        str
            String containing the data (atributes) of the Film (director; title; release year; score).
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
        This method is used to check if a Film is equal to (==) another Film provided as a parameter (other). 
        To do this, it starts by comparing the directors based on lexicographical ordering. If they are equal, it proceeds to compare the title of the film.
        Thus, two films are considered equal if both their director and title are the same (without considering the release year, as the comparison of these for equal films will be carried out during the removal of duplicates).
        This function returns a boolean value depending on whether the Film calling the function (self) is equal to the other Film (returning True in this case and False otherwise).
        Parameters
        ----------
        other : "Film"
            The Film being compared to the Film used to call the function, wanting to know if the latter is equal to other.
        Returns
        -------
        boolean
            True if Film == other, and False otherwise.
        """
        if self.director == other.director:
            return self.title == other.title
        else:
            return self.director == other.director

class Film_Manager:
    """
    Class responsible for managing Films to use their information.
    
    This class contains an ordered list of films, which will make up its catalog and will be used for various purposes.
    With them, the Film_Manager will be able to create an interactive menu with multiple options such as: 
        - Enter a catalog/file of movies for management (mandatory in order to access the remaining options)
        - Query all movies, movies directed by a specific director, movies released in a specific year (all of these will be done using to the ordered list with duplicates)
        - Create a new txt file with the ordered and unique movies. 
        - Show statistics about the catalog (Taken from the list without duplicates)
    through which the user can make personalized queries within the catalog.
    
    Usage Example:
        manager = Film_Manager()
        manager.user_menu()
        
    Attributes
    ----------
    Class Attributes: 
        
        film_list: LinkedOrderedPositionalList or ArrayOrderedPositionalList
            Ordered list containing a series of movies, Film objects, that will be handled by it and used in a catalog.
        film_unique_list: LinkedOrderedPositionalList or ArrayOrderedPositionalList
            Ordered list that becomes an ordered list without duplicates through the _delete_duplicated function.
            
    Both implementations (array_ordered_positional_list and linked_ordered_positional_list) can be used for both lists, obtaining equivalent results. 
    
    Methods
    -------
    Public Methods:
        user_menu(self) -> None:
            This function allows the user to make personalized queries through an interactive menu with six options: 
                1) Enter a catalog (mandatory to continue) 
                2) Consult all the movies from the catalog
                3) Consult the movies of a specific director
                4) Show the movies released in a year given by the user.
                5) Create a file with the movies containing no duplicates 
                6) Show stats of the catalog 
            from option 2 to 4, the ordered list WITH duplicates is used, in 5 and 6 the list WITHOUT DUPLICATES is used. 

    Private Methods: 
        _create_film(self, films_text:str )-> list:
            This function creates Film objects from a given text document with the necessary information and is responsible for adding the read movies to the list
            film_list, an ordered list of the movies in its catalog. Returns a list with the data of the unique movies, used subsequently
            for statistical purposes.
            
        _delete_duplicated(self) -> list :
            Removes duplicated movies from the ordered list film_unique_list. Returns a list with the data of the unique movies, which is passed to the _create_film function used subsequently
            for statistical purposes.
            
        _file_writer(self) -> None:
            Writes in a new file ("unique_films_file.txt") the ordered movies, without duplicates.
        
        _pandas_stats(self, data_film_list: list) -> None:
            Calculates and prints statistics based on the movie data (WITHOUT DUPLICATES) in the catalog: number of movies per director, average score per director, and average score per
            release year.
        
    Note
    -----
    To start the program execution, only the user_menu method needs to be called, the other methods are called internally. 
    """

    def __init__(self):
        """
        Defines the class attributes, which are the two lists to be used in the implementation.
        
        Class Attributes: 
        -----------------
            film_list: LinkedOrderedPositionalList or ArrayOrderedPositionalList
                An ordered list containing a series of movies, Film objects, that will be handled by the class and used in a catalog.
            film_unique_list: LinkedOrderedPositionalList or ArrayOrderedPositionalList
                An ordered list that starts being empty and through the _delete_duplicated function, becomes an ordered list without duplicates.
    
        Returns
        -------
        None.
        """
        self._film_list = LinkedOrderedPositionalList() #Or ArrayOrderedPositionalList()
        self._film_unique_list = LinkedOrderedPositionalList() #Or ArrayOrderedPositionalList()
        
    @property
    def film_list(self):
        """
        Gets the ordered list of the Films.
        
        Returns
        -------
        LinkedOrderedPositionalList() #or ArrayOrderedPositionalList(): 
            The Film ordered list of the catalog.
        """
        return self._film_list

    @property
    def film_unique_list(self):
        """
        Gets the ordered list of unique Films.
        
        Returns
        -------
            The Film ordered list of the catalog without duplicates.
            
        """
        return self._film_unique_list
    

 
    def _create_film(self, films_text:str )-> list:
        """
        This function creates Film objects from a given text document with the necessary information and is responsible for adding the read movies to the list film_list. 
        Returns a list with the data of the movies, used subsequently for statistical purposes.
        
        Method Characteristics:
            - Instances of the Film class are created using the attributes provided in the films_text.
            - These instances are added to each of the lists.
            - film_unique_list starts being empty, but then the _delete_duplicated() method is called to remove duplicate movies from it.
    
        Parameters
        ----------
        films_text : str
            Text with the information of the movies.
            Each movie in the films_text must be on a separate line, and each of its attributes separated by a semicolon (;).
    
        Returns
        -------
        list
            A list with the movies from the catalog ordered and without duplicates, using this list the statistics will be calculated. 
            This list is created and returned by the _delete_duplicated() method.
            
        Note
        -----
        Called by the user_menu function for the proper execution of option 1.
        """
        films = films_text.split("\n")
        
        for line in films:
            film_info = line.split('; ')
            director, title, release_year, score = film_info
            film = Film(director, title, int(release_year), float(score))
            self.film_list.add(film)

        data_film_list = self._delete_duplicated()
        return(data_film_list)
    
    def user_menu(self) -> None:
        """
        This function prints an interface with six options that the user can choose from:
            - 1) Enter the name of a file with a catalog of films to be read 
            - 2) Print the data of all the Films in the catalog, from film_list
            - 3) Print the data of the Films by a certain author introduced by the user
            - 4) Print the data of the Films released in a year introduced by the user
            - 5) Create a file that contains the non-duplicated movies 
            - 6) Print some stats of the catalog

        The menu will continuously appear until a character other than (1,2,3,4,5,6) is entered. If another number is entered, the while loop will exit, and if it's another character, an exception is handled 
        because the user input is converted to an integer, in these cases the function ends and "Exiting..." is printed. To choose an option different than 1, a warning will appear: it is necessary to enter 
        data in order to work with them, and until data is entered or the menu is exited, it will continue appearing. When option 1 is selected (necessary to start), the catalog of movies will be created using 
        the filename entered by the user, this file will be opened and the create_film() function will be called to fill the film_list attribute of the Film_Manager and return the data_film_list with information 
        about them, used in option 6. If it is not possible to access the file or the file does not exist, it goes from the previous try part to the exception, indicating that the file must be valid in the directory.
        From this point on, we can use the other options. Options 2, 3, and 4 iterate through film_list, the first printing all the movies in the catalog. Option 3 asks for a last name and first name of the author to 
        search for them in the catalog and return the movies that correspond to them (none if the author is not found in the catalog or the format is not valid), it also checks that they are valid characters. Option 4 asks 
        for a year, converting it to an integer (this makes if the user does not enter the character of a number an exception occurs, using a try-except so that when this happens a warning appears indicating that a number must 
        be entered), if the counter is 0 it means that no movie was released in that year. These last three options use the iterator (__iter__) of the list to iterate through it. Option 5 calls the private method _file_writer() 
        to create the corresponding file without duplicates. Finally, option 6 allows printing statistical data from the catalog by calling the pandas_stats() function, and passing data_film_list as a parameter.
        
        Returns
        -------
        None
        """

        try:
           option = int(input("\n***   FILM CATALOG MENU   ***\nChoose one of the following options: \n 1) Introducir un catálogo \n   2) Consult all platform movies \n   3) Consult movies directed by an author \n   4) Consult movies released in a year\n 5) Create a file with the movies containing no duplicates \n 6) Show stats of the catalog \n  - Press any other key to exit\n"))
           while option in (1,2,3,4,5,6): #len(self.film_list)>0
               if len(self.film_list) == 0 and option in (2,3,4,5,6):
                   print("\nPlease, enter the catalog data")
                   option = int(input("\n***   FILM CATALOG MENU   ***\nChoose one of the following options: \n 1) Introducir un catálogo \n   2) Consult all platform movies \n   3) Consult movies directed by an author \n   4) Consult movies released in a year\n 5) Create a file with the movies containing no duplicates \n 6) Show stats of the catalog \n  - Press any other key to exit\n"))
                   continue
               if option == 1:
                   try: 
                       film_catalog = input("Enter the name of the file containing the film catalog: \n")
                       with open(film_catalog, encoding="utf-8") as f:
                            # With strip(), we ensure that there are no additional spaces, tabs, or newline characters present in the file.
                           films_text = f.read().strip()
                           data_film_list = self._create_film(films_text)
                   except:
                       print("\nPlease enter the name of 6a valid file in your directory")
               elif option == 2:
                    for film in self.film_list:
                        print(film)
 
               elif option == 3:
                    author_ln = input("Enter the director's last name for the movies you want to consult\n")
                    author_fn = input("Enter the director's first name for the movies you want to consult\n")
                    cnt = 0
                    if author_ln.isalpha() and author_fn.isalpha():
                        for film in self.film_list:
                            if film.director == f"{author_ln}, {author_fn}":
                                print(film)
                                cnt+=1
                        if cnt == 0:
                            print(f"\nNo movies directed by {author_ln}, {author_fn} are found in the catalog, or incorrect format: (Last Name, First Name)")
                    else:
                        print("\nPlease enter a valid name")
 
                        
               elif option == 4:
                    year = input("Enter the release year of the movies you want to consult: \n\n")             
                    try:
                         cnt = 0
                         for film in self.film_list:
                             if film.release_year == int(year):
                                 print(film)
                                 cnt+=1
                         if cnt == 0:
                             print(f"No movie in the catalog was released in the year {year}")
                    except:
                         print("Please enter a valid year")
 
               elif option == 5:
                    self._file_writer()
                    print("A file named 'unique_films_file.txt' has been created in your directory")
 
               elif option == 6:
                   self._pandas_stats(data_film_list)
               option = int(input("\n***   FILM CATALOG MENU   ***\nChoose one of the following options: \n 1) Introducir un catálogo \n   2) Consult all platform movies \n   3) Consult movies directed by an author \n   4) Consukt movies released in a year\n 5) Create a file with the movies containing no duplicates \n 6) Show stats of the catalog \n  - Press any other key to exit\n"))
 
           
        except:
            print("Exiting...")

    def _delete_duplicated(self) -> list :
        """
        This function adds the movies from film_list to the ordered list film_unique_list, ensuring there are no duplicates. To do this, it iterates through the movies in film_list. At the beginning, 
        film_unique_list is empty, so it adds the first Film from film_list to it. In the following iterations, the function stores a marker with the positions of film_unique_list, traversing it and changing 
        the position to the next one to match other_film (the Film from film_unique_list), aiming to ensure that the Film from the iteration (from film_list) doesn't have duplicates in film_unique_list. The 
        duplicated value starts as False, and if any movie in film_unique_list is found to be equal to the Film, it becomes True. If this happens, it checks the release years of the movies, and if the release year 
        is greater in the Film from film_list, it replaces the other film (other_film) in film_unique_list with Film at the marker position stored by the function. If there are no duplicates, the Film is added to 
        film_unique_list. Finally, it traverses film_unique_list to store the movie data in the data_film_list, which will be used later for statistical data. It returns this list.
             
        Returns:
        --------
        list 
            A list with the movies from the catalog ordered and without duplicates, using this list the statistics will be calculated. 
                
        Note:
        -----

        """
        # The marker starts as the position of the first element
        data_film_list = []  
        for film in self.film_list:
            if self.film_unique_list.is_empty():
                self.film_unique_list.add(film)
            else: 
                marker = self.film_unique_list.first()
                duplicated = False
                for other_film in self.film_unique_list:
                    if other_film == film:
                        duplicated = True
                        if other_film.release_year < film.release_year:
                            self.film_unique_list.replace(marker, film)
                    marker = self.film_unique_list.after(marker)
                    
                if not duplicated:
                     self.film_unique_list.add(film)
                            
        for film in self.film_unique_list:
            data_film_list.append([film.director, film.title, film.release_year, film.score])
        return data_film_list
    
        
    def _file_writer(self) -> None:
        
        """
        Writes to a new file ("unique_films_file.txt") the ordered movies, without duplicates. 
                    
        Method Characteristics:
            - Starting from the already ordered and duplicate-free film_unique_list:
            - A txt file is created with a fixed name 'unique_films_file.txt', and there all the movies remaining in the film_unique_list are stored. 
            - This file is written with the same syntax as the original movie catalog (film_text).
                
        Returns:
        --------
        None
                    
        Note:
        -----
        This method is called internally by the user_menu() function and executes option 5 of the menu.
        """
        
        nombre_archivo = "unique_films_file.txt"
    
        with open(nombre_archivo, "w") as archivo: 
            for film in self.film_unique_list:
                archivo.write(str(film))
                archivo.write('\n')

    def _pandas_stats(self, data_film_list:list) -> None:
        """
        Calculates and prints statistics based on the movie data in the catalog: 
                
                - Number of movies per director.
                - Average score per director.
                - Average score per release year. 
            
            Parameters
            ----------
            data_film_list : list
                List with the ordered and duplicate-free Film objects from the catalog.
    
            Returns
            -------
            None
                The metrics are printed on the screen.
        """
        data = pandas.DataFrame(data_film_list, columns=["Director", "Films", "Release year", "Score"])
        
        #Number of movies per director (counter).
        group_col = "Director"
        target_col = "Films"
        single_stats = data.groupby(group_col).agg({target_col: ["count"]})
        print('\n', "*"*37, '\n', "          Number of films     ", '\n',  "*"*37)
        print(single_stats, "\n")
        #Average score per director.
        group_col = "Director"
        target_col = "Score"
        single_stats = data.groupby(group_col).agg({target_col: ["mean"]})
        print('\n', "*"*37, '\n', "      Mean score for director   ", '\n',  "*"*37)
        print(single_stats, "\n")
        #Average score per release year.
        group_col = "Release year"
        target_col = "Score"
        single_stats = data.groupby(group_col).agg({target_col: ["mean"]})
        print('\n', "*"*37, '\n', "    Mean score for release year ", '\n',  "*"*37)
        print(single_stats, "\n")

def main():
    """
    The main function that reads from a file and starts the simulation.
    """
    manager = Film_Manager()
    manager.user_menu()
 
 
if __name__ == '__main__':
    main()
