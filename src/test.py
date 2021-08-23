from random import randint

yes = ['X', 'O', ' ', ' ']
grid = [yes[randint(0,3)] for _ in range(9)]

def print_grid():
    for r in range(3):    
        print("     " + str(grid[3*r+0]) + " | " + str(grid[3*r+1]) + " | " + str(grid[3*r+2]))
        if r < 2: print("    -----------")
    print('\n\n')

def hi(i,j):
    for n in range(2):
        a = [grid[(2*n+2*(2-n)*x)] for x in range(3) if grid[(2*n+2*(2-n)*x)] == i]
        g = [grid[(2*n+2*(2-n)*x)] for x in range(3)]
        if i in g and ' ' in g and len(set(a)) < len(a):
            grid[3*g.index(" ")+n] = j
   
    for n in range(3):
        a = [grid[3*n+x] for x in range(3) if grid[3*n+x] == i]
        g = grid[3*n:3*n+3]
        if i in g and ' ' in g and len(set(a)) < len(a):
            grid[g.index(" ")+3*n] = j
            return
    
    for n in range(3):
        a = [grid[n+3*x] for x in range(3) if grid[n+3*x] == i]
        g = [grid[n+3*x] for x in range(3)]
        if i in g and ' ' in g and len(set(a)) < len(a):
            grid[3*g.index(" ")+n] = j
            return
    
    if (i,j) == ('O','X'): hi('X','O')
    return

print_grid()
hi('O','O')
print_grid()