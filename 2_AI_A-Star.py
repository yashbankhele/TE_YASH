class Node:
    def __init__(self, data, level, fval):
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        x, y = self.find(self.data, '_')
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []

        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)
        return children

    def shuffle(self, puz, x1, y1, x2, y2):
        if 0 <= x2 < len(self.data) and 0 <= y2 < len(self.data):
            temp_puz = self.copy(puz)
            temp_puz[x1][y1], temp_puz[x2][y2] = temp_puz[x2][y2], temp_puz[x1][y1]
            return temp_puz
        return None

    def copy(self, root):
        return [row[:] for row in root]

    def find(self, puz, x):
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if puz[i][j] == x:
                    return i, j


class Puzzle:
    def __init__(self, size):
        self.n = size
        self.open = []
        self.closed = []

    def accept(self):
        puz = []
        print(f"Enter a {self.n}x{self.n} matrix (use '_' for blank):")
        for i in range(self.n):
            while True:
                temp = input(f"Row {i + 1}: ").strip().split(" ")
                if len(temp) != self.n:
                    print(f"Please enter exactly {self.n} values.")
                    continue
                puz.append(temp)
                break
        return puz

    def f(self, start, goal):
        return self.h(start.data, goal) + start.level

    def h(self, start, goal):
        temp = 0
        for i in range(self.n):
            for j in range(self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp

    def process(self):
        print("Enter the start state matrix:")
        start = self.accept()
        print("Enter the goal state matrix:")
        goal = self.accept()

        start_node = Node(start, 0, 0)
        start_node.fval = self.f(start_node, goal)
        self.open.append(start_node)

        while True:
            if not self.open:
                print("No solution found.")
                return

            cur = self.open.pop(0)

            print("====================================")
            for row in cur.data:
                print(' '.join(row))

            if self.h(cur.data, goal) == 0:
                print("Goal state reached!")
                return

            for child in cur.generate_child():
                child.fval = self.f(child, goal)
                self.open.append(child)

            self.closed.append(cur)
            self.open.sort(key=lambda x: x.fval)


# Run the A* puzzle solver
puz = Puzzle(3)
puz.process()
