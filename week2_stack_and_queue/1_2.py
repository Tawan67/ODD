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
    def is_in(self,ele):
        return ele in self.items
    def __str__(self):
        s = "stack of "+str(self.size_list)+ "\nlist :"
        for i in self.items:
            s += str(i)+" "
        return s
    def sum(self):
        sum = 0
        try:
            for i in self.items:
                sum+=i
            return sum
        except:
            print("This is not pure Numberic Stack")
            return None
        
    def reset(self,re_list=None):
        if re_list == None:
            re_list = []
        self.items = re_list.copy()
    
    def sort(self):
        self.items.sort()
    def copy(self,stack:"Stack"):
        self.reset()
        store_stack = Stack()
        while not(stack.isEmpty):
            self.push(stack.peek)
            store_stack.push(stack.pop_item)
        while not(store_stack.isEmpty):
            stack.push(store_stack.pop_item)
            
def is_float(element):
    if not("." in element):
        return 0
    for i in element:
        if i == '.':
            initial  = element.index(i)
            try:
                if not(element[initial-1].isnumeric() and element[initial+1].isnumeric()):
                    return 0
            except:
                return 0
    return 1
last = []
value = 0

def reverse(string:str):
    i = [i+']' for i in string.split("]")]
    i.reverse()
    i=[j for j in i if j!=']']
    i = "".join(i)
    return i

def out(ans:Stack,initial,before:Stack):
    # print("start")
    if ans.sum() > initial:
        pass
    output = ""
    front = ""
    # check = len(last)>0
    
    end = (ans.sum()*2)+20
    store_1 =Stack()
    store_2 = Stack()
    
    store_2.copy(before)
    store_1.copy(ans)
    # print("??????????????????")
    # print(store_1)
    # print(store_2)
    # print("////////////////////")
    while store_2.isEmpty and not(store_1.isEmpty):
        p_u.push(store_1.pop_item)
        front+= "PU:"+str(p_u.pop_item)+" "
    while not(store_2.isEmpty) or not(store_1.isEmpty):
        if not(store_1.isEmpty) and not(before.is_in(store_1.peek)):
            p_u.push(store_1.pop_item)
        elif not(store_1.isEmpty) :
            store_1.pop_item
            
        if not(store_2.isEmpty) and not(ans.is_in(store_2.peek)):
            p_o.push(store_2.pop_item)
        elif not(store_2.isEmpty):
            store_2.pop_item
        if not(p_o.isEmpty): front+= "PO:"+str(p_o.pop_item)+" "
        

    p_u2 = Stack()
    p_u2.reset()
    
    while not(p_u.isEmpty):
        p_u2.push(p_u.pop_item)
    while not(p_u2.isEmpty):
        front+= "PU:"+str(p_u2.pop_item)+" "
    # while not(p_o.isEmpty):
    #     if not(p_o.isEmpty):front+= "PO:"+str(p_o.pop_item)+" "
    # while not(p_u.isEmpty):
    #     if not(p_u.isEmpty):front+= "PU:"+str(p_o.pop_item)+" "
    # while not(store_2.isEmpty) and ans.sum() < before.sum():
    #     if not(ans.is_in(store_2.peek)):
    #         p_u.push(store_2.pop_item)
    #     elif not(store_2.isEmpty):
    #         store_2.pop_item
    #     if not(before.is_in(store_1)):
    #         p_o.push(store_1.pop_item)
    #     else:
    #         store_1.pop_item
            
    #     front+= "PU:"+str(p_u.pop_item)+" "
    store_1.copy(ans)
    while not(store_1.isEmpty):
        # if check:
        #     for i in range(len(last)):
        #         front += "PO:"+str(last.pop(i-1))+" "
        
        output+= '['+str(store_1.pop_item)+']'
        output1 = reverse(output)
        bar = ""
        for i in range(5-ans.size_list):
            bar+='-'
        
    # print(p_o)
    print(f"{front}=> {bar}{output1}|======|{output}{bar} => {end} KG.")
    # print("STOP")
    pass


plate_list = [1.25,2.5,5,10,15,20,25]
plate = Stack(plate_list)
ans = Stack()
store = Stack()
p_o = Stack()
p_u = Stack()
before = Stack()

def advice_plate(i):
    defult = i
    before.copy(ans)
    
    plate.reset(plate_list)
    ans.reset()
    # print(plate)
    while not(store.isEmpty):
        plate.push(store.pop_item)
    plate.sort()
    if i == 20:
        print("-----|======|----- => 20 KG.")
        return 1
    i = i-20 # del stick weight for 20 kg
    i=i/2
    check = i
 
    
    # if not(ans.isEmpty):
    #     if ans.sum() >check:
            
    #         while ans.sum() > check:
    #             # p_u.push(ans.peek)
    #             store.push(ans.pop_item)
    #         i = i - ans.sum()
    #     elif ans.sum() < check:
    #         i = i-ans.sum()
        
    #     print(i)
    # print(plate)
    # print(store)
    while (i > 0) and not(plate.isEmpty):
        
        if i >= plate.peek:
            i -= plate.peek
            # p_o.push(plate.peek)
            ans.push(plate.pop_item)
            
        else:
            plate.pop_item
            
        if check == ans.sum():
            out(ans,check,before)
            return 1
        
    
    if check != ans.sum() and len(sticks) > 0:
        print(f"It's impossible to achieve the weight you want({defult}).")
        return 0

#main

input_text = input("Enter needed weight(s): ")
check = True
sticks =[]
for i in input_text:
    if i ==" ":
        stick_base = input_text.split(" ")
        for i in stick_base:
            if is_float(i):
                sticks.append(float(i))
            else:
                sticks.append(int(i))
        check = False
        break
if check:
    if(is_float(input_text)):
        sticks.append(float(input_text))
    else:
        sticks.append(int(input_text))




for i in sticks:
    # print(i)
    if advice_plate(i) ==0:
        break
    # print(f"status = {advice_plate(i)}")

# มีทางแก้ 2 ทางที่คิดไว้ 1 คือทำตัวเก็บค่าก่อนหนเ้าแล้วค่อยมาดูว่าอันไหนจะเอาเข้าหรือเอาออก
# 2  คือ ไม่ reset ค่าของ ans แล้ว เอาค่า sum ออกมา จากนั้นเอาไปเช็คกับค่า input ว่าขาดหรือเกิน ถ้าขาดให้ push เข้า ถ้าเกิน ให้ pop ออก จนกว่าจะน้อยกว่า แล้วเรียงค่าใน plate 