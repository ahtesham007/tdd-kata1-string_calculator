import re

class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        
        if numbers.startswith("//"):
            delimiter_part, numbers = numbers[2:].split("\n", 1)

            delimiters = re.findall(r'\[([^\]]+)\]', delimiter_part)

            if not delimiters:
                delimiters = [delimiter_part]

            for delimiter in delimiters:
                numbers = numbers.replace(delimiter, ",")

        numbers = numbers.replace("\n", ",")

        num_list = [int(num) for num in numbers.split(",")]

        negatives = [num for num in num_list if num < 0]
        if negatives:
            raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")

        return sum(num for num in num_list if num <= 1000)