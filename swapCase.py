def swap_case(s):
    r=[]
    for i in (s):
        
        if i == i.lower():
            i = i.upper()
            r.append(i)
        elif i == i.upper():
            i= i.lower()
            r.append(i)
        else:
            r.append(i)
    return ''.join(r)