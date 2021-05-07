class tree:
    def __init__(self,data):
        self.data=data
        self.children = []
        self.parent=None


    def get_value(self):
        c=0
        p= self.parent
        while p:
            c+=1
            p=p.parent
        return c
    def print(self):
        spaces = ' ' * self.get_value() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print()
    def add_child(self, child):
        child.parent= self
        self.children.append(child)
def built():
    root=tree('electronics')
    lap=tree('Laptop')
    lap.add_child(tree("Mac"))
    lap.add_child(tree("acer"))
    lap.add_child(tree("lenovo"))
    lap.add_child(tree("hp"))
    lap.add_child(tree("dell"))
    tv=tree('TV')
    tv.add_child(tree('LG'))
    tv.add_child(tree('onida'))
    tv.add_child(tree('vediocon'))
    tv.add_child(tree('samsung'))
    mob=tree('Mobile')
    mob.add_child(tree('oneplus'))
    mob.add_child(tree('redmi'))
    mob.add_child(tree('samsung'))
    mob.add_child(tree('iphone'))
    mob.add_child(tree('nokia'))
    root.add_child(lap)
    root.add_child(mob)
    root.add_child(tv)
    root.print()




if __name__ == '__main__':
    built()
    pass
