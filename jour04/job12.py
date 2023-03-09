def list_order(liste):
    liste.sort()
    return liste

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

L_order = list_order(L)

print("List sorted in ascending order :", L_order)

