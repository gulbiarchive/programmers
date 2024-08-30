def solution(n):
    prime = []

    for i in range(1, n + 1):
        if n % i == 0:
            prime.append(i)
    
    return sum(prime)

print(solution(int(input())))