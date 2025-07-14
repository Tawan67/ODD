def reverse(string:str):
    i = [i+']' for i in string.split("]")]
    i.reverse()
    i=[j for j in i if j!=']']
    i = "".join(i)
    return i
print(reverse(input()))
