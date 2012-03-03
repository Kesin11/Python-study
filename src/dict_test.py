from multiprocessing import Queue
q = Queue(10)
list=[]
dict={}
for i in range(0, 100, 10):
    dict['num'] = i
    q.put(dict.copy())
while not q.empty():
    list.append(q.get())
for part_list in list:
    print part_list.get('num')
