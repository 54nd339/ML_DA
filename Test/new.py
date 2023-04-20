import sys
import re
import random
import copy
import math

# Check if cell (x, y) is valid or not
def is_valid_cell(x, y, N, M):
    if x < 0 or y < 0 or x >= N or y >= M or grid[x][y] == '':
        return False

    return True

def find_paths_util(maze, source, destination, visited, path, paths):
  """Find paths using Breadth First Search algorithm """
  # Done if destination is found
  if source == destination:
    paths.append(path[:])  # append copy of current path
    return

  # mark current cell as visited
  N = len(maze)
  M = len(maze[0])
  x, y = source
  visited[x][y] = True

  # if current cell is a valid and open cell, 
  if is_valid_cell(x, y, N, M) and maze[x][y]:
    # Using Breadth First Search on path extension in all direction

    # go right (x, y) --> (x + 1, y)
    if x + 1 < N and (not visited[x + 1][y]):
      path.append((x + 1, y))
      find_paths_util(maze,(x + 1, y), destination, visited, path, paths)
      path.pop()

    # go left (x, y) --> (x - 1, y)
    if x - 1 >= 0 and (not visited[x - 1][y]):
      path.append((x - 1, y))
      find_paths_util(maze, (x - 1, y), destination, visited, path, paths)
      path.pop()

    # go up (x, y) --> (x, y + 1)
    if y + 1 < M and (not visited[x][y + 1]):
      path.append((x, y + 1))
      find_paths_util(maze, (x, y + 1), destination, visited, path, paths)
      path.pop()

    # go down (x, y) --> (x, y - 1)
    if y - 1 >= 0 and (not visited[x][y - 1]):
      path.append((x, y - 1))
      find_paths_util(maze, (x, y - 1), destination, visited, path, paths)
      path.pop()

    # Unmark current cell as visited
  visited[x][y] = False

  return paths

def find_paths(maze, source, destination):
  """ Sets up and searches for paths"""
  N = len(maze)
  M = len(maze[0])

  # 2D matrix to keep track of cells involved in current path
  visited = [[False]*M for _ in range(N)]

  path = [source]
  paths = []
  paths = find_paths_util(maze, source, destination, visited, path, paths)

  return paths

def calc_adj(grid):
    """"find the adjacency of each cell"""
    twoD = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            c = 0
            if j-1>=0 and grid[i][j-1]=='':
                c+=1
            if i+1 < len(grid) and grid[i+1][j] == '':
                c+=1
            if j+1 < len(grid[0]) and grid[i][j+1] == '':
                c+=1
            if i-1 >=0 and grid[i-1][j] == '':
                c+=1
                
            twoD[i][j] = c
            
    return twoD

def adjacent_vacant(twoD, q, grid):
    """"check if a qubit have vacant adjacent pos"""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if twoD[i][j] == q:
                if j-1>=0 and grid[i][j-1]=='':
                    return True, i, j
                if i+1 < len(grid) and grid[i+1][j] == '':
                    return True, i, j
                if j+1 < len(grid[0]) and grid[i][j+1] == '':
                    return True, i, j
                if i-1 >=0 and grid[i-1][j] == '':
                    return True, i, j
                
    return False, -1, -1

def get(ad, n, grid):
    """get pos if it has vacant adjacent location"""
    for i in range(len(ad)):
        for j in range(len(ad[0])):
            if ad[i][j]==n:
                adjacent_empty, x, y = adjacent_vacant(ad, n, grid)
                print(adjacent_empty, x, y)
                if adjacent_empty:
                    return True, x, y
                
    return False, -1, -1

def get_pos(twoD, n):
    """get position of an element in 2D matrix"""
    for i in range(len(twoD)):
        for j in range(len(twoD[0])):
            if twoD[i][j]==n:
                return i,j

def place_qubit(grid, q, qubit_pri,twoD):
    print(qubit_pri)
##    print(ad)
    print('a'+str(q+1))
    row_mid = len(grid)//2
    col_mid = len(grid[0])//2
