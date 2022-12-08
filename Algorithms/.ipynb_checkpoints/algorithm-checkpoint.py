import copy


class Algorithm:
    
    def __init__(self, **kwargs):
        self.init_kwargs = copy.deepcopy(kwargs)
        print(kwargs)
        self.save_times = kwargs.pop("save_times", 0)
        self.problem = None
        self.result = None
        self.metric = None
        
    def solve(self, problem):
        self.result = {}
        self.metric = {'runtime': 0}
        self.problem = problem
        self.problem.consumed_function_evaluation = 0
        self.run(problem)
        
    def run(self, problem):
        print('a')
        