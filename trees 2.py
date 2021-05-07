class tree:#creating a class
    def __init__(self,data,des):#creating a root node
        self.data=data
        self.des=des
        self.children = []
        self.parent=None


    def get_value(self):#getting the height of the tree
        c=0
        p= self.parent
        while p:
            c+=1
            p=p.parent
        return c
    def print(self,a): #printing the tree in terms of hierarchy
        if a =='name':
            value=self.data
        elif (a =='both'):
            value = self.data + '(' + self.des + ')'

        else:
            value = self.des
        spaces = ' ' * self.get_value() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print(a)


    def add_child(self, child):# adding children to nodes
        child.parent= self
        self.children.append(child)
def built():# function used to input the values
    infra_head = tree("Vishwa", "Infrastructure Head")
    infra_head.add_child(tree("Dhaval", "Cloud Manager"))
    infra_head.add_child(tree("Abhijit", "App Manager"))

    cto = tree("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(tree("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = tree("Gels", "HR Head")

    hr_head.add_child(tree("Peter", "Recruitment Manager"))
    hr_head.add_child(tree("Waqas", "Policy Manager"))

    ceo = tree("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)
    return ceo




if __name__ == '__main__':
    root = built()
    root.print("name")  # prints only name hierarchy
    root.print("designation")  # prints only designation hierarchy
    root.print("both")  # prints both (name and designation) hierarchy