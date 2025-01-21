import fusion

def tri_fusion(lst:list[int]):
    if len(lst) <= 1:
        return lst
    else:
        return fusion(tri_fusion(lst[:len(lst)//2]), tri_fusion(lst[len(lst)//2:]))