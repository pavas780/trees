class binary:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def addchild(self,data):
        if data==self.data:
            return
        if data<self.data:
            if self.left:
                self.left.addchild(data)
            else:
                self.left=binary(data)
        else:
            if self.right:
                self.right.addchild(data)
            else:
                self.right=binary(data)
    def search(self,v):
        if v==self.data:
            print(v,'is present in tree')
            return True
        if v<self.data:
            if self.left:
                return self.left.search(v)
            else:
                return  False
        if v>self.data:
            if self.right:

                return self.right.search(v)
            else:
                return False
    def inorder(self):
        element=[]
        if self.left:
            element+=self.left.inorder()
        element.append(self.data)
        if self.right:
            element+=self.right.inorder()
        return element
    def preorder(self):
        element=[self.data]


        if self.left:
            element+=self.left.preorder()
        if self.right:
            element+=self.right.preorder()
        return element
    def postorder(self):
        element = []
        if self.left:
            element += self.left.postorder()
        if self.right:
            element += self.right.postorder()
        element.append(self.data)
        return element

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            max_val = self.left.find_max()
            self.data = max_val
            self.right = self.left.delete(max_val)

        return self

def built_tree(element):
    root=binary(element[0])
    for i in range(1,len(element)):
        root.addchild(element[i])
    return  root
if __name__=='__main__':

    numbers_tree = built_tree([17, 34, 81, 18, 84, 23, 41,42,92])
    print("In order traversal gives this sorted list:", numbers_tree.inorder())
    print('the minimum element in the tree is',numbers_tree.find_min()) #finds minimum element in entire binary tree
    print('the maximum element in the tree is',numbers_tree.find_max()) #finds maximum element in entire binary tree
    print('the sum of the elements in the tree is',numbers_tree.calculate_sum()) #calcualtes sum of all elements
    print('In postorder traversal gives this sorted list:',numbers_tree.postorder()) #performs post order traversal of a binary tree
    print('In preorder traversal gives this sorted list:',numbers_tree.preorder())# performs  pre order traversal of a binary tree
    numbers_tree.delete(42)
    print('inorder traversal after deleting ',numbers_tree.inorder())
    numbers = built_tree([17, 4, 1, 20, 9, 23, 18, 34])

    numbers.delete(18)
    print('In order traversal gives this sorted list:',numbers.inorder())