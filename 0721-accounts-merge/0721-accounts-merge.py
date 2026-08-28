class DSU:
    def __init__(self, emails):
        self.parent = {email: email for email in emails}
        self.rank = {email: 0 for email in emails}

    def find(self, email):
        if self.parent[email] != email:
            self.parent[email] = self.find(self.parent[email])
        return self.parent[email]

    def union(self, x, y):
        pX = self.find(x)
        pY = self.find(y)

        if pX == pY:
            return False

        if self.rank[pX] > self.rank[pY]:
            self.parent[pY] = pX

        elif self.rank[pY] > self.rank[pX]:
            self.parent[pX] = pY

        else:
            self.parent[pY] = pX
            self.rank[pX] += 1

        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToName = {}

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                emailToName[email] = name
        
        dsu = DSU(emailToName.keys())

        for account in accounts:
            firstEmail = account[1]

            for email in account[2:]:
                dsu.union(firstEmail, email)
        
        groups = defaultdict(list)

        for email in emailToName:
            root = dsu.find(email)
            groups[root].append(email)
        
        result = []
        for root, emails in groups.items():
            emails.sort()
            result.append([emailToName[root]] + emails)
        
        return result


