def validPath(n: int, e: List[List[int]], s: int, d: int) -> bool:
    graph = collections.defaultdict(list)
    for u, v in e:
        graph[u].append(v)
        graph[v].append(u)
    def dfs(node, visit):
        if node == d:
            return True 
        visit.add(node)
        for i in graph[node]:
            if i not in visit:
                if dfs(i, visit):
                    return True
        return False 
    return "true" if dfs(s, set()) else "false"

f = open('user.out', 'w')
for l1,l2,l3,l4 in zip(stdin,stdin,stdin,stdin):
    #inp1,inp2,inp3,inp4 = loads(l1),loads(l2),loads(l3),loads(l4)  
    f.write(f'{validPath(loads(l1),loads(l2),loads(l3),loads(l4))}\n')
f.flush()
exit(0)