def nest_ed(lst):
    n_lst=[]
    for i in lst:
        #if list(i):
        if isinstance(i,list):    
            n_lst.extend(nest_ed(i))
        else:
            n_lst.append(i)    
    
    return n_lst            
            
                    

lst = [[1,2,[3]],4,[5,[6,[7]]]]
n_el = nest_ed(lst)
print(n_el)