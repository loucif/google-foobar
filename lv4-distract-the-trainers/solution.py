class Graph:
    def __init__(self, banana_list):
        self.l = len(banana_list)
        self.graph = list([0]*self.l for i in range(self.l))
        for i in range(self.l):
            for j in range(self.l):
                if i < j:
                    self.graph[j][i] = self.graph[i][j] = self.willLoop(
                        banana_list[i], banana_list[j])
        print(self.graph)

    def willLoop(slef, x, y):
        n = x+y
        while n % 2 == 0:
            n /= 2
        if((x % n) == 0):
            return 0
        else:
            return 1

#    def willLoopV2(slef, x, y):
#        l = x+y
#        while n % 2 == 0:
#            l /= 2
#        if((x % l) == 0):
#            return 0
#        else:
#            return 1

    def search(self, i, match, seen):
        for j in range(self.l):
            if self.graph[i][j] and seen[j] == False:
                seen[j] = True
                if match[j] == -1 or self.search(match[j], match, seen):
                    match[j] = i
                    return True
        return False

    def maxPairs(self):
        ctr, match = 0, [-1] * self.l
        for i in range(self.l):
            seen = [False] * self.l
            if self.search(i, match, seen):
                ctr += 1
        return self.l - 2*(ctr/2)


def solution(l):
    return Graph(l).maxPairs()


print(solution([1, 7, 3, 21, 13, 19]))
