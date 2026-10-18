#Introduction to Sets

def average(array):
    unique = set(array)
    return round(sum(unique) / len(unique), 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#Symmetric Difference

if __name__ == '__main__':
    m = int(input())
    M = set(map(int, input().split()))

    n = int(input())
    N = set(map(int, input().split()))

    result = sorted(M.symmetric_difference(N))

    for x in result:
        print(x)

#Set .add()
if __name__ == '__main__':
    N = int(input())
    countries = set()

    for _ in range(N):
        country = input()
        countries.add(country)

    print(len(countries))

#Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    command = input().split()

    if command[0] == "pop":
        s.pop()

    elif command[0] == "remove":
        s.remove(int(command[1]))

    elif command[0] == "discard":
        s.discard(int(command[1]))

print(sum(s))