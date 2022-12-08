from Algorithms import nsgaii
from Problems import problem


if __name__ == '__main__':
    algorithm = nsgaii.Nsgaii(save_times=10)
    problem = problem.Problem()
    algorithm.solve(problem)
    print('a')