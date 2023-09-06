import random
class Node:
    def __init__(self,data):
        
        self.left=None
        self.right=None
        self.data=data

    def print_wood(self):
        
        if self.left:
            self.left.print_wood()
        print(self.data)
        if self.right:
            self.right.print_wood()

    def insert(self,data):
        if data == self.data:
            self.data = data
        else:
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else :
                    self.left.insert(data)
            elif data> self.data:
                
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def max_el(self):
        if self.right:
            print("self.right")
            return self.right.max_el()
        else:
            print("else", self.data)
            return self.data
    
    def search_el(self,data):        
        if data!=self.data:
            if  data < self.data:
                
                if self.left is not  None:
                    return self.left.search_el(data)
                else:
                    return "элемент не найден"
            else:
                if self.right is not None:
                    return self.right.search_el(data)
                else:
                    return "элемент не найден"
                
        else:
            return "искомый элемент найден"















