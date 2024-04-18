
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 23:42:43 2024
 
@author: isabe
"""
 
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
        _file_writer(self) -> None:
            Crea y escribe en un nuevo fichero las peliculas ordenadas, sin repetidos.
        
    Note
    -----
    """
 
    
    def __init__(self):
        self.film_list = LinkedOrderedPositionalList()
        self.film_unique_list = LinkedOrderedPositionalList()
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
                           data_film_list = self.create_film(films_text)
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
                   self.pandas_stats(data_film_list)
               option = int(input("\n***   FILM CATALOG MENU   ***\nChoose one of the following options: \n 1) Introducir un catálogo \n   2) Consult all platform movies \n   3) Consult movies directed by an author \n   4) Consukt movies released in a year\n 5) Create a file with the movies containing no duplicates \n 6) Show stats of the catalog \n  - Press any other key to exit\n"))
 
           
        except:
            print("Exiting...")
    
    def _delete_duplicated(self) -> list :
        #marcador empieza siendo la posicion del primer elemento
        data_film_list = []
        marker = self.film_unique_list.first()
        while marker != self.film_unique_list.last(): # no tiene sentido hablar del marcador de despues del ultimo marcador. Y este nunca estara repetido (siendo marker) ya que es una lista ordenada
            marker_before = marker #definimos el marker_before como marker, usado para que al momento de elminarlo aun conservar el marker incial 
            marker_after = self.film_unique_list.after(marker) #marcador usado para la comparacion, es la posicion del siguiente elemento
            #obtenemos los elementos film en la posiciones del marcador y la siguiente
            film_1 = self.film_unique_list.get_element(marker)
            film_2 = self.film_unique_list.get_element(marker_after)
            #recordemos que el metodo __eq__ en film me devuelve true si EL DIRECTOR Y EL NOMBRE de la pelicula son el mismo
            if film_1 == film_2:
                #dejamos la pelicula con fecha de lanzamiento mas reciente
                if film_1.release_year <= film_2.release_year: 
                    self.film_unique_list.delete(marker_before) #eliminamos el marker_before que es una copia del original, que no podemos eliminar porque entonces ya seria None y las siguientes iteraciones no serian validas 
                    marker =self.film_unique_list.before(marker_after) #el marker original cambia (el cual es borrado mediante su copia) cambia y se convierte en el marker de antes del marker_after 
                else: 
                    self.film_unique_list.delete(marker_after)
                    marker = self.film_unique_list.after(marker) #ahora el marker sera el siguiente (el de despues del que ha sido eliminado)
            #si film_1 y film_2 son iguales sigue con el mismo marker (si se elimina el marker_after, este pasaria a ser el siguiente(o sea al marker_after_after)), o con el siguiente (si se elimina el marker). (Para una explicacion mas detallada vease la nota de la documentacion) 
            #Notese que hay que hacerlo manuelmente cuando film_1 y film_2 son distintos porque no se elimina ninguno y este cambio de marker interno no ocurre. 
            else: 
                marker = marker_after
                
        iterator = self.film_unique_list.__iter__()
        for i in range(len(self.film_unique_list)):
            film = next(iterator)
            data_film_list.append([film.director, film.title, film.release_year, film.score])
        return data_film_list
            
        
    def _file_writer(self) -> None:
        
        """Crea y escribe en un nuevo fichero con las peliculas ordenadas, sin repetidos. 
                
        Method Characteristics:
            - De la film_unique_list que inicialmente es una lista ordenada con todas las peliculas (como una copia de la film_list) eliminamos los duplicados
            - Se considera que dos peliculas SON IGUALES cuando sus directores y titulos son los mismos (Esto se define en el metodo __eq__() de Film). Con respecto a el año de lanzamiento, no tienen que ser los mismos. Se escogera la de año mas reciente y el resto se eliminara. 
            - Para llevar a cabo esta comparacion de peliculas utilizamos un marker (que hace referencia al nodo en la lista) y comienza siendo la posicion del primer elemento, asi cada elemento de la lista se compara con el siguiente (marker_after) y si son iguales se procede eliminando uno de los dos con el metodo delete(). Esto se ejecuta hasta llegar al antepenultimo elemento.
            - Se crea un archivo txt con un nombre fijo 'unique_films_file.txt' y alli se almacenan todas las peliculas que quedan en la film_unique_list. 
            - Este metodo es llamado internamente por la funcion user_menu() y ejecuta una de las opciones del menu. 
                   
        Returns:
        --------
        None.
                
        Note:
        -----
        - Cuando se elimina un elemento de la lista, el nodo correspondiente se borra de la memoria, pero los nodos adyacentes siguen conectados entre sí. El marcador (marker), se actualiza para apuntar al siguiente nodo después de la eliminación. Esto significa que no es necesario ajustar manualmente el marcador después de eliminar un elemento de la lista; la actualización ocurre automáticamente gracias a la implementación del método delete(). 
        - Cuando los elementos comparados (film_1 y film_2) son iguales, el marker permanece en su posición actual si se elimina marker_after, o avanza al siguiente nodo si se elimina marker. Sin embargo, cuando los elementos comparados son distintos, el marker debe ser actualizado manualmente para avanzar al siguiente nodo en la lista, ya que no hay eliminación que provoque la actualización automática del marcador.
        """
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
 
    manager = Film_Manager()
    manager.user_menu()
 
 
if __name__ == '__main__':
    main()
