# https://leetcode.com/problems/accounts-merge/

# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name,
# and the rest of the elements are emails representing emails of the account.

# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Explanation:
# The first and second John's are the same person as they have the common email "johnsmith@mail.com".
# The third John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

from collections import defaultdict


class Solution_DFS:

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        email_to_account = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_account[email].append(i)

        result = []
        visited = [False for _ in range(len(accounts))]

        def dfs(i):
            emails = set()

            if visited[i]:
                return emails
            visited[i] = True

            for email in accounts[i][1:]:
                emails.add(email)
                for account in email_to_account[email]:
                    emails |= dfs(account)
            return emails

        for i, account in enumerate(accounts):
            emails = dfs(i)
            if emails:
                result.append([account[0]] + sorted(list(emails)))
        return result


class UnionFind:
    def __init__(self):
        self.parent = {}

    def union(self, a, b):
        find_a = self.find(a)
        find_b = self.find(b)
        if find_a == find_b:
            return
        self.parent[find_b] = find_a

    def find(self, a):
        if self.parent[a] == a:
            return self.parent[a]
        return self.find(self.parent[a])


class Solution_UF:

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        names = {}
        emails = {}
        unionfind = UnionFind()
        for acc in accounts:
            person = acc[0]
            id = len(names)
            names[id] = person
            for email in acc[1:]:
                emails[email] = id
                if email not in unionfind.parent:
                    unionfind.parent[email] = email
            for email1, email2 in zip(acc[1:], acc[2:]):
                unionfind.union(email1, email2)

        merged = defaultdict(list)

        for email in emails:
            id = emails[unionfind.find(email)]
            merged[id].append(email)
        return [[names[id]] + sorted(merged[id]) for id in names if merged[id]]


def main():
    accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"]]

    S = Solution_UF()
    print(S.accountsMerge(accounts))


if __name__ == "__main__":
    main()