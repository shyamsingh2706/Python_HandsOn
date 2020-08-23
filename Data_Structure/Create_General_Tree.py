
''' Program to create a product Tree and print its hierarchy '''

class TreeNode() :

    def __init__(self, Node_name):

        self.node_name = Node_name
        self.parent_node = None
        self.child_node = []

    def add_child(self,child_node_name):

        child_node_name.parent_node = self
        self.child_node.append(child_node_name)

    def get_level(self):

        level = 0
        p = self.parent_node
        while p:
            level = level + 1
            p = p.parent_node

        return level

    def print_tree(self):

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__"
        print(prefix + self.node_name)
        for child in self.child_node:
            child.print_tree()

def Build_tree():

        Root = TreeNode("Root")
        Electronics = TreeNode("Electronics")
        Root.add_child(Electronics)
        laptop = TreeNode("laptop")
        Electronics.add_child(laptop)
        Acer = TreeNode("Acer")
        HP = TreeNode("HP")
        Dell = TreeNode("Dell")
        laptop.add_child(Acer)
        laptop.add_child(HP)
        laptop.add_child(Dell)
        TV = TreeNode("TV")
        Electronics.add_child(TV)
        Xiomi = TreeNode("Xiomi")
        Samsung = TreeNode("Samsung")
        Sony = TreeNode("Sony")
        TV.add_child(Xiomi)
        TV.add_child(Sony)
        TV.add_child(Samsung)
        Mob = TreeNode("Mobile")
        Electronics.add_child(Mob)
        Mob.add_child(Xiomi)
        Mob.add_child(Sony)
        Root.print_tree()

if __name__ == "__main__" :

    Build_tree()