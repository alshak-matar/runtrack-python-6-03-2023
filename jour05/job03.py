def afficher_tapis_diagonal(n):
    for i in range(n, -1, -1):
        for j in range(n+1):
            if i == j:
                print(" ", end="")
            else:
                print("#", end="")
        print()
afficher_tapis_diagonal(10)
