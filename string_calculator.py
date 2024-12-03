class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        if numbers.startswith("//"):
            delimiter, numbers = numbers[2:].split("\n", 1)
            numbers = numbers.replace(delimiter, ",")
        numbers = numbers.replace("\n", ",")

        return int(sum(map(int, numbers.split(',')))) 