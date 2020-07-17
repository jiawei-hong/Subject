def f(g, n, array):
    numberSum = 0

    for i in range(g):
        if n + i + 1 < len(array):
            if array[n + i + 1].isnumeric():
                numberSum += int(array[n + i + 1])
            else:
                numberSum += 10

    return numberSum


output = open('./output.txt', 'w')

for q in range(2):
    f = open(f'./in{str(q + 1)}.txt')
    n = f.readline()

    for i in range(int(n)):
        data = f.readline().replace('\n', '').split(' ')
        answer = 0

        for j in range(len(data)):
            if data[j] == 'X':
                answer += 10
                answer += f(2, j, data)
            elif data[j] == '/':
                answer += 10
                answer -= int(data[j - 1])
                answer += int(f(1, j, data))
            else:
                answer += int(data[j])

        output.write(str(answer) + '\n')
    output.write('\n')