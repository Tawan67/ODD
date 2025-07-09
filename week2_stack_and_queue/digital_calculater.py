from stack import Stack


def check_equa(equa):
    equa = [i for i in equa if i != " "]
    open=Stack()
    num = [str(j) for j in range(10)]
    open_text = ['(','{','[']
    close_text = [')','}',']']
    operation = ['+','-','*','/']
    num = num +open_text+close_text
    all = num+operation
    
    for i in equa:
        if i in open_text:
            open.push(i)
        if i in close_text:
            if not(close_text.index(i) == open_text.index(open.pop_item)):
                return 0
        if not(i in all):return 0
    for i in range(len(equa)):
        if equa[i] in operation:
            if i == len(equa)-1 or i == 0:
                return 0
            if not(equa[i-1] in num and equa[i+1] in num):
                return 0
    return 1

def postfix_form(equation):
    equa = [i for i in equation if i != " "]
    if not check_equa(equa):
        return "Invalid Equation"
    equa+="."
    number = [str(i) for i in range(10)]
    oper_1 = ['+','-']
    oper_2 = ['*','/']
    open_text = ['(','{','[']
    close_text = [')','}',']']
    custom_order = {}
    for i in number:
        custom_order[i]=0
    for i in oper_1:
        custom_order[i]=1
    for i in oper_2:
        custom_order[i]=2
    for i in open_text:
        custom_order[i]=3
    for i in close_text:
        custom_order[i]=4
    num = Stack()
    oper = Stack()
    anwser = list()
    for i in equa:
        if i in number:
            if num.isEmpty:
                num.push(i)
            else:
                anwser.append(num.pop_item)
                num.push(i)
        else:
            if oper.isEmpty and i !='.': # operation ว่าง
                oper.push(i)
            elif i !='.' and custom_order[oper.peek] < custom_order[i]: # * ทับ + == เอา เลข ออก เก็บ บวก
                anwser.append(num.pop_item)
                oper.push(i)
                # print(oper)
            elif i !='.' and custom_order[oper.peek] > custom_order[i]:# + ทับ * == เอา เงข ออก * ออก ก่อน * ออก แล้ว add +
                anwser.append(num.pop_item)
                anwser.append(oper.pop_item)
                if not oper.isEmpty: anwser.append(oper.pop_item)
                if i!= '.':oper.push(i)
            elif i !='.' and custom_order[oper.peek] == custom_order[i]: # + เจอ +
                anwser.append(num.pop_item)
                anwser.append(oper.pop_item)
                if i!= '.':oper.push(i)
            elif i =='.' :
                anwser.append(num.pop_item)
                anwser.append(oper.pop_item)
    return anwser
        

equa = input("Input Your Eqution :")
result = postfix_form(equa)
print(result)