##    print(grid)
    if grid[row_mid][col_mid]=='':
        grid[row_mid][col_mid] = 'a'+str(q+1)
        twoD[row_mid][col_mid] = -1
        return grid
    
    max_ele = 0
    for i in range(len(twoD)):
        for j in range(len(twoD[0])):
            if twoD[i][j]>max_ele:
                max_ele = twoD[i][j]
                i_r, i_c = i, j
    max_count = 0
    for i in range(len(twoD)):
        for j in range(len(twoD[0])):
            if twoD[i][j] == max_ele:
                max_count += 1
    
    f = 0
    
    print(twoD)
    print(max_count)
    print(i_r,i_c)
    if grid[i_r][i_c] == '' and max_count == 1:
        print("isme")
        grid[i_r][i_c] = 'a'+str(q+1)
        twoD[i_r][i_c] = -1
        return grid

    adjacent_empty, x, y = get(ad, twoD[i_r][i_c]+1, grid)
    print(adjacent_empty, x, y)
    if adjacent_empty:
        if y-1 >=0 and grid[x][y-1] == '':
            grid[x][y-1] = 'a'+str(q+1)
            twoD[x][y-1] = -1
            return grid
        if x+1 < len(grid) and grid[x+1][y] == '':
            grid[x+1][y] = 'a'+str(q+1)
            twoD[x+1][y] = -1
            return grid
        if y+1 < len(grid[0]) and grid[x][y+1] == '':
            grid[x][y+1] = 'a'+str(q+1)
            twoD[x][y+1] = -1
            return grid
        if x-1 >=0 and grid[x-1][y] == '':
            grid[x-1][y] = 'a'+str(q+1)
            twoD[x-1][y] = -1
            return grid
    if not adjacent_empty:
        for k in qubit_pri[::-1]:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if k == grid[i][j]:
                        if j-1 >=0 and grid[i][j-1] == '':
                            grid[i][j-1] = 'a'+str(q+1)
                            twoD[i][j-1] = -1
                            return grid
                        if i+1 < len(grid) and grid[i+1][j] == '':
                            grid[i+1][j] = 'a'+str(q+1)
                            twoD[i+1][j] = -1
                            return grid
                        if j+1 < len(grid[0]) and grid[i][j+1] == '':
                            grid[i][j+1] = 'a'+str(q+1)
                            twoD[i][j+1] = -1
                            return grid
                        if i-1 >=0 and grid[i-1][j] == '':
                            grid[i-1][j] = 'a'+str(q+1)
                            twoD[i-1][j] = -1
                            return grid
    return grid

def check_adjacency(grid, c, t):
    """checks if two qubits are adjacent"""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == c:
                if j-1 >= 0 and grid[i][j-1] == t:
                    return True
                elif j+1 < len(grid[0]) and grid[i][j+1] == t:
                    return True
                elif i-1 >= 0 and grid[i-1][j] == t:
                    return True
                elif i+1 < len(grid) and grid[i+1][j] == t:
                    return True
                
    return False

def gen_combo(s):
    """fenerates combination for swap gate insertion"""
    for i in range(s + 1):
        s2 = s - i
        yield (i, s2)

def interaction_frequency(qubit, line):
    interactions = l[int(qubit)-1]
    count=0
    tot_int=0
    for i in interactions:
        if(i>line):
            tot_int+=i
            
        else:
            count+=1
            
##    print(tot_int)
##    print(count)
    try:
        interval=interactions[-1] - interactions[count]
        lookahead_freq = tot_int/interval
    except ZeroDivisionError:
        lookahead_freq=tot_int/interactions[-1]
    except IndexError:
        lookahead_freq=1
##    print(lookahead_freq)
    return lookahead_freq

