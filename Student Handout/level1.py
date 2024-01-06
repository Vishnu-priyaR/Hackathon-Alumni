import sys
import json
class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]
		self.visited=[]
		self.cost=0
		self.current_capacity=0
	def printSolution(self, dist):
		min1=float('inf')
		val=0
		for i in range(self.V):
		   if dist[i]==0:
		        continue
		   else:
		        if dist[i]<min1 and (i not in self.visited):
		            val=i
		            min1=dist[i]
		self.cost+=min1
		self.visited.append(val)      
	def minDistance(self, dist, sptSet):
		min = sys.maxsize
		minc = sys.maxsize
		for u in range(self.V):
			#print(dist[u],min,capacity[u],minc)
			if dist[u] < min and capacity[u] < minc and sptSet[u] == False :
				min = dist[u]
				min_index = u
				minc=capacity[u]
		return min_index
	def dijkstra(self, src):
		dist = [sys.maxsize] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):
			x = self.minDistance(dist, sptSet)
			sptSet[x] = True
			for y in range(self.V):
				if self.graph[x][y] > 0 and sptSet[y] == False and \
						dist[y] > dist[x] + self.graph[x][y]:
					dist[y] = dist[x] + self.graph[x][y]

		self.printSolution(dist)

output={}
dist,capacity=[],[]
with open('level1a.json') as user_file:
  f= json.load(user_file)
for v in range(len(f['vehicles'])):
  max_capacity=f['vehicles']['v'+str(v)]['capacity']
  r=[f['restaurants'][f['vehicles']['v'+str(v)]['start_point']]['neighbourhood_distance']]
  for i in range(0,20):
    dist.append(f['neighbourhoods']['n'+str(i)]['distances'])
    capacity.append(f['neighbourhoods']['n'+str(i)]['order_quantity'])
print(capacity)
#print(max_cap,capacity)
g = Graph(20)
g.graph=dist

min1=r[0].index((min(r[0])))
g.visited.append(min1)
g.cost=r[0][g.visited[-1]]
g.dijkstra(min1)
for i in range(1,len(g.graph)-1):
    g.dijkstra(g.visited[-1])
    #print(capacity[g.visited[-1]])
g.cost+=r[0][g.visited[-1]]
g.current_capacity = max_capacity - capacity[min1]
print(g.current_capacity)
g.dijkstra(min1)

for i in range(1, len(g.graph)-1):
    if g.current_capacity == 0:
        g.visited.append(0)
        g.cost += r[0][0]
        g.current_capacity = max_capacity-capacity[0]
        print(g.visited)
    print(g.current_capacity)
    if g.current_capacity <= 0:
        g.visited.append(0)
        g.current_capacity = max_capacity-capacity[0]
        g.cost += r[0][0]
    g.dijkstra(g.visited[-1])
    g.current_capacity -= capacity[g.visited[-1]]
g.cost += r[0][g.visited[-1]]
print(g.visited)
for i in range(len(g.visited)):
    if g.visited[i] == 0:
        
        g.visited[i] = "r"+str(g.visited[i])
    else:
        g.visited[i] = "n"+str(g.visited[i])
#output = {'v'+str(v): {"path": ["r0"]+g.visited+["r0"]}}
print(g.visited,g.current_capacity)

for i in range(len(g.visited)):
    g.visited[i]="n"+str(g.visited[i])
    output.update({'v'+str(v):{"path":["r0"]+g.visited+["r0"]}})
print(output)
#with open("level0_output.json", "w") as outfile:
    #json.dump(output, outfile)
