scr = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([scr[i] for i in range(1, len(scr)) if scr[i] > scr[i - 1]])
