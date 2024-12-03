class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        return int(sum(map(int, numbers.split(',')))) 