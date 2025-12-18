
# n = int(input())

# matrix = []

# for _ in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# ways = []
# ways_to_process = [(0,0,1,"")]

# while ways_to_process:
#     new_paths = []
#     for i, j, product, path in ways_to_process:
#         product *= matrix[i][j]

#         if i == n-1 and j == n-1:
#             ways.append((product, path))
#         else:
#             if j+1<n:
#                 new_paths.append((i,j+1, product, path+"R"))
#             if i+1<n:
#                 new_paths.append((i+1,j,product, path+"D"))
#     ways_to_process = new_paths

# trailing_zeros = []

# # for i,j in ways:
# #     print(i,j)

# for i,j in ways:
#     num = i
#     if num == 0:
#         trailing_zeros.append((j,0))
#         break
#     count = 0 
#     while num > 0 and num % 10 == 0:
#         count += 1
#         num //= 10
#     trailing_zeros.append((j,count))

# dict_trailing_zero = dict(trailing_zeros)

# max_trailing_zeros = max(dict_trailing_zero.values())
# min_trailing_zeros = min(dict_trailing_zero.values())
# for i, j in trailing_zeros:
#     if j == 0:
#         print(0)
#         print(i)
#         break
#     if j < max_trailing_zeros and j == min_trailing_zeros:
#         print(j)
#         print(i)
#         break
    
# # This above solutions work but failed at test 11 since memory limit exceed when n= 20 which requires path of 3.5 billions which is beyond the capability of even fastest computer

import sys

def count_factor(num:int, factor:int) -> int:
    if num == 0:
        return INF
    cnt = 0
    while num % factor == 0:
        cnt += 1
        num //= factor
    return cnt

def reconstruct_path(n: int, dir_table:list) -> str:
    path = []
    i,j = n-1, n-1

    while i > 0 or j > 0 :
        if dir_table[i][j] == 'D':
            path.append('D')
            i -= 1
        else: 
            path.append('R')
            j -= 1

    path.reverse()

    return ''.join(path)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    n = int(data[0])
    idx = 1
    grid = []

    for _ in range(n):
        row = list(map(int, data[idx:idx+n]))
        idx += n
        grid.append(row)

    global INF
    INF = 10**9

    twos = [[0]*n for _ in range(n)]
    fives = [[0]*n for _ in range(n)]
    has_zeros = False
    zero_row = zero_col = -1

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                has_zeros = True
                zero_col, zero_row = i, j
                twos[i][j] = INF
                fives[i][j] = INF
            else:
                twos[i][j] = count_factor(grid[i][j], 2)
                fives[i][j] = count_factor(grid[i][j], 5)

    dp2 = [[INF] * n for _ in range(n)]
    dp5 = [[INF] * n for _ in range(n)]
    dir2 = [[''] * n for _ in range(n)]
    dir5 = [[''] * n for _ in range(n)]

    dp2[0][0] = twos[0][0]
    dp5[0][0] = fives[0][0]

    # DP to minimize 2s
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue

            if i > 0:
                from_above = dp2[i-1][j]
            else:
                from_above = INF

            
            if j > 0:
                from_left = dp2[i][j-1]
            else:
                from_left = INF

            if from_above < from_left:
                dp2[i][j] = from_above + twos[i][j]
                dir2[i][j] = 'D'
            elif j > 0:
                dp2[i][j] = from_left + twos[i][j]
                dir2[i][j] = 'R'

    # DP to minimize 5s
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue

            if i > 0:
                from_above = dp5[i-1][j]
            else:
                from_above = INF

            if from_above < from_left:
                dp5[i][j] = from_above + fives[i][j]
                dir5[i][j] = 'D'
            
            elif i > 0:
                dp5[i][j] = from_left + fives[i][j]
                dir5[i][j] = 'R'

    path1_twos = dp2[n-1][n-1]

    i,i = n-1,n-1
    path1_fives = fives[i][j]
    while i > 0 or j > 0:
        if dir2[i][j] == 'D':
            i -= 1
        else:
            j -= 1
        path1_fives +=fives[i][j]

    if path1_twos >= INF or path1_fives >= INF:
        zeros1 = INF
    else:
        zeros1 = min(path1_twos, path1_fives)
    
    path2_fives = dp5[n-1][n-1]
    
    i,j = n-1, n-1
    path2_twos = twos[i][j]
    while i > 0 or j > 0:
        if dir5[i][j] == 'D':
            i -= 1
        else:
            j -= 1
        path2_twos += twos[i][j]

    if path2_twos >= INF or path2_fives >= INF:
        zeros2 = INF
    else:
        zeros2 = min(path2_twos, path2_fives)
    
    best_zeros = min(zeros1, zeros2)

    if has_zeros and best_zeros > 1:
        print(1)

        path = []

        for _ in range(zero_col):
            path.append('R')
        for _ in range(n-1):
            path.append('D')
        for _ in range(zero_col, n-1):
            path.append('R')
        print(''.join(path))
        return
    
    if zeros1 <= zeros2:
        best_path = reconstruct_path(n, dir2)
    else:
        best_path = reconstruct_path(n, dir5)

    if best_zeros >= INF:
        best_zeros = 1
        if has_zeros:
            best_path = []
            for _ in range(zero_col):
                best_path.append('R')
            for _ in range(n-1):
                best_path.append('D')
            for _ in range(zero_col, n-1):
                best_path.append('R')
            best_path = ''.join(best_path)

    print(best_zeros)
    print(best_path)

if __name__ == "__main__":
    main()

# This solutions was suggested by deepseek which failed in test number 17 due to memory limit. 

# This problem is rated as 2000 so leave it and come later once you reach that level. 








            

