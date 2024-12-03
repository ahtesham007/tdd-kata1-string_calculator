class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        numbers = numbers.replace("\n", ",")
        return int(sum(map(int, numbers.split(',')))) 