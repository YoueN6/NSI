def fusion(L1:list[int], L2:list[int]) -> list[int]:
    L3 = []
    i = 1
    j = 1
    while len(L3) != len(L1) + len(L2) and i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            L3.append(L1[i])
            i += 1
        if L1[i] > L2[j]:
            L3.append(L2[j])
            j += 1
        