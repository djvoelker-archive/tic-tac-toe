
grid = ['O', ' ', 'X', 'O', ' ', ' ', 'X', ' ', ' ']

def print_grid():
    for r in range(3):    
        print("     " + str(grid[3*r+0]) + " | " + str(grid[3*r+1]) + " | " + str(grid[3*r+2]))
        if r < 2: print("    -----------")
    print('\n\n')

def hi(i,j):
    for m in range(3):
        for n in range([2,3,3][m]):
            a = [grid[[2*n+2*(2-n)*x, 3*n+x, n+3*x][m]] for x in range(3) if grid[[2*n+2*(2-n)*x, 3*n+x, n+3*x][m]] == i]
            g = [grid[[2*n+2*(2-n)*x, 3*n+x, n+3*x][m]] for x in range(3)]
            if i in g and ' ' in g and len(set(a)) < len(a):
                grid[[2*n+2*(2-n)*g.index(" "), 3*n+g.index(" "), n+3*g.index(" ")][m]] = j
                return
                
    if (i,j) == ('O','O'): hi('X','O')
    return

print_grid()
hi('O','O')
print_grid()