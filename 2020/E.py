tme = 0
tmt = 0
tempo = 0

n = int(input())

for i in range(n):
    a, b = list(map(int, input().split()))
    tme += (tempo - a)
    tempo += b
    tmt += (tempo - a)

print(f"TME: {tme/n:.1f}")
print(f"TMT: {tmt/n:.1f}")
    