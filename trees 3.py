class TreeNode:#creating a class
    def __init__(self,data): #creating a root node
        self.data=data
        self.children=[]
        self.parent=None
    def get_value(self): #getting the height of the tree
        c=0
        p=self.parent
        while p:
            c+=1
            p=p.parent
        return c
    def add_child(self,a): # adding children to nodes
        a.parent=self
        self.children.append(a)
    def print_tree(self,d): #printing the tree in terms of height
        g=self.get_value()
        if g<=d:
            s=' ' * self.get_value()*3
            pre=s + '|__'  if self.parent else ""
            print(pre+self.data)
            if self.children:
                for c in self.children:
                    c.print_tree(d)





def built():
    root = TreeNode("Global") #creating root node

    india = TreeNode("India") #creating root node

    gujarat = TreeNode("Gujarat")#creating rootnode
    gujarat.add_child(TreeNode("Ahmedabad"))#creating leafs
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")#creating another root node
    karnataka.add_child(TreeNode("Bangluru"))#its leafs..
    karnataka.add_child(TreeNode("Mysore"))

    india.add_child(gujarat)#adding the root nodes to single node i.e. gujarat was a root node before but it become node of root node india
    india.add_child(karnataka)

    usa = TreeNode("USA")

    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root
if __name__ == '__main__':
    root_node = built() #calling of the built funcyion will will create tree
    for i in range(4):   #calling trees on ths basis of height
        root_node.print_tree(i)
        print(' ')

