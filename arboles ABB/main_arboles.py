# -*- coding: utf-8 -*-
"""
Santrich Escalona, Elizabet
(elizabet.santrich.escalona@udc.es)
Rodríguez Polín, Isabel
(isabel.rodriguezp@udc.es)
"""
from avl_tree import AVL
from courses import Course
import pandas
    
class CursesManager():
    """
    La función de esta clase es manejar un catálogo de cursos haciedno uso de los árboles AVL para almacearlos y poder acceder a ellos de forma eficiente. Cuenta 
    con 4 árboles AVL: tree_A, tree_B, tree_add y tree_common que guardan respectivamente los cursos de la academia A, los de la academia B, la unión de ambas ofertas
    y la oferta común. Mediante esta clase el usuario puede acceder a la información disponible mediante un menú, que mostrará las siguientes opciones:
        - 1) Añadir los cursos de las dos academias
        - 2) Mostrar la unión de las ofertas
        - 3) Mostrar la oferta común
         -4) Mostrar las estadísticas del árbol deseado
    
    Usage Example:
        manager = Course_Manager()
        manager.user_menu()
        
    Attributes
    ----------
    Class Attributes: 
        
        tree_A: AVL
            AVL que almacena los cursos de la academia A, que serán introducidos por el usuario.
        tree_B: AVL
            AVL que almacena los cursos de la academia B, que serán introducidos por el usuario.
        tree_add: AVL
            AVL que almacena la unión de los cursos de ambas academias, quedándose con los de mayor beneficio en caso de que tengan el mismo nombre, idioma y nivel en ambas academias.
        tree_common: AVL
            AVL que almacena los cursos comunes de ambas academias (mismo nombre, nivel e idioma) quedándose con el de mayor beneficio.
        
            
    Methods
    -------
    Public Methods:
        user_menu(self) -> None:
            Esta función permite al usuario elegir la acción que quiere realizar entre las siguientes:
                - 1) Añadir el catálogo de los cursos de ambas academias (necesario para las siguientes opciones)              
                - 2) Oferta agregada
                - 3) Oferta común
                - 4) Mostrar estadísticas, eligiendo el árbol del que el usuario quiere consultar información         

    Private Methods: 
         _get_menu_option(self) -> int:
             Muestra las opciones del menú y devuelve la opción elegida por el usuario.
             
        __read_courses(self)-> None:
            Se encarga de pedirle al usuario que introduzca el nombre del fichero de texto que incluye el catálogo de los cursos primero de la academia A y después de la B. Después llama al
            método create_course_catalog() para cear el catálogo de cada academia, pasándole el nombre del fichero y el árbol correspondiente (tree_A y tree_B respectivamente).
                               
        _create_course_catalog(self, cursos_file: str, tree: AVL) -> None:
            Lee el fichero del nombre dado y lo divide en líneas. Cada línea es un curso, y cada curso tiene sus atributos separados por "," : name, duration, students, level, language y price.
            Introduce cada curso en el árbol correspondienet del CourseMananager.
            
       _union_courses(self, course_A:Course, course_B:Course) -> Course:
            Dados dos cursos iguales (con la misma clave: nombre, idioma, nivel) de ambas academias devuelve aquek que tenga un mayor beneficio.
            
         _find_name(self, p, name:str, cnt:int) -> int:
             Dado un nombre de un curso, recorre el árbol de la academia A (tree_A) empezando por la posición p buscando si existe algún curso de esta que se encuentre en tree_add y que tenga ese 
             mismo nombre. El motivo de esto es añadirle al nombre de este curso que está en tree_add el string " A" al final para poder distinguirlo del del curso B.
       
        _added_offer(self) -> None:
            Recorre tree_A añadiendo sus cursos a tree_add para conseguir la oferta agregada, comprobando que no exista otro curso con la misma clave [nombre, nivel, idioma] en tree_B.
            Si esto ocurre se llama al método union_course(). Después se recorre tree_B para añadir sus cursos, distinguiéndolos de los de la academia B si tiene su mismo nombre añadiendole
            un distintivo en el nombre.
            
        _common_offer(self) -> None:
           Encuentra los cursos que tienen en común ambos cursos quedándose con el de mayor beneficio y añadiéndolos a tree_common para conseguir la oferta común.
            
         _show_stadistics(self) -> None:
             Muestra un menú para elegir el árbol del que queremos mostrar las estadísticas con pandas_stats()
             
          _pandas_stats(self, tree:AVL) -> None:
            Se encarga de mostar la información estadística (media de estudiantes por idioma y por nivel e ingresos totales) del árbol introducido.
             
                   
            
    """
    
    def __init__(self):
        """
        Defines the class attributes, which are cuatro árboles que almacenan cursos.
        
        Class Attributes: 
        -----------------
            tree_A: AVL
                Árbol con los cursos de la academia A (comienza siendo vacío)
            tree_B: AVL
                Árbol con los cursos de la academia B (comienza siendo vacío)
            tree_add: AVL
                Árbol con los cursos de la unión de las academias A y B (comienza siendo vacío)
            tree_common: AVL
                Árbol con los cursos de los cursos comunes de las academias A y B (comienza siendo vacío)
           
        Returns
        -------
        None.
        """
        
        self._tree_A = AVL()
        self._tree_B= AVL()
        self._tree_add = AVL()
        self._tree_common = AVL()
        
    @property
    def tree_A(self):
        """
        Gets the AVL tree_A con los cursos de la academia A.
        
        Returns
        -------
        AVL
            El árbol de la academia A.
        """
        return self._tree_A
    @property
    def tree_B(self):
        """
        Gets the AVL tree_B con los cursos de la academia B.
        
        Returns
        -------
        AVL
            El árbol de la academia B.
        """
        return self._tree_B
    @property
    def tree_add(self):
        """
        Gets the AVL tree_add con los cursos de la unión de las academias A y B.
        
        Returns
        -------
        AVL
            El árbol de la unión de las academias A y B.
        """
        return self._tree_add
    @property
    def tree_common(self):
        """
        Gets the AVL tree_add con los cursos comunes de las academias A y B.
        
        Returns
        -------
        AVL
            El árbol de los cursos comunes de las academias A y B.
        """
        return self._tree_common

    
    def user_menu(self) -> None:
        """
        Menú interactivo que permite al usuario elegir la información que quiere añadir/consultar sobre el catálogo de cursos de la academia. Presenta una interfaz con 4 opciones posibles (1,2,3,4),
        si el usuario introduce una opción diferente se saldrá del menú y aparecerá en pantalla "Exiting.." (si se introduce un número, se saldrá del while al no cumplir la condición y si se añade 
        cualquier otro caracter aparecerá una excepción al intentar pasarlo a entero y se entrará en el bloque except del try-except). En otro caso, el menú aparecerá continuamente, llamando a la función 
        get_menu_option() para conocer la acción que quiere realizar el usuario. Al llamar a la función user_menu() será necesario introducir los catálogos de las academias, es decir, elegir la opción 1 
        para llenar los árboles, si no se le pedirá al usuario que elija esta opción para continuar.
        Las opciones son las siguientes:
        1- Introducir los catálogos de las academias A y B. Cuenta con un bloque try-except para controlar la excepción causada al pedir al usuario que introduzca el nombre de los ficheros donde se encuentran
           los catálogos y que estos no estén en el drectorio o no se pueda acceder a ellos. En otro caso  se llama al método privado read_courses() para obtener los cursos y llenar los árboles de la academia A
           (tree_A) y B (tree_B) y si están vación tambien el de la oferta agregada (tree_add) y la común (tree_common).
        2- Mostrar oferta agregada. Solo disponible si se ha elegido previamente la opción 1. LLama a la función preorder_indent_BST() para imprimir por pantalla el contenido de tree_add con la unión de los cursos
           de las academias, pasándole como parámetro este árbol y su primera posición.
        3- Mostrar la oferta común. Solo disponible si se ha elegido previamente la opción 1. LLama a la función preorder_indent_BST() para imprimir por pantalla el contenido de tree_common con los cursos comunes
           de las academias, pasándole como parámetro este árbol y su primera posición.
        4- Mostrar estadísticas sobre un árbol determinado. Solo disponible si se ha elegido previamente la opción 1. Es a su vez otro menú con 4 opciones, que se manejan mediante el método privado show_stadistics()

        Returns
        -------
        None

        """
        # option must be an integer, else: except
        option = self._get_menu_option()
        while option in (1,2,3,4):
            if (len(self.tree_A) == 0 or len(self.tree_B) == 0) and option in (2,3,4):
                print("\nPlease, introduzca los datos de ambos cursos")
                option = self._get_menu_option()
                continue
            if option == 1:
                try:
                     self._read_courses()
                     print("\nFicheros leídos correctamente")

                     if self.tree_common.is_empty():
                         self._common_offer()
                     if self.tree_add.is_empty():
                         self._added_offer()
                except:
                    print("\nIntroduzca nombres de archivos válidos en su directorio")

            if option == 2:
                print("\nOfertas disponibles en los cursos A o B: \n")
                # Visualizar el resultado
                print("Árbol fusionado:")
                self._preorder_indent_BST(self.tree_add, self.tree_add.root(), 0)
                
                
            if option == 3:
                print("\nOfertas disponibles en ambos cursos: \n")
                print("Árbol común:")
                self._preorder_indent_BST(self.tree_common, self.tree_common.root(), 0)
                
            if option == 4:
                self._show_stadistics()
                
            option = self._get_menu_option()
        print("Exiting...")
        
            
    def _get_menu_option(self) -> int:
        """
        Muestra las opciones del menú y devuelve la opción elegida por el usuario.
    
        Esta función se utiliza para obtener la opción elegida por el usuario en el menú interactivo. 
        Muestra las opciones disponibles en el menú del programa y solicita al usuario que ingrese una opción. 
        Si el usuario ingresa un número entero válido, devuelve esa opción. 
        Si se ingresa cualquier otro carácter, se maneja la excepción imprimiendo una linea en blanco, para luego salir de la iteracion en el menu.
    
        Returns
        -------
        int
            La opción elegida por el usuario.
    
        Notes
        -----
        Esta función es llamada dentro del método user_menu() para obtener la opción seleccionada por el usuario en el menú principal del programa.

        """
        try: 
            return int(input("\n***   CURSES MENU   ***\nChoose one of the following options: \n 1) Añadir catálogos de los cursos \n   2) Mostrar oferta sumada de los cursos \n   3) Mostrar oferta conjunta de los cursos \n   4) Mostrar estadísticas \n - Press any other key to exit\n"))
        except: 
            print()
            
    
    def _read_courses(self) -> None:
        """
        Solicita al usuario que introduzca los nombres de los archivos de texto que contienen los cursos asociados a las academias A y B. 
        Llama al método create_course_catalog() para crear el catálogo de cada academia, pasándole el nombre del archivo y el arbol asociado para cada curso (tree_A y tree_B respectivamente)
       
        Returns
        -------
        None
    
        Notes
        -----
        Esta función es llamada dentro del método user_menu() cuando el usuario elige la opción 1 para añadir los catálogos de cursos de ambas academias.
    
        """
        cursos_A = input("Enter the name of the file containing the courses for academy A: ")
        cursos_B = input("Enter the name of the file containing the courses for academy B: ")
        self._create_course_catalog(cursos_A, self.tree_A)
        self._create_course_catalog(cursos_B, self.tree_B)
        

    def _create_course_catalog(self, courses_file: str, tree: AVL) -> None:
        """
        Lee el fichero con el nombre dado por el usuario (courses_file) el cual contiene a los cursos de la academia, lo divide en líneas ya que cada línea (sin tener en cuenta las que son comentarios) es un curso, luego crea una instancia de Courses para representar cada curso los cuales tienen sus atributos separados por ",".
        Finalmente, Introduce cada curso en su árbol correspondiente (tree).
        
        Parameters
        ----------
        courses_file : str
            El nombre del archivo que contiene la información de los cursos.
        tree : AVL
            El árbol AVL en el que se almacenarán los cursos.
        
        Returns
        -------
        None
        
        Notes
        -----
        Esta función es llamada desde el método _read_courses() para crear el catálogo de cursos para cada academia.
        El formato del archivo de texto debe ser el siguiente para cada línea: nombre, duración, estudiantes, nivel, idioma y precio, separados por comas.
        Por ejemplo: "C#,133,18,D,Chi,70.08".
        
        """
        with open(courses_file, encoding="ISO-8859-1") as f:
            cursos_text = f.read().strip()
        cursos = cursos_text.split("\n")
        for line in cursos:
            if not line.startswith('#'): #no tenemos en cuenta comentarios del archivo.
                curso_info = line.split(',')
                name, duration, students, level, language, price = curso_info 
                curso = Course(name, float(duration), int(students), level, language, float(price))
                tree[curso.name, curso.level, curso.language] = curso
            
                             
    def _union_courses(self, course_A:Course, course_B:Course) -> Course:
        """
        Returns a new course which is a union of two identical courses (con la misma clave: nombre, idioma, nivel) from different academies,
        keeping the one with higher benefit(income). The attributes of the merged course remain the same as the course with higher benefit except for the number of students, which is the sum of students from both academies.
        
        Parameters
        ----------
        course_A : Course
            Course object representing a course from academy A.
        course_B : Course
            Course object representing a course from academy B.
        
        Returns
        -------
        Course
            Course object representing the merged course.
        """
        if course_A.benefice > course_B.benefice:
            result_course = Course(course_A.name, course_A.duration, course_A.students+course_B.students, course_A.level, course_A.language, course_A.price)
        else:
            result_course = Course(course_B.name, course_B.duration, course_B.students+course_A.students, course_B.level, course_B.language, course_B.price)
        return result_course
    
    def _find_name(self, p, name:str, cnt:int) -> int:
        if p is not self.tree_A.last() and p is not None:
            print(p.value().name)
            if p.value().name == name and p.key() in self.tree_add.keys():
                if not  self.tree_add[p.key()].name.endswith(" A"):
                    self.tree_add[p.key()].name += " A"
                cnt +=1
            if self.tree_A.children(p) is not None:
                for c in self.tree_A.children(p):
                    cnt = self._find_name(c, name, cnt)
            return(cnt)
 
    def _added_offer(self) -> None:
        """
        Combines the course catalogs of both academies into one.
        This method iterates over the courses in academy A and checks if there's a corresponding course
        with the same key in academy B (las claves de los arboles A y B son lo mismo por lo que se define la igualdad de cursos(nombre, nivel e idioma)). 
        If found, it merges the courses using the _union_courses method and adds the merged course to the arbol de la oferta agregada(tree_add). 
        If not found, it adds the course from academy A a el tree_add. Then, it iterates over the courses in academy B and adds any course that is
        not already in the combined catalog. 
        Para esto usa a la funcion _find_name() que comprueba si un curso de la academia B tiene el mismo nombre que uno de la academia A (no contando los cursos que son iguales en ambas). 
        Si la funcion devuelve un numero distinto a 0 (indicando que hay iguales) se añade " B" a el numbre del curso B. 

        Returns
        -------
        None

        """
        # Iterate over courses in academy A
        for key_A, course_A in self.tree_A.items():
            #la clave de los arboles es por lo que se define la igualdad de cursos (nombre, nivel e idioma)
            if key_A in self.tree_B: # Check if the course exists in academy B
                #obtenemos el curso en el arbol B con esa clave que es igual
                course_B = self.tree_B[key_A]
                #obtenemos y añadimos el curso de la union a el arbol de la oferta agregada 
                union_course = self._union_courses(course_A, course_B)
                self.tree_add[key_A] = union_course
            else:
                #de otro modo, si los cursos no son iguales, de todas formas añade el curso en A en el arbol de la oferta agregada 
                new_course = Course(course_A.name, course_A.duration, course_A.students, course_A.level, course_A.language, course_A.price)
                self.tree_add[key_A] = new_course
        
        # Iterate over courses in academy B
        for key_B, course_B in self.tree_B.items():
            # Check if the course is not already in the combined catalog
            if key_B not in self.tree_A and key_B not in self.tree_add:
                # Check if a course with the same name exists in academy A
                cnt = self._find_name(self.tree_A.root(), course_B.name, 0)
                # Add the course from academy B a el arbol de la oferta combinada 
                new_course = Course(course_B.name, course_B.duration, course_B.students, course_B.level, course_B.language, course_B.price)
                self.tree_add[key_B] = new_course
                # If a course with the same name exists in academy A, append ' B' to its name
                if cnt != 0:
                    self.tree_add[key_B].name += " B"
            
    def _common_offer(self) -> None:
        """
        Encuentra los cursos que tienen en común ambos cursos llamando a _union_courses para quedarse con el de mayor beneficio y añadiéndolos a tree_common para conseguir la oferta común.
        
        Este método recorre los catálogos de cursos de ambas academias y busca cursos con claves idénticas (las claves de los arboles A y B son lo mismo por lo que se define la igualdad de cursos). 
        Si encuentra un curso con la misma clave (nombre, nivel e idioma) en ambas academias, compara sus beneficios 
        (ingresos) y conserva el curso con mayor beneficio. Luego, añade este curso al árbol de la oferta común (tree_common).
        
        Returns
        -------
        None
        """
        for key_A, course_A in self.tree_A.items():
            if key_A in self.tree_B:
                course_B = self.tree_B[key_A]
                union_course = self._union_courses(course_A, course_B)
                self.tree_common[key_A] = union_course
                
        
    def _show_stadistics(self) -> None:
        """
        Displays a menu for the user to choose which tree to show statistics for using the _pandas_stats() method.
        
        This method presents a menu with options for the user to choose the tree for which they want to see statistics. 
        The user can choose from four options: 
            1) Statistics for courses in academy A.
            2) Statistics for courses in academy B.
            3) Statistics for la oferta agregada of courses from both academies.
            4) Statistics for la oferta comun of courses shared by both academies.
        
        Returns
        -------
        None
        
        Notes 
        -----
        Este metodo es llamado internamente cuando en el menu principal el usuario selecciona la opcion 4 
        """
        try:
            option2 = int(input("\n-- Catálogos disponibles para las estadísticas --\n 1) Oferta curso A \n 2) Oferta curso B \n 3) Oferta sumada de los cursos \n 4) Oferta común de los cursos \n"))
            if option2 in (1,2,3,4): 
                option_dict = {1:self.tree_A, 2:self.tree_B, 3:self.tree_add, 4:self.tree_common}
                self._pandas_stats(option_dict[option2])
            else:
                print("\nIntroduzca una opción válida")
        except:
            print("\nIntroduzca una opción válida")

    def _pandas_stats(self, tree: "AVL") -> None:
        """
        Displays statistical information (average students per language and per level, and total income) for the selected AVL tree using Pandas.
        
        This method generates statistical information for the courses stored in the given AVL tree.
        Primero, obtiene una lista de los cursos a partir del arbol para hacer el dataframe.
        It calculates the mean number of students per language and per level, as well as the total income generated by all courses.
        The statistical information is displayed in tabular format using the Pandas library.
        
        Parameters
        ----------
        tree : AVL
            The AVL tree for which statistics are to be displayed.
        
        Returns
        -------
        None
        """
        course_data = []
        for course in tree.values():
            course_data.append([course.students, course.level, course.language, course.benefice])
            
        data = pandas.DataFrame(course_data, columns=["Students", "Level", "Language", "Income"])
        
        group_col = "Level"
        target_col = "Students"
        single_stats = data.groupby(group_col).agg({target_col: ["mean"]})
        print('\n', "*"*37, '\n', "    Number of students per level     ", '\n',  "*"*37)
        print(single_stats, "\n")

        group_col = "Language"
        target_col = "Students"
        single_stats = data.groupby(group_col).agg({target_col: ["mean"]})
        print('\n', "*"*37, '\n', "   Number of students per language   ", '\n',  "*"*37)
        print(single_stats, "\n")
        
        target_col = "Income"
        single_stats = data.agg({target_col: ["sum"]})
        print('\n', "*"*20, '\n', "    Total income    ", '\n',  "*"*20)
        print(single_stats, "\n")
    
    
    def _preorder_indent_BST(self, T: AVL, p: AVL.Position, d:int) -> None:
        """
        Print preorder representation of a binary subtree of T rooted at p at depth d.
        To print aTree completely call preorder_indent_BST(aTree, aTree.root(), 0)
    
        Parameters:
        -----------
        T : AVL
            The AVL tree containing the subtree to be printed.
        p : AVL.Position
            The position representing the root of the subtree to be printed.
        d : int
            The depth of the current node in the subtree.
    
        Returns:
        --------
        None
    
        Notes:
        ------
        The purpose of this recursive helper function is to print the preorder representation
        of a binary subtree of the AVL tree. It prints each node in the subtree along with its key
        and value, using indentation to represent the depth of each node in the subtree.
            
        Example:
        --------
        Printing a complete AVL tree called 'tree'
        preorder_indent_BST(tree, tree.root(), 0)
        """
        if p is not None:
            # use depth for indentation
            print(2*d*' ' + "(" + str(p.key()) + "," +  str(p.value()) + ")") 
            self._preorder_indent_BST(T, T.left(p), d+1) # left child depth is d+1
            self._preorder_indent_BST(T, T.right(p), d+1) # right child depth is d+1
    
if __name__ == "__main__":
    manager = CursesManager()
    manager.user_menu()
