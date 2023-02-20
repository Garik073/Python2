N = list(int(i) for i in input().split())
n_min, n_max = (int(input()) for _ in 'ab')
print(list(i for i in range(len(N)) if N[i] in range(n_min, n_max + 1)))