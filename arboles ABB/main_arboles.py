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
    
    def __init__(self):
        self.tree_A = AVL()
        self.tree_B= AVL()
        self.tree_add = AVL()
        self.tree_common = AVL()

    
    def user_menu(self) -> None:
        # option must be an integer, else: except
        option = int(input("\n***   CURSES MENU   ***\nChoose one of the following options: \n 1) Añadir catálogos de los cursos \n   2) Mostrar oferta sumada de los cursos \n   3) Mostrar oferta conjunta de los cursos \n   4) Mostrar estadísticas \n - Press any other key to exit\n"))
        while option in (1,2,3,4):
            if (len(self.tree_A) == 0 or len(self.tree_B) == 0) and option in (2,3,4):
                print("\nPlease, introduzca los datos de ambos cursos")
                option = int(input("\n***   CURSES MENU   ***\nChoose one of the following options: \n 1) Añadir catálogo de los cursos \n   2)  \n   3)  \n   4) \n - Press any other key to exit\n"))
                continue
            if option == 1:
                try:
                     cursos_A = input("Ingrese el nombre del archivo donde se encuentran los cursos de la academia A:  ")
                     cursos_B = input('Ingrese el nombre del archivo donde se encuentran los cursos de la academia B:  ')     
                     self.read_courses(cursos_A, cursos_B)
                     print("\nFicheros leídos correctamente")
                except:
                    print("\nIntroduzca nombres de archivos válidos en su directorio")
  
            if option == 2:
                print("\nOfertas disponibles en los cursos A o B: \n")
                if self.tree_add.is_empty():
                    self.union_and_display()
                # Visualizar el resultado
                print("Árbol fusionado:")
                self.preorder_indent_BST(self.tree_add, self.tree_add.root(), 0)
                
            if option == 3:
                print("\nOfertas disponibles en ambos cursos: \n")
                if self.tree_common.is_empty():
                    self.common_offer()
                print("Árbol común:")
                self.preorder_indent_BST(self.tree_common, self.tree_common.root(), 0)
                
            if option == 4:
                try:
                    option2 = int(input("\n-- Catálogos disponibles para las estadísticas --\n 1) Oferta curso A \n 2) Oferta curso B \n 3) Oferta sumada de los cursos \n 4) Oferta común de los cursos \n"))
                    if option2 in (1,2,3,4,5,6): 
                        option_dict = {1:self.tree_A, 2:self.tree_B, 3:self.tree_add, 4:self.tree_common}
                        self.pandas_stats(option_dict[option2])
                    else:
                        print("\nIntroduzca una opción válida")
                except:
                    print("\nIntroduzca una opción válida")
                
            option = int(input("\n***   CURSES MENU   ***\nChoose one of the following options: \n 1) Añadir catálogos de los cursos \n   2) Mostrar oferta sumada de los cursos \n   3) Mostrar oferta conjunta de los cursos \n   4) Mostrar estadísticas \n - Press any other key to exit\n"))

        print("Exiting...")

    def read_courses(self, cursos_A, cursos_B):
        with open(cursos_A, encoding="ISO-8859-1") as f:
             # With strip(), we ensure that there are no additional spaces, tabs, or newline characters present in the file.
            cursos_text = f.read().strip()
            self.create_course(cursos_text, self.tree_A)
        with open(cursos_B, encoding="ISO-8859-1") as f:
             # With strip(), we ensure that there are no additional spaces, tabs, or newline characters present in the file.
            cursos_text = f.read().strip()
            self.create_course(cursos_text, self.tree_B)
                             
    def create_course(self, cursos_text:str, tree:"AVL" )->None:
        cursos = cursos_text.split("\n")
        for line in cursos:
            if not line.startswith('#'):
                curso_info = line.split(',')
                name, duration, students, level, language, price= curso_info 
                curso = Course(name, float(duration), int(students), level, language, float(price))
                tree[curso.name, curso.level, curso.language] = curso
    
    
    def union_courses(self, course_A, course_B):
        if course_A.benefice > course_B.benefice:
            result_course = course_A
            result_course.students += course_B.students
        else:
            result_course = course_B
            result_course.students += course_A.students
        return result_course
 
 
    def union_and_display(self):
        for key_A, course_A in self.tree_A.items():
            if key_A in self.tree_B:
                course_B = self.tree_B[key_A]
                union_course = self.union_courses(course_A, course_B)
                self.tree_add[key_A] = union_course
            else:
                self.tree_add[key_A] = course_A
        for key_B, course_B in self.tree_B.items():
            if key_B not in self.tree_A and key_B not in self.tree_add:
                cnt = self.find_name(self.tree_A.root(), course_B.name, 0)
                self.tree_add[key_B] = course_B
                if cnt != 0:
                    self.tree_add[key_B].name += " B"

       
            
    def common_offer(self) -> None:
        for key_A, course_A in self.tree_A.items():
            if key_A in self.tree_B:
                course_B = self.tree_B[key_A]
                union_course = self.union_courses(course_A, course_B)
                self.tree_common[key_A] = union_course
        
                    
    def pandas_stats(self, tree: "AVL") -> None:
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
    
    
    def preorder_indent_BST(self, T, p, d):
        """Print preorder representation of a binary subtree of T rooted at p at depth d.
           To print aTree completely call preorder_indent_BST(aTree, aTree.root(), 0)"""
        if p is not None:
            # use depth for indentation
            print(2*d*' ' + "(" + str(p.key()) + "," +  str(p.value()) + ")") 
            self.preorder_indent_BST(T, T.left(p), d+1) # left child depth is d+1
            self.preorder_indent_BST(T, T.right(p), d+1) # right child depth is d+1
        
    def find_name(self, p, name, cnt):
        if p is not self.tree_A.last() and p is not None:
            print(p.value().name)
            if p.value().name == name and p.key() in self.tree_add.keys():
                self.tree_add[p.key()].name += " A"
                cnt +=1
            if self.tree_A.children(p) is not None:
                for c in self.tree_A.children(p):
                    cnt = self.find_name(c, name, cnt)
            return(cnt)

        
    
if __name__ == "__main__":
    m = CursesManager()
    m.user_menu()

