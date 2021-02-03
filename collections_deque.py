import collections

deq = collections.deque([0, 1, 2, 3])
print(deq)
deq.append(4)
print(deq)
deq.appendleft(-1)
print(deq)

elem = deq.popleft()
print(elem)
print(deq)

deq.rotate(-2)
print(deq)


deq_1 = collections.deque([0, 1, 2, 3], maxlen=4)
print(deq_1)
deq_1.append(5)
print(deq_1)