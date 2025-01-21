def fusion(L1:list[int], L2:list[int]) -> list[int]:
    L3 = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            L3.append(L1[i])
            i += 1
        if L1[i] >= L2[j]:
            L3.append(L2[j])
            j += 1
    while i < len(L1):
        L3.append(L1[i])
    while j < len(L2):
        L3.append(L2[j])