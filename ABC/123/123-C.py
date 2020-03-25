N = int(input())
T_list = [int(input()) for i in range(5)]

T_min = min(T_list)

print( (N+T_min-1) // T_min + 4)