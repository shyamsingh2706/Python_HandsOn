''' Extend TreeNode class built in "Create_General_Tree so that it takes designation in data part of TreeNode class.
   Also extend/override print_tree function such that it can print either name tree, designation tree or name and designation tree.
   Further overload print_tree function such that Print Hierarchy function will print hierarchy by Levels
'''

import Create_General_Tree as CGT
from pythonlangutil.overload import Overload, signature

class Management_tree(CGT.TreeNode):

    def __init__(self,Node_name,designation):

        self.node_name = Node_name
        self.parent_node = None
        self.child_node = []
        self.designation = designation


    '''
    Print Type N --> Print by Name
    Print Type D --> Print by Designation
    Print Type B --> Print by Both
    '''
    @Overload
    @signature("str")
    def print_tree(self, print_type):

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__"

        if(print_type == 'N'):
            print(prefix + self.node_name)
        elif (print_type == 'D'):
            print(prefix + self.designation)
        elif (print_type == 'B'):
            print(prefix + self.node_name + ' ( ' + self.designation + ' )')

        for child in self.child_node:
            child.print_tree(print_type)

    @print_tree.overload
    @signature("str","int")
    def print_tree(self, print_type, level):

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__"

        if (print_type == 'N'):
            print(prefix + self.node_name)
        elif (print_type == 'D'):
            print(prefix + self.designation)
        elif (print_type == 'B'):
            print(prefix + self.node_name + ' ( ' + self.designation + ' )')

        if (self.get_level() < level):
            for child in self.child_node:
                child.print_tree(print_type,level)


def Build_tree():

        ''' Print by Name, Designation or Both '''
        Nilupul = Management_tree("Nilupul","CEO")
        Chinmay = Management_tree("Chinmay","CTO")
        Nilupul.add_child(Chinmay)
        Vishwa = Management_tree("Vishwa","Tech Artch.")
        Anupam = Management_tree("Anupam","HR")
        Chinmay.add_child(Vishwa)
        Chinmay.add_child(Anupam)
        Peter = Management_tree("Peter","Policy HR")
        Abhijeet = Management_tree("Abhijeet","Application Owner")
        Vishwa.add_child(Abhijeet)
        Anupam.add_child(Peter)
        Nilupul.print_tree("B")
        print ("##################")
        Nilupul.print_tree("D", 2)

if __name__ == "__main__" :

    Build_tree()