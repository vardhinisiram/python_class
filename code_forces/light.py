n1 = [int(x) for x in input().split()]
n2 = [int(x) for x in input().split()]
n3 = [int(x) for x in input().split()] 
n = n1 + n2 + n3
initial_state=[1,1,1,1,1,1,1,1,1]
change_dict={
    0:[0, 1, 3, 4], 
    1: [0, 1, 2, 3, 4, 5],
    2:[1, 2, 4, 5], 
    3:[0, 1, 3, 4, 6, 7], 
    4:[0, 1, 2, 3, 4, 5, 6, 7, 8], 
    5:[1, 2, 4, 5, 7, 8], 
    6:[3, 4, 6, 7], 
    7:[3, 4, 5, 6, 7, 8], 
    8:[4, 5, 7, 8], 
}

for index, val in enumerate(n):
    if val % 2 == 0:
        continue
    else:
        change_indices = change_dict[index]
        for ch_i in change_indices:
            # if n[ch_i] == 1:
            #     n[ch_i] = 0
            # else:
            #     n[ch_i] = 1
            # n[ch_i] = 0 if n[ch_i] == 1 else 1
            initial_state[ch_i]=(initial_state[ch_i]-1)*(-1)
for i in range(1, 10):
    print(initial_state[i-1], end = " ")
    if i % 3 == 0:
        print()
