class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self
        self.rank = 0


def make_set(key):
    return Node(key)


def find_set(x):
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent


def union(x, y):
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


Z = []

for i in range(10):
    Z.append(make_set(i))

# union(find_set(Z[0]), find_set(Z[1]))
# union(find_set(Z[2]), find_set(Z[3]))
# union(find_set(Z[1]), find_set(Z[2]))
# union(find_set(Z[5]), find_set(Z[6]))
# union(find_set(Z[7]), find_set(Z[8]))
# union(find_set(Z[3]), find_set(Z[5]))
# union(find_set(Z[0]), find_set(Z[7]))

union(find_set(Z[5]), find_set(Z[6]))
union(find_set(Z[8]), find_set(Z[9]))
union(find_set(Z[1]), find_set(Z[9]))
union(find_set(Z[7]), find_set(Z[8]))
union(find_set(Z[2]), find_set(Z[3]))
union(find_set(Z[2]), find_set(Z[6]))
union(find_set(Z[2]), find_set(Z[7]))

for each in Z:
    print(f'parent of {each.key} is {each.parent.key}')

