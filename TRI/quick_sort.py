def quick_sort(lst:list[int]):
    pivot = lst[0]
    reste = lst[1:]
    gauche = [x for x in reste if x < pivot]
    droite = [x for x in reste if x >= pivot]
    return quick_sort(gauche) + [pivot] + quick_sort(droite)