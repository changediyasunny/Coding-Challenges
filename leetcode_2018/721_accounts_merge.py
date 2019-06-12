"""
721. Accounts Merge

Given a list accounts, each element accounts[i] is a list of strings, where the
first element accounts[i][0] is a name, and the rest of the elements are emails
representing emails of the account.
Now, we would like to merge these accounts. Two accounts definitely belong to the
same person if there is some email that is common to both accounts. Note that even
if two accounts have the same name, they may belong to different people as people
could have the same name. A person can have any number of accounts initially, but
all of their accounts definitely have the same name.
After merging the accounts, return the accounts in the following format: the first
element of each account is the name, and the rest of the elements are emails in
sorted order. The accounts themselves can be returned in any order.

Example 1:
Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]

Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']]
would still be accepted.

"""


"""
Draw an edge between two emails if they occur in the same account. The problem comes
down to finding connected components of this graph.

Algorithm:
For each account, draw the edge from the first email to all other emails. Additionally,
we'll remember a map from emails to names on the side. After finding each connected
component using a depth-first search, we'll add that to our answer.
"""
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        graph = collections.defaultdict(set)
        email_to_acc = {}
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[email].add(acc[1])
                graph[acc[1]].add(email)
                email_to_acc[email] = name

        visited = set()
        result = []
        for email in graph:
            if email not in visited:
                visited.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in visited:
                            visited.add(nei)
                            stack.append(nei)
                result.append([email_to_acc[email]] + sorted(component))
        return result
