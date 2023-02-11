import collections 

class Solution:
    def numberOfGoodPaths(self, vals, edges) -> int:
        def find(i):
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]

        n = len(vals)
        p = list(range(n))
        count = [collections.Counter({vals[i]:1}) for i in range(n)]
        edges = sorted((max(vals[i],vals[j]),i,j) for i,j in edges)
        res = n
       
        for val, i, j in edges:
            pi, pj = find(i), find(j)
            res += count[pi][val]*count[pj][val]
            p[pi] = pj
            count[pj][val] += count[pi][val]
        return res
        
vals = [1,3,2,1,3]
edges = [[0,1],[0,2],[2,3],[2,4]]

sol = Solution()
sol.numberOfGoodPaths(vals, edges)

""" v2ids = collections.defaultdict(list)
        for i, v in enumerate(vals):
            v2ids[v].append(i)
        print(v2ids)
        seeds = []
        for k, v in v2ids.items():
            if len(v) == 2:
                seeds.append(v[0])
                continue
            if len(v) > 2:
                seeds.extend(v)
        
        mp = collections.defaultdict(list)
        for start, end in edges:
            mp[start].append(end)
            mp[end].append(start)
        
        def bfs(sid):
            seen = set()
            res = set()
            q = collections.deque()
            target = vals[sid]
            q.append(sid)
            while q:
                curid = q.popleft()
                if curid != sid and vals[curid] == target:
                    res.add((sid, curid))
                for ngb in mp[curid]:
                    seen.add(ngb)
                    if vals[ngb] <= target:
                        q.append(ngb)
            return res
        
        res = set()
        for seed in seeds:
            curres = bfs(seed)
            res.union(curres)
        return len(vals) + len(res)




return 0 """