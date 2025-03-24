class Node:
    def __init__(self, total, prefix, suffix, best):
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.best = best

    @staticmethod
    def from_value(val):
        return Node(val, val, val, val)

    @staticmethod
    def merge(left, right):
        total = left.total + right.total
        prefix = max(left.prefix, left.total + right.prefix)
        suffix = max(right.suffix, right.total + left.suffix)
        best = max(left.best, right.best, left.suffix + right.prefix)
        return Node(total, prefix, suffix, best)


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [Node(0, 0, 0, float('-inf'))] * (4 * self.n)
        self._build(data, 1, 0, self.n - 1)

    def _build(self, data, v, tl, tr):
        if tl == tr:
            self.tree[v] = Node.from_value(data[tl])
        else:
            tm = (tl + tr) // 2
            self._build(data, v * 2, tl, tm)
            self._build(data, v * 2 + 1, tm + 1, tr)
            self.tree[v] = Node.merge(self.tree[v * 2], self.tree[v * 2 + 1])

    def update(self, pos, val, v=1, tl=0, tr=None):
        if tr is None:
            tr = self.n - 1
        if tl == tr:
            self.tree[v] = Node.from_value(val)
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(pos, val, v * 2, tl, tm)
            else:
                self.update(pos, val, v * 2 + 1, tm + 1, tr)
            self.tree[v] = Node.merge(self.tree[v * 2], self.tree[v * 2 + 1])

    def query(self, l, r, v=1, tl=0, tr=None):
        if tr is None:
            tr = self.n - 1
        if l > r:
            return Node(0, float('-inf'), float('-inf'), float('-inf'))
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        left_part = self.query(l, min(r, tm), v * 2, tl, tm)
        right_part = self.query(max(l, tm + 1), r, v * 2 + 1, tm + 1, tr)
        return Node.merge(left_part, right_part)


if __name__ == "__main__":
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    seg_tree = SegmentTree(A)

    for _ in range(Q):
        parts = input().split()
        if parts[0] == "U":
            i = int(parts[1]) - 1  # convert to 0-indexed
            x = int(parts[2])
            seg_tree.update(i, x)
        elif parts[0] == "Q":
            l = int(parts[1]) - 1
            r = int(parts[2]) - 1
            res = seg_tree.query(l, r)
            print(res.best)
