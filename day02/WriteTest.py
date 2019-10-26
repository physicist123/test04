def writeMethod():
    some_sentences = '''\
I love learning python
because python is fun
and also easy to use
'''
    f = open("sentence.txt", "w")
    f.write(some_sentences)
    f.close()


# writeMethod()

g = open("sentence.txt")
while True:
    line=g.readline()
    if len(line) == 0:
        break
    print(line)
g. close()
