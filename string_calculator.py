import re
class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        
        negatives = [int(n) for n in re.findall(r'-\d+', numbers)]
        if negatives:
            raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")
        
        if numbers.startswith("//"):
            delimiter, numbers = numbers[2:].split("\n", 1)
            numbers = numbers.replace(delimiter, ",")
        numbers = numbers.replace("\n", ",")

        return int(sum(map(int, numbers.split(',')))) 