
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
        print_film(self) -> str:
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
            
    def print_film(self):
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
            Ordered list that starts out equal to film_list but then becomes an ordered list without duplicates through the _delete_duplicated function.
            
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
            This function creates Film objects from a given text document with the necessary information and is responsible for adding the read movies to each of the lists 
            film_list, an ordered list of the movies in its catalog, and film_unique_list. Returns a list with the data of the unique movies, used subsequently
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
                An ordered list that starts out identical to film_list but later, through the _delete_duplicated function, becomes an ordered list without duplicates.
    
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
 
    @film_list.setter
    def film_list(self, value: Union[LinkedOrderedPositionalList, ArrayOrderedPositionalList]):
        """
        Set the ordered list of the Films.
 
        Parameters
        ----------
        value : Union[LinkedOrderedPositionalList, ArrayOrderedPositionalList]
            The new ordered list of Films.
 
        Raises
        ------
        ValueError
            If the provided value is not an ordered list (LinkedOrderedPositionalList or ArrayOrderedPositionalList) of Film objects.
        """
        if isinstance(value, LinkedOrderedPositionalList) or isinstance(value, ArrayOrderedPositionalList):
            self._film_list = value
        else:
            raise ValueError("The film list must be a LinkedOrderedPositionalList or a ArrayOrderedPositionalList")
        for film in self._film_list:
            if not isinstance(film, Film):
                raise TypeError("Elements of film_list must be Films")
    @property
    def film_unique_list(self):
        """
        Gets the ordered list of unique Films.
        
        Returns
        -------
            The Film ordered list of the catalog without duplicates.
            
        """
        return self._film_unique_list
    
    @film_unique_list.setter
    def film_unique_list(self, value: Union[LinkedOrderedPositionalList, ArrayOrderedPositionalList]):
        """
        Set the ordered list of the unique Films.
        
        Parameters
        ----------
        value : Union[LinkedOrderedPositionalList, ArrayOrderedPositionalList]
        
            The new ordered list of unique Films.
            
        Raises
        ------
        ValueError
            If the provided value is not an ordered list (LinkedOrderedPositionalList or ArrayOrderedPositionalList) of Film objects.
        """

        if isinstance(value, LinkedOrderedPositionalList) or isinstance(value, ArrayOrderedPositionalList):
            self._film_unique_list = value
        else:
            raise ValueError("The film list must be a LinkedOrderedPositionalList or a ArrayOrderedPositionalList")
        for film in self._film_unique_list:
            if not isinstance(film, Film):
                raise TypeError("Elements of film_list must be Films")
 
    def _create_film(self, films_text:str )-> list:
        """
        This function creates Film objects from a given text document with the necessary information and is responsible for adding the read movies to each of the lists: film_list and film_unique_list. 
        Returns a list with the data of the movies, used subsequently for statistical purposes.
        
        Method Characteristics:
            - Instances of the Film class are created using the attributes provided in the films_text.
            - These instances are added to each of the lists.
            - film_unique_list starts with the same content as film_list, but then the _delete_duplicated() method is called to remove duplicate movies from it.
    
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
            self.film_unique_list.add(film)

        data_film_list = self._delete_duplicated()
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
           option = int(input("\n***   FILM CATALOG MENU   ***\nChoose one of the following options: \n 1) Introducir un catálogo \n   2) Consult all platform movies \n   3) Consult movies directed by an author \n   4) Consult movies released in a year\n 5) Create a file with the movies containing no duplicates \n 6) Show stats of the catalog \n  - Press any other key to exit\n"))
           while option in (1,2,3,4,5,6): #len(self.film_list)>0
               if len(self.film_list) == 0 and option in (2,3,4,5,6):
                   print("\nPlease, enter the catalog data")
                   option = int(input("\n***   FILM CATALOG MENU   ***\nChoose one of the following options: \n 1) Introducir un catálogo \n   2) Consult all platform movies \n   3) Consult movies directed by an author \n   4) Consult movies released in a year\n 5) Create a file with the movies containing no duplicates \n 6) Show stats of the catalog \n  - Press any other key to exit\n"))
                   continue
               iterador = self.film_list.__iter__()
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
                    for i in range(len(self.film_list)):
                        print(next(iterador).print_film())
 
               elif option == 3:
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
                            print(f"\nNo movies directed by {author_ln}, {author_fn} are found in the catalog, or incorrect format: (Last Name, First Name)")
                    else:
                        print("\nPlease enter a valid name")
 
                        
               elif option == 4:
                    year = input("Enter the release year of the movies you want to consult: \n\n")             
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
        Elimina de la lista ordenada film_unique_list las peliculas repetidas. 
                
        Method Characteristics:
            - De la film_unique_list que inicialmente es una lista ordenada con todas las peliculas (como una copia de la film_list) eliminamos los duplicados
            - Se considera que dos peliculas SON IGUALES cuando sus directores y titulos son los mismos (Esto se define en el metodo __eq__() de Film). Con respecto a el año de lanzamiento, no tienen que ser los mismos. Se escogera la de año mas reciente y el resto se eliminara. 
            - Para llevar a cabo esta comparacion de peliculas utilizamos un marker (que hace referencia al nodo en la lista) y comienza siendo la posicion del primer elemento, asi cada elemento de la lista se compara con el siguiente (marker_after) y si son iguales se procede eliminando uno de los dos con el metodo delete(). Esto se ejecuta hasta llegar al antepenultimo elemento.
                   
        Returns:
        --------
        list 
            Lista con las peliculas del catalogo ordenadas y sin repetidos, usando esta lista se calcularan las estadisticas. 
            
        Note:
        -----
        - Cuando se elimina un elemento de la lista, el nodo correspondiente se borra de la memoria, por lo tanto es necesario que El marcador (marker), se actualize para apuntar al siguiente nodo después de la eliminación.
        - Cuando los elementos comparados (film_1 y film_2) son iguales, el marker permanece en su posición actual si se elimina marker_after, o avanza al siguiente nodo si se elimina marker. Cuando los elementos comparados son distintos, el marker debe es actualizadp para avanzar al siguiente nodo en la lista. 
        """
        """
        Removes duplicate movies from the ordered list film_unique_list. 
                    
        Method Characteristics:
            - From film_unique_list, which initially is an ordered list with all the movies (as a copy of film_list), we remove the duplicates.
            - Two movies are considered EQUAL when their directors and titles are the same (This is defined in the __eq__() method of Film). Regarding the release year, they do not have to be the same. The most recent year will be chosen, and the rest will be deleted. 
            - To carry out this comparison of movies, we use a marker (which refers to the node in the list) and starts being the position of the first element, so each element of the list is compared with the next one (marker_after), and if they are equal, one of the two is deleted using the delete() method. This is executed until reaching the penultimate element.
                       
        Returns:
        --------
        list 
            A list with the movies from the catalog ordered and without duplicates, using this list the statistics will be calculated. 
                
        Note:
        -----
        - When an element of the list is deleted, the corresponding node is removed from memory, therefore it is necessary for the marker to be updated to point to the next node after deletion.
        - When the compared elements (film_1 and film_2) are equal, the marker remains in its current position if marker_after is deleted, or it moves to the next node if marker is deleted. When the compared elements are different, the marker must be updated to move to the next node in the list. 
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
                archivo.write(film.print_film())
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
