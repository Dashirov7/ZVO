def c_text(t):
    s = []
    with open(t, 'r') as f:
        for word in f.read().split():
            if word.startswith('c') or word.startswith('C'):
                s.append(word)
    return s
print(c_text('text.txt'))