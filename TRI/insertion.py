def insertion(lst):
    for i in range(1, len(lst)):
        valeur_a_inserer = lst(i)
        j = i
        while j > 0 and lst[j-1] > valeur_a_inserer:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = valeur_a_inserer