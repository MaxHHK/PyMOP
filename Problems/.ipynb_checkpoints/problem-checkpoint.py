import copy

class Problem:
    def __init__(self, **kwargs):
        self.init_kwargs = copy.deepcopy(kwargs)
        
        self.population_size = 100
        self.max_function_evaluation = 100000
        self.consumed_function_evaluation = 0
        
        self.num_of_objectives = 0
        self.num_of_decision_variables = 0
        self.max_runtime = 10000000
        self.encoding_scheme = 1
        self.lower_bound = 0
        self.upper_bound = 1
        self.optimum = None
        self.pareto_front = None
