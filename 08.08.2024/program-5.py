def tri_invt(rows):
    for i in range(rows, 0, -1):
        print('$' * i)
rows = int(input("Enter the number of rows: "))
tri_invt(rows)
