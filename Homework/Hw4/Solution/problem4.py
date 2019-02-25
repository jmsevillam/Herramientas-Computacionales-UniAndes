def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        prev_line = pascal(n-1)
        for i in range(len(prev_line)-1):
            line.append(prev_line[i] + prev_line[i+1])
        line += [1]
    return line
w=1
print(pascal(5))
