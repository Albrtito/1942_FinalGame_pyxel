enemy_1 = [1, 2, 3, 4]
enemy_2 = [1, 2]
enemy_3 = [3, 4]
enemy_4 = [5, 7]
enemy_global = [enemy_1, enemy_2, enemy_3, enemy_4]
iterations_1 = 0
for index_global in enemy_global:
    iterations_1 += 1
    for index_local in index_global:
        iterations_1 += 1



enemy_global_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
iterations_2 = 0
for index in enemy_global_2:
    iterations_2 += 1

print(iterations_1, ":1: vs :2: ", iterations_2)
