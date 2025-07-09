class Stack:
    def __init__(self,list_item = None):
        if list_item == None:
            list_item = []
        self.items = list_item
        self.size = len(self.items)
        
    def push(self,item):
        self.items.append(item)
        
        
    @property
    def pop_item(self):
        if len(self.items):
            return self.items.pop()
        print("Can't Pop It's Out of Range")
        return None
    @property
    def peek(self):
        return self.items[-1]
    @property
    def isEmpty(self):
        return len(self.items)==0
    @property
    def size_list(self):
        return len(self.items)

    def __str__(self):
        s = "stack of "+str(self.size_list)+ "\nlist :"
        for i in self.items:
            s += str(i)+" "
        return s
    
  
# s=Stack(["lemon","ice"])
# print(s)
# s.push("pop")
# print(s)