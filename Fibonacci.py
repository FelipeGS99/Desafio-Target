num = int(input('Digite um número: '))
fibonacci = [0, 1]
i = 0
while fibonacci[i] < num:
    fibonacci.append(fibonacci[i] + fibonacci[i + 1])
    i += 1
print(fibonacci)
if num in fibonacci:
    print("O número digitado pertence a sequência de fibonacci")
else:
    print("O número digitado não pertence a sequência de fibonacci")   