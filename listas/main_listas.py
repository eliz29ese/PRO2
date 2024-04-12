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
        
        if self.author == other.author:
            if self.release_year == other.release_year:
                return self.title >= other.title
            else:
                return self.release_year >= other.release_year
        else:
            return self.author >= other.author
    
