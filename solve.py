class Comb_Iterator:

    def __init__(self, num_counters, max_value=1):
        """
        Object constructor:
        * num_counters: number of counters of the combinations
            computed by the generator function comb_generator().
        * max_value: maximum value of each counter.
        """
        self.num_counters = num_counters
        self.max_value = max_value

        return

    def comb_generator(self):
        """
        Generator function. Return a list containing the next
        value of the counters.
        """

        valores = [i for i in range(self.max_value + 1)]
        result = [valores[0]] * self.num_counters
        loop = {x: i for i, x in enumerate(valores)}
        while True:
            yield result
            for i in range(1, self.num_counters + 1):
                if result[-i] != valores[-1]:
                    result[-i] = valores[loop[result[-i]] + 1]
                    break
                else:
                    result[-i] = valores[0]
            else:
                break