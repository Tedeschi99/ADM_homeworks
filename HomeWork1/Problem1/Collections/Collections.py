#collections.Counter()
from collections import Counter

X = int(input())
shoes = Counter(map(int, input().split()))

N = int(input())
earnings = 0

for _ in range(N):
    size, price = map(int, input().split())

    if shoes[size] > 0:
        earnings += price
        shoes[size] -= 1

print(earnings)

#DefaultDict Tutorial
from collections import defaultdict

n, m = map(int, input().split())

positions = defaultdict(list)

# Lettura del gruppo A
for i in range(1, n + 1):
    word = input()
    positions[word].append(i)

# Lettura del gruppo B
for _ in range(m):
    word = input()

    if word in positions:
        print(*positions[word])
    else:
        print(-1)

#