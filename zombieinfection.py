'''Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour.
Find out how many hours does it take to infect all humans?

Example:

Input:
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

Output: 2

Explanation:
At the end of the 1st hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]

At the end of the 2nd hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]]
int minHours(int rows, int columns, List<List<Integer>> grid) {
	// todo
}'''
import time
print("Started")

b = [[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

def minHours(rows, columns, grid):
    '''
    hours = 0
    checker = []
    #One method
    for i in range(rows):
        for j in range(columns):
            checker.append(grid[i][j])

    while(0 in checker):
        del checker[0:]
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    if i != 0 and grid[i-1][j] == 0:
                        grid[i-1][j] = 1
                    elif j != 0 and grid[i][j-1] == 0:
                        grid[i][j-1] = 1
                    elif i != rows-1 and grid[i+1][j] == 0:
                        grid[i+1][j] = 1
                    elif j != columns-1 and grid[i][j+1] == 0:
                        grid[i][j+1] = 1
        hours +=1
        for i in range(rows):
            for j in range(columns):
                checker.append(grid[i][j]) 
    return hours
'''
    #different method
    hours = 0
    zombieList = []
    numOfSpots = rows * columns
    
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                zombieList.append([i, j])
                
    while (len(zombieList)<numOfSpots):
        for i in range(len(zombieList)):
            spot = zombieList[i]
            if spot[0] != 0 and grid[spot[0]-1][spot[1]] == 0:
                grid[spot[0]-1][spot[1]] = 1
                zombieList.append([spot[0]-1,spot[1]])
            if spot[1] != 0 and grid[spot[0]][spot[1]-1] == 0:
                grid[spot[0]][spot[1]-1] = 1
                zombieList.append([spot[0],spot[1]-1])
            if spot[0] != rows-1 and grid[spot[0]+1][spot[1]] == 0:
                grid[spot[0]+1][spot[1]] = 1
                zombieList.append([spot[0]+1,spot[1]])
            if spot[1] != columns-1 and grid[spot[0]][spot[1]+1] == 0:
                grid[spot[0]][spot[1]+1] = 1
                zombieList.append([spot[0],spot[1]+1])
        hours += 1
    return hours

hours = minHours(4,5,b)
print("Hours: %s" % hours)



