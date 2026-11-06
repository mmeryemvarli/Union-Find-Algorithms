#1
class SocialNetworkQF:
    def __init__(self, n):
        self.id = list(range(n))

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def add_friendship(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == pid:   #herkes
                self.id[i] = qid


question1 = SocialNetworkQF(6)
question1.add_friendship(0, 1)
question1.add_friendship(1, 2)
question1.add_friendship(3, 4)

print(question1.connected(0, 2))
print(question1.connected(0, 3))
print(question1.id)
#union yavaş

#2
class NetworkQU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find_root(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def connect_cable(self, p, q):
        root_p = self.find_root(p)
        root_q = self.find_root(q)
        self.parent[root_p] = root_q  #tek hamle

    def is_connected(self, p, q):
        return self.find_root(p) == self.find_root(q)


question2 = NetworkQU(6)
question2.connect_cable(0, 1)
question2.connect_cable(1, 2)

print(question2.is_connected(0, 2))
print(question2.is_connected(0, 4))
print(question2.parent)

#zincir sorunu

#3
class WeightedQU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find_root(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def connect_cable(self, p, q):
        root_p = self.find_root(p)
        root_q = self.find_root(q)

        if root_p == root_q: #p ve q'nun kökü aynıysa, zaten aynı kümedeler,fonksiyonu bitir"
            return

        if self.size[root_p] < self.size[root_q]:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        else:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]

    def is_connected(self, p, q):
        return self.find_root(p) == self.find_root(q)


question3 = WeightedQU(6)
question3.connect_cable(0, 2)
question3.connect_cable(1, 2)
question3.connect_cable(4, 5)
question3.connect_cable(1, 5)

print(question3.is_connected(0, 2))
print(question3.is_connected(0, 4))
print(question3.parent)
print(question3.size)


#4
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find_root(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def connect_root(self, p, q):
        root_p = self.find_root(p)
        root_q = self.find_root(q)
        self.parent[root_p] = root_q

    def is_connected(self, p, q):
        return self.find_root(p) == self.find_root(q)


question4 = UnionFind(11)

grid = [
    [True, True, False],
    [False, True, True],
    [False, True, False]
]

virtual_top = 9
virtual_bottom = 10

for row in range(3):
    for col in range(3):
        if not grid[row][col]:
            continue

        index = row * 3 + col

        if row == 0:
            question4.connect_root(index, virtual_top)

        if row == 2:
            question4.connect_root(index, virtual_bottom)

        if col < 2 and grid[row][col + 1]:
            question4.connect_root(index, index + 1)

        if row < 2 and grid[row + 1][col]:
            question4.connect_root(index, index + 3)

if question4.is_connected(virtual_top, virtual_bottom):
    print("Liquid is percolated")
else:
    print("Liquid does not percolate")