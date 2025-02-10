import heapq

blockchain = []
balance = {0: 10, 1: 10, 2: 10}
#mapping for ports to id but we just use 900012 hard mapped for now
users = {}
metime = 0 #lamport time
requests = [] #priority queue for requests


heapq.heappush(requests, (0, 1, 0))
heapq.heappush(requests, (1, 2, 0))
heapq.heappush(requests, (0, 0, 0))
heapq.heappush(requests, (2, 1, 0))
heapq.heappush(requests, (1, 1, 0))

while requests:
    print(heapq.heappop(requests))