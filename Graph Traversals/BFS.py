from queue import Queue

q = Queue()
q.put(1)
q.put(2)
q.put(3)
# 3 2 1
print(q.get(), q.get(), q.get())
# remove 1
