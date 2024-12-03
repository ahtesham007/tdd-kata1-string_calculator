import re
class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        
        negatives = [int(n) for n in re.findall(r'-\d+', numbers)]
        if negatives:
            raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")
        
        if numbers.startswith("//"):

            delimiter_part, numbers = numbers[2:].split("\n", 1)
            delimiter = re.findall(r'\[([^\]]+)\]', delimiter_part)[0]
            numbers = numbers.replace(delimiter, ",")
        numbers = numbers.replace("\n", ",")

        return int(sum(num for num in map(int, numbers.split(',')) if num < 1000)) 