def rearrange_grid(grid, q, t, line):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == q:
                a,b = i,j
            elif grid[i][j] == t:
                c,d = i,j

    source = (a,b)
    destination = (c,d)
    paths = find_paths(grid, source, destination)
    
    minPath = []
    p = sys.maxsize
    for path in paths:
        if len(path) < p:
            p = len(path)
    for path in paths:
        if len(path)==p:
            minPath.append(path)
    print(minPath)

    freq_for_each_path={}
    for path in minPath:
        path_int_freq=0
        for qubit in path:
##            print("273line", re.findall('\d+', grid[qubit[0]][qubit[1]])[0], line)
            path_int_freq += interaction_frequency(re.findall('\d+', grid[qubit[0]][qubit[1]])[0], line)
        freq_for_each_path[tuple(path)]=path_int_freq
    print(freq_for_each_path)
    min_freq=min(freq_for_each_path.values())
    print(min_freq)

    myPath = list(filter(lambda x: freq_for_each_path[x] == min_freq, freq_for_each_path))[0]
    print(myPath)
    
##    myPath = random.choice(minPath)
##    print(myPath)

    myPath_len = len(myPath)
    swap_ways_number = myPath_len - 2
    ways = list(gen_combo(swap_ways_number))
    print(ways)
    my_way = random.choice(ways)
    print(my_way)
    swap_source, swap_destination = my_way

    f = 0
    for i in range(swap_source):
        grid[myPath[i][0]][myPath[i][1]], grid[myPath[i+1][0]][myPath[i+1][1]] = grid[myPath[i+1][0]][myPath[i+1][1]], grid[myPath[i][0]][myPath[i][1]]
        f += 1

    j = myPath_len - 1
    for i in range(swap_destination):
        grid[myPath[j][0]][myPath[j][1]], grid[myPath[j-1][0]][myPath[j-1][1]] = grid[myPath[j-1][0]][myPath[j-1][1]], grid[myPath[j][0]][myPath[j][1]]
        j -= 1
        f += 1

    f=int(math.ceil(0.8*f))
    print(grid)
    
    return grid, f

with open('decod24-v3_46.real','r') as f:
    data = f.read()
##print(data)
qubits = int(re.search(r".numvars ([\d]*)", data).group(1))
print(qubits)

gates = re.search(r"(?s)(?<=.begin).*?(?=.end)", data, re.MULTILINE).group(0)
##print(gates.strip())

lines = gates.strip().split('\n')
print(len(lines))

l=[[] for i in range(qubits)]
c=1
for line in lines:
    timestamp = line.split(' ')
##    print(timestamp)
    for gate in range(1,len(timestamp)):
##        print(timestamp[gate])
        i = re.search(r"\d+(\.\d+)?", timestamp[gate]).group(0)
##        print(int(i))
        l[int(i)-1].append(c)
##        print(l)
    c+=1
print(l)

int_freq=[]
for interactions in l:
    if len(interactions) == 0:
        int_freq.append(0)
        continue
    int_freq.append(sum(interactions)/(max(interactions)-min(interactions)))
print(int_freq)

grid = [['' for i in range(2)] for j in range(3)]
twoD = calc_adj(grid)
ad = copy.deepcopy(twoD)
##print(ad)

qubit_pri = []

for i in range(qubits):
    max_freq = max(int_freq)
    its_index = int_freq.index(max_freq)
##    print(max_freq, its_index)
    qubit_pri.append('a'+str(its_index+1))
    grid = place_qubit(grid, its_index, qubit_pri, twoD)
    
    print(grid)
    int_freq[its_index] = -1
##print(int_freq)

swap_count = 0
line_no=0
for line in lines:
    line_no+=1
    timestamp = line.split(' ')
##    line_no=re.findall('\d+', str(timestamp[:1]))[0]

    gate=timestamp[1:]
    print("line_no.", line_no)
    print("gate", gate)
    if len(gate)>1:
        adjacent = check_adjacency(grid, gate[0],gate[1])
        print(adjacent)
        if not adjacent:
            grid, swap = rearrange_grid(grid, gate[0], gate[1], line_no)
##            print(grid)
            swap_count += swap


print("Swap count ", swap_count)