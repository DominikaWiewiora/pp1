class Statistics:
    def __init__(self):
        self.numbers = []

    def add(self, num):
        self.numbers.append(num)

    def display(self):
        for n in self.numbers:
            print(f'{n} ',end="")

    def greatest(self):
        greatest = max(self.numbers)
        return greatest

    def smallest(self):
        smallest = min(self.numbers)
        return smallest

    def mean(self):
        mean = sum(self.numbers) / len(self.numbers)
        return mean

    def median(self):
        sort = sorted(self.numbers)
        l = len(sort)
        if l % 2 == 0:
            median = (sort[l // 2 - 1] + sort[l // 2]) / 2
        else:
            median = sort[l // 2]
        return median

    def display_statistics(self):
        print("Minimum:", self.smallest())
        print("Maximum:", self.greatest())
        print("Mean:", self.mean())
        print("Median:", self.median())

stats = Statistics()
numbers = [12, 37, 6, 9, 17]

for num in numbers:
    stats.add(num)

stats.display()
stats.display_statistics()


stats.display()
stats.display_statistics()


    


        