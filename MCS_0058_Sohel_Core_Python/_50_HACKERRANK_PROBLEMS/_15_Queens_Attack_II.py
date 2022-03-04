def queensAttack(n, k, r_q, c_q, obstacles):
    total = 0
    #moving right, i same j increase
    i = r_q
    j = c_q+1
    while(j <= n):
        pos = [i,j]
        if(pos not in obstacles):
            total += 1
        else:
            break
        j += 1
    print("total 1 : ",total)    
    #moving left, i same j decrease
    i = r_q
    j = c_q-1
    while(j >= n):
        pos = [i,j]
        if(pos not in obstacles):
            total += 1
        else:
            break 
        j -= 1
    print("total 2 : ",total)
    #moving up, j same i increase
    i = r_q+1 
    j = c_q
    while(i <= n):
        pos = [i,j]
        if(pos not in obstacles):
            total += 1
        else:
            break
        i += 1
    print("total 3 : ",total)
    #moving down, j same i decrease
    i = r_q-1 
    j = c_q
    while(i >= n):
        pos = [i,j]
        if(pos not in obstacles):
            total += 1
        else:
            break
        i -= 1
    print("total 4 : ",total)
    #moving up right,i increase j increase 
    i = r_q+1
    j = c_q+1
    while(i <= n and j <= n):
        pos = [i,j]
        if(pos not in obstacles):
            total += 1
        else:
            break
        i += 1
        j += 1
    print("total 5 : ",total)
    #moving down left, i decrease j decrease
    i = r_q-1
    j = c_q-1
    while(i >= n and j >= n):
        pos = [i,j]
        if(pos not in obstacles):
            total += 1
        else:
            break
        i -= 1
        j -= 1
    print("total 6 : ",total)
    #moving up left, i increase j decrease   
    i = r_q+1
    j = c_q-1
    while(i <= n and j >= n):
        pos = [i,j]
        if(pos not in obstacles):
            total += 1
        else:
            break
        i += 1
        j -= 1    
    print("total 7 : ",total)
    #moving down right, i decrease j increase
    i = r_q-1
    j = c_q+1
    while(i >= n and j <= n):
        pos = [i,j]
        if(pos not in obstacles):
            total += 1
        else:
            break
        i -= 1
        j += 1
    print("total 8 : ",total)

    return total

    

n = 5
k = 3
r_q = 4
c_q = 3
obstacles = [[5,5],[4,2],[2,3]]
print(queensAttack(n, k, r_q, c_q, obstacles))