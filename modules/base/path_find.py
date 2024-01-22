class AlgorithmPathFound:
    def __init__(self, map, sx, sy, fx, fy):
        self.width = len(map[0])
        self.height = len(map)

        self.map = [[0 for _ in range(self.width + 2)] for _ in range(self.height + 2)]

        for i in range(self.height + 2):
            for j in range(self.width + 2):
                if j == 0 or i == 0 or j == self.width + 1 or i == self.height + 1:
                    self.map[i][j] = -1

        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                self.map[i][j] = map[i - 1][j - 1]

        self.sx = sy + 1
        self.sy = sx + 1

        self.fx = fy + 1
        self.fy = fx + 1

        self.uk = 1
        self.un = 0

        self.queue = [[self.sx, self.sy]]
        self.map[self.sx][self.sy] = 1

        self.out = []

    def sos(self, i, j, x, y):
        if self.map[x][y] == 0:
            self.queue.append([x, y])

            self.uk += 1

            self.map[x][y] = self.map[i][j] + 1

    def start(self):
        while self.map[self.fx][self.fy] == 0 and self.uk > self.un:
            i = self.queue[self.un][0]
            j = self.queue[self.un][1]

            self.un += 1

            self.sos(i, j, i + 1, j)
            self.sos(i, j, i - 1, j)
            self.sos(i, j, i, j + 1)
            self.sos(i, j, i, j - 1)

            # print("t")

            # for element in self.map:
            #     print(element)

            # print()

        if self.map[self.fx][self.fy] == 0:
            return []

        else:
            l = int(self.map[self.fx][self.fy])

            # for element in self.map:
            #     print(element)

            # print()

            while l >= 1:
                self.map[self.fx][self.fy] = "+"

                self.out.append([self.fx - 1, self.fy - 1])

                if self.map[self.fx - 1][self.fy] == l - 1:
                    self.fx -= 1

                elif self.map[self.fx + 1][self.fy] == l - 1:
                    self.fx += 1

                elif self.map[self.fx][self.fy - 1] == l - 1:
                    self.fy -= 1

                else:
                    self.fy += 1

                l -= 1

            # for element in self.map:
            #     print(element)

            return self.out[::-1]


if __name__ == "__main__":
    alg = AlgorithmPathFound([[0, 0, -1], [0, -1, -1], [0, 0, 0]], 1, 0, 2, 2)
    print(alg.start())
