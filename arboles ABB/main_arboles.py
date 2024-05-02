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
    This class manages a catalog of courses using AVL trees to store them and access them efficiently. 
    It consists of four AVL trees: tree_A, tree_B, tree_add, and tree_common, which respectively store the courses from academy A, academy B, the union of both offers, and the common offer. 
    Through this class, the user can access the available information via a menu, which will display the following options:
        - 1) Add the course catalogs from both academies (required for the following options)
        - 2) Show the aggregated offer
        - 3) Show the common offer
        - 4) Show statistics for the desired tree
    
    Usage Example:
        manager = CursesManager()
        manager.user_menu()
        
    Attributes
    ----------
    Class Attributes: 
        
        tree_A: AVL
            AVL tree that stores the courses from academy A, which will be entered by the user.
        tree_B: AVL
            AVL tree that stores the courses from academy B, which will be entered by the user.
        tree_add: AVL
            AVL tree that stores the union of the courses from both academies, keeping the ones with the highest benefit in case they have the same name, language, and level in both academies.
        tree_common: AVL
            AVL tree that stores the common courses from both academies (same name, level, and language), keeping the one with the highest benefit.
        
            
    Methods
    -------
    Public Methods:
        user_menu(self) -> None:
            This function allows the user to choose the action to perform among the following:
                - 1) Add the course catalogs from both academies (required for the following options)              
                - 2) Aggregated offer
                - 3) Common offer
                - 4) Show statistics, choosing the tree from which the user wants to retrieve information         

    Private Methods: 
         _get_menu_option(self) -> int:
             Displays the menu options and returns the option chosen by the user.
             
         _read_courses(self)-> None:
            Prompts the user to enter the name of the text file that includes the course catalog first from academy A and then from academy B. Then calls the
            create_course_catalog() method to create the catalog for each academy, passing the filename and the corresponding tree (tree_A and tree_B respectively).
                               
         _create_course_catalog(self, courses_file: str, tree: AVL) -> None:
            Reads the file with the given name and splits it into lines. Each line represents a course, and each course has its attributes separated by "," : name, duration, students, level, language, and price.
            Inserts each course into the corresponding tree of the CourseManager.
            
         _union_courses(self, course_A:Course, course_B:Course) -> Course:
            Given two identical courses (with the same key: name, language, level) from both academies, returns the one with higher benefit.
            
         _find_name(self, p, name:str, cnt:int) -> int:
             Given a course name, traverses the academy A tree (tree_A) starting from position p to find if there is any course in it that is also in tree_add and has that 
             same name. The reason for this is to add the string " A" to the name of this course in tree_add to distinguish it from the one in academy B.
       
         _added_offer(self) -> None:
            Traverses tree_A adding its courses to tree_add to obtain the aggregated offer, checking that there is no other course with the same key [name, level, language] in tree_B.
            If this occurs, the union_course() method is called. Then, tree_B is traversed to add its courses, distinguishing them from those of academy B if they have the same name by adding
            a distinctive identifier in the name.
            
         _common_offer(self) -> None:
           Finds the courses that are common to both academies, keeping the one with the highest benefit, and adds them to tree_common to obtain the common offer.
            
         _show_statistics(self) -> None:
             Displays a menu to choose the tree from which we want to show statistics using pandas_stats()
             
         _pandas_stats(self, tree:AVL) -> None:
            Displays statistical information (average students per language and per level and total income) of the introduced tree.
        
         _preorder_indent_BST(self, T: AVL, p: AVL.Position, d:int) -> None:
            Prints the preorder representation of a binary subtree of T rooted at p at depth d.
            To print aTree completely call preorder_indent_BST(aTree, aTree.root(), 0)
    """
    
    def __init__(self):
        """
        Defines the class attributes, which are four trees that store courses.
        
        Class Attributes: 
        -----------------
            tree_A: AVL
                Tree with courses from academy A (starts as empty)
            tree_B: AVL
                Tree with courses from academy B (starts as empty)
            tree_add: AVL
                Tree with courses from the union of academies A and B (starts as empty)
            tree_common: AVL
                Tree with courses that are common to academies A and B (starts as empty)
               
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
        Gets the AVL tree_A with the courses from academy A.
        
        Returns
        -------
        AVL
            The tree of academy A.
        """
        return self._tree_A
    
    @property
    def tree_B(self):
        """
        Gets the AVL tree_B with the courses from academy B.
        
        Returns
        -------
        AVL
            The tree of academy B.
        """
        return self._tree_B
    
    @property
    def tree_add(self):
        """
        Gets the AVL tree_add with the courses from the union of academies A and B.
        
        Returns
        -------
        AVL
            The tree of the union of academies A and B.
        """
        return self._tree_add
    
    @property
    def tree_common(self):
        """
        Gets the AVL tree_common with the courses that are common to academies A and B.
        
        Returns
        -------
        AVL
            The tree of the courses that are common to academies A and B.
        """
        return self._tree_common

    def user_menu(self) -> None:
        """
        Interactive menu allowing the user to choose the information they want to add/consult about the course catalog of the academy. 
        It presents an interface with 4 possible options (1, 2, 3, 4). If the user enters a different option, the menu will exit and "Exiting.." will be displayed on the screen 
        (if a number is entered, the while loop will exit due to the condition not being met, and if any other character is added, an exception will occur when trying to cast it to an integer and 
        the try-except block will be entered). Otherwise, the menu will continue to appear, calling the get_menu_option() function to determine the action the user wants to perform. 
        When calling the user_menu() function, it will be necessary to enter the catalogs of the academies, this means, at first, the user should choose option 1 to fill the trees, otherwise the user will be prompted 
        to choose this option to continue.
        
        Menu Options:
            
        1- Enter the catalogs of academies A and B. It has a try-except block to handle the exception caused when asking the user to enter the file names where the catalogs are located and 
           they are not in the directory or cannot be accessed. Otherwise, it calls the private method read_courses() to obtain the courses and fill the trees of academy A (tree_A) and B (tree_B), 
           and if they are empty also the one for the added offer (tree_add) and the common one (tree_common).
        2- Show added offer. Only available if option 1 has been previously chosen. Calls the preorder_indent_BST() function to print the contents of tree_add with the union of the courses from the academies, 
           passing this tree and its root position as parameters.
        3- Show common offer. Only available if option 1 has been previously chosen. Calls the preorder_indent_BST() function to print the contents of tree_common with the common courses of the academies, 
           passing this tree and its root position as parameters.
        4- Show statistics about a specific tree. Only available if option 1 has been previously chosen. It is also another menu with 4 options, which are handled by the private method show_statistics().
        
        Returns
        -------
        None
        """
        # option must be an integer, else: except
        option = self._get_menu_option()
        while option in (1,2,3,4):
            if (len(self.tree_A) == 0 or len(self.tree_B) == 0) and option in (2,3,4):
                print("\nPlease, enter data for both courses")
                option = self._get_menu_option()
                continue
            if option == 1:
                try:
                     self._read_courses()
                     print("\nFiles read successfully")
    
                     if self.tree_common.is_empty():
                         self._common_offer()
                     if self.tree_add.is_empty():
                         self._added_offer()
                except:
                    print("\nEnter valid file names in your directory")
    
            if option == 2:
                print("\nOffers available in courses A or B (added offer): \n")
                print("Merged Tree:")
                self._preorder_indent_BST(self.tree_add, self.tree_add.root(), 0)
                
            if option == 3:
                print("\nOffers available in both courses (common offer): \n")
                print("Common Tree:")
                self._preorder_indent_BST(self.tree_common, self.tree_common.root(), 0)
                
            if option == 4:
                self._show_statistics()
                
            option = self._get_menu_option()
        print("Exiting...")

    def _get_menu_option(self) -> int:
        """
        Displays the menu options and returns the option chosen by the user.
    
        This function is used to obtain the option chosen by the user in the interactive menu. 
        It displays the available options in the program menu and prompts the user to enter an option. 
        If the user enters a valid integer, it returns that option. 
        If any other character is entered, the exception is handled by printing a blank line, and then exiting the menu iteration.
    
        Returns
        -------
        int
            The option chosen by the user.
    
        Notes
        -----
        This function is called within the user_menu() method to get the option selected by the user in the main program menu.
        """
        try: 
            return int(input("\n***   CURSES MENU   ***\nChoose one of the following options: \n 1) Add course catalogs \n   2) Show added course offer \n   3) Show common course offer \n   4) Show statistics \n - Press any other key to exit\n"))
        except: 
            print()

    def _read_courses(self) -> None:
        """
        Prompts the user to enter the names of the text files containing the courses associated with academies A and B. 
        Calls the create_course_catalog() method to create the catalog for each academy, passing the filename and the associated tree for each course (tree_A and tree_B respectively).
       
        Returns
        -------
        None
    
        Notes
        -----
        This function is called within the user_menu() method when the user chooses option 1 to add the course catalogs of both academies.
        """
        courses_A = input("Enter the name of the file containing the courses for academy A: ")
        courses_B = input("Enter the name of the file containing the courses for academy B: ")
        self._create_course_catalog(courses_A, self.tree_A)
        self._create_course_catalog(courses_B, self.tree_B)
                
    def _create_course_catalog(self, courses_file: str, tree: AVL) -> None:
        """
        Reads the file with the name provided by the user (courses_file), which contains the courses of the academy. It divides the file into lines, where each line (excluding comments) represents a course. Then it creates an instance of Course to represent each course, where the attributes are separated by commas.
        Finally, it inserts each course into the corresponding tree (tree).
        
        Parameters
        ----------
        courses_file : str
            The name of the file containing the course information.
        tree : AVL
            The AVL tree in which the courses will be stored.
        
        Returns
        -------
        None
        
        Notes
        -----
        This function is called from the _read_courses() method to create the course catalog for each academy.
        The format of the text file should be as follows for each line: name, duration, students, level, language, and price, separated by commas.
        For example: "C#,133,18,D,Chi,70.08".
        
        """
        with open(courses_file, encoding="ISO-8859-1") as f:
            courses_text = f.read().strip()
        courses = courses_text.split("\n")
        for line in courses:
            if not line.startswith('#'): # Ignore comments in the file.
                course_info = line.split(',')
                name, duration, students, level, language, price = course_info 
                course = Course(name, float(duration), int(students), level, language, float(price))
                tree[course.name, course.level, course.language] = course

                             
    def _union_courses(self, course_A:Course, course_B:Course) -> Course:
        """
        Returns a new course which is a union of two identical courses (with the same key: name, language, level) from different academies,
        keeping the one with higher benefit (income). The attributes of the merged course remain the same as the course with higher benefit except for the number of students, which is the sum of students from both academies.
        
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
        with the same key in academy B (the keys of trees A and B are the same so the equality of courses is defined by course attributes (name, level, and language)). 
        If found, it merges the courses using the _union_courses method and adds the merged course to the combined catalog tree (tree_add). 
        If not found, it adds the course from academy A to the combined catalog. Then, it iterates over the courses in academy B and adds any course that is
        not already in the combined catalog. 
        For this, it uses the _find_name() function that checks if a course from academy B has the same name as one from academy A (excluding courses that are identical in both). 
        If the function returns a number other than 0 (indicating duplicates), " B" is appended to the name of course B. 
    
        Returns
        -------
        None
    
        """
        # Iterate over courses in academy A
        for key_A, course_A in self.tree_A.items():
            # The keys of the trees define the equality of courses (name, level, and language)
            if key_A in self.tree_B: # Check if the course exists in academy B
                # Get the course in tree B with the same key
                course_B = self.tree_B[key_A]
                # Merge and add the course to the combined catalog tree
                union_course = self._union_courses(course_A, course_B)
                self.tree_add[key_A] = union_course
            else:
                # Otherwise, if the courses are not identical, add the course from A to the combined catalog tree 
                new_course = Course(course_A.name, course_A.duration, course_A.students, course_A.level, course_A.language, course_A.price)
                self.tree_add[key_A] = new_course
        
        # Iterate over courses in academy B
        for key_B, course_B in self.tree_B.items():
            # Check if the course is not already in the combined catalog
            if key_B not in self.tree_A and key_B not in self.tree_add:
                # Check if a course with the same name exists in academy A
                cnt = self._find_name(self.tree_A.root(), course_B.name, 0)
                # Add the course from academy B to the combined catalog tree 
                new_course = Course(course_B.name, course_B.duration, course_B.students, course_B.level, course_B.language, course_B.price)
                self.tree_add[key_B] = new_course
                # If a course with the same name exists in academy A, append ' B' to its name
                if cnt != 0:
                    self.tree_add[key_B].name += " B"

    def _common_offer(self) -> None:
        """
        Finds the courses common to both academies by calling _union_courses to retain the one with greater benefit and adding them to tree_common to achieve the common offer.
        
        This method iterates over the course catalogs of both academies and looks for courses with identical keys (the keys of trees A and B are the same so the equality of courses is defined by course attributes). 
        If it finds a course with the same key (name, level, and language) in both academies, it compares their benefits 
        (revenue) and retains the course with greater benefit. Then, it adds this course to the tree of common offer (tree_common).
        
        Returns
        -------
        None
        """
        for key_A, course_A in self.tree_A.items():
            if key_A in self.tree_B:
                course_B = self.tree_B[key_A]
                union_course = self._union_courses(course_A, course_B)
                self.tree_common[key_A] = union_course
            
    def _show_statistics(self) -> None:
        """
        Displays a menu for the user to choose which tree to show statistics for using the _pandas_stats() method.
        
        This method presents a menu with options for the user to choose the tree for which they want to see statistics. 
        The user can choose from four options: 
            1) Statistics for courses in academy A.
            2) Statistics for courses in academy B.
            3) Statistics for the combined offer of courses from both academies.
            4) Statistics for the common offer of courses shared by both academies.
        
        Returns
        -------
        None
        
        Notes 
        -----
        This method is internally called when the user selects option 4 in the main menu.
        """
        try:
            option2 = int(input("\n-- Available catalogs for statistics --\n 1) Academy A course offer \n 2) Academy B course offer \n 3) Added course offer \n 4) Common course offer \n"))
            if option2 in (1, 2, 3, 4): 
                option_dict = {1: self.tree_A, 2: self.tree_B, 3: self.tree_add, 4: self.tree_common}
                self._pandas_stats(option_dict[option2])
            else:
                print("\nPlease enter a valid option.")
        except:
            print("\nPlease enter a valid option.")


    def _pandas_stats(self, tree: "AVL") -> None:
        """
        Displays statistical information (average students per language and per level, and total income) for the selected AVL tree using Pandas.
        
        This method generates statistical information for the courses stored in the given AVL tree.
        First, it obtains a list of courses from the tree to create the dataframe.
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
        """
        if p is not None:
            # use depth for indentation
            print(2*d*' ' + "(" + str(p.key()) + "," +  str(p.value()) + ")") 
            self._preorder_indent_BST(T, T.left(p), d+1) # left child depth is d+1
            self._preorder_indent_BST(T, T.right(p), d+1) # right child depth is d+1
    
if __name__ == "__main__":
    manager = CursesManager()
    manager.user_menu()
