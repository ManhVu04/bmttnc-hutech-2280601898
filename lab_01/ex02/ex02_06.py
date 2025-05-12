innput_scr = input("Enter X, Y: ")
dimension = [int(x) for x in innput_scr.split(",")]
rowcomlumn = dimension[0]
col = dimension[1]
multiply = [[0 for i in range(col)] for j in range(rowcomlumn)]
for i in range(rowcomlumn):
    for j in range(col):
        multiply[i][j] = i*j
print(multiply)

        