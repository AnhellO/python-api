import abc, random, copy

class CoalesceStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def coalesce(self, responses: tuple):
        pass

class AverageCoalesceConcreteStrategy(CoalesceStrategy):
    def coalesce(self, responses: tuple):
        length = len(responses)
        average = responses[0]
        for i in responses[1:]:
            for key in average.keys():
                average[key] += i[key]

        for k, v in average.items():
            average[k] = v // length

        return average

class MaxCoalesceConcreteStrategy(CoalesceStrategy):
    def coalesce(self, responses: tuple):
        _max = responses[0]
        for i in responses[1:]:
            for key in _max.keys():
                _max[key] = max(_max[key], i[key])

        return _max

class MinCoalesceConcreteStrategy(CoalesceStrategy):
    def coalesce(self, responses: tuple):
        _min = responses[0]
        for i in responses[1:]:
            for key in _min.keys():
                _min[key] = min(_min[key], i[key])
        
        return _min

class RandomCoalesceConcreteStrategy(CoalesceStrategy):
    def coalesce(self, responses: tuple):
        return responses[random.randint(0, 2)]

class CoalesceContext(object):
    def __init__(self, responses: tuple, strategy: CoalesceStrategy = None):
        self._responses = responses
        self._strategy = strategy

    def execute_strategy(self):
        if self._strategy != None:
            return self._strategy.coalesce(copy.deepcopy(self._responses))

        return AverageCoalesceConcreteStrategy().coalesce(copy.deepcopy(self._responses))

    def set_strategy(self, strategy: CoalesceStrategy):
        self._strategy = strategy

def main():
    items = (
        {
            "deductible": 1000,
            "stop_loss": 10000,
            "oop_max": 5000
        },
        {
            "deductible": 1200,
            "stop_loss": 13000,
            "oop_max": 6000
        },
        {
            "deductible": 1000,
            "stop_loss": 10000,
            "oop_max": 6000
        }
    )

    context = CoalesceContext(items)
    print(context.execute_strategy())

    max_coalescer = MaxCoalesceConcreteStrategy()
    context.set_strategy(max_coalescer)
    print(context.execute_strategy())
    
    random_coalescer = RandomCoalesceConcreteStrategy()
    context.set_strategy(random_coalescer)
    print(context.execute_strategy())


if __name__ == '__main__':
    main()