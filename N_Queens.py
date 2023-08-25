import matplotlib.pyplot as plt
import random

# Run in jupyter 
# Local Search : N-Queens

plt.rcParams['figure.figsize'] = (8, 8)

class NQueensState():
    def __init__(self, queens=None, N=8):
        if queens:
            self.N = len(queens)
            self.queens = queens
        else:
            self.N = N
            self.queens = list(range(1, N+1))
            random.shuffle(self.queens)

        self.num_conflicts = None

    def conflicts(self):
        if self.num_conflicts is None:
            self._compute_conflicts()  
        return self.num_conflicts

    def _compute_conflicts(self):
        self.num_conflicts = sum(self.queens[j] - self.queens[i] == j - i
                                 for i in range(self.N - 1)
                                 for j in range(i+1, self.N))

    def neighbors(self):
        N = self.N
        all_neighbors = []

        for i in range(N-1):
            for j in range(i+1, N):
                neighbors = NQueensState(queens=self.queens)
                neighbors.queens[i], neighbors.queens[j] = neighbors.queens[j], neighbors.queens[i]
                yield neighbors

    def best_neighbors(self):
        return min(self.neighbors(), key=lambda x: x.conflicts())

    def random_neighbors(self):
        i = random.randint(0, self.N - 2)
        j = random.randint(i+1, self.N - 1)
        neighbors = NQueensState(queens=self.queens)
        neighbors.queens[i], neighbors.queens[j] = neighbors.queens[j], neighbors.queens[i]
        return neighbors

    def plot(self, width=512, height=512, show_conflicts=False):
        N = self.N
        w, h = width//N, height//N

        border = plt.Rectangle((0, 0), N*w, N*h, ec='k', fc='w')
        plt.gca().add_patch(border)

        # draw chess
        for i in range(N):
            for j in range(N):
                if (i + j) % 2 == 0: 
                    cell = plt.Rectangle(
                        (i*w, j*h), w, h, fc='gray', alpha=0.6)
                    plt.gca().add_patch(cell)

        # Queen State
        for col, raw in enumerate(self.queens):
            c = 'k' if (col + raw) % 2 == 0 else 'w'  
            x = col*w + w//2
            y = (raw - 1) * h + h//2  
            fs = max(16-N//8, 5)
            plt.text(x, y, 'Q', color=c, fontsize=fs)

        plt.axis('square')
        plt.axis('off')
        plt.title('N Queen')
        plt.show()

state = NQueensState(N=16)
state.plot()
