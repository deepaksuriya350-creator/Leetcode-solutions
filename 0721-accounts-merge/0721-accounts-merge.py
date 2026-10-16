from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts):
        par=list(range(len(accounts)))
        def find(x):
            while par[x]!=x: par[x]=par[par[x]]; x=par[x]
            return x
        eid={}
        for i,acc in enumerate(accounts):
            for email in acc[1:]:
                if email in eid: par[find(i)]=find(eid[email])
                else: eid[email]=i
        merged=defaultdict(set)
        for i,acc in enumerate(accounts):
            for email in acc[1:]: merged[find(i)].add(email)
        return [[accounts[r][0]]+sorted(e) for r,e in merged.items()]