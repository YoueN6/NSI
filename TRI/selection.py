def tri_selection(lst):
   for i in range(len(lst)):
       imin = i
       for j in range(i, len(lst)):
           if lst[imin] > lst[j]:
               imin = j
                
       tmp = lst[i]
       lst[i] = lst[imin]
       lst[imin] = tmp
