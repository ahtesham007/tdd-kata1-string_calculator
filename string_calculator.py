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

            if '[' in delimiter and ']' in delimiter:
                t_delimeter = ""
                delimiters = []
                for char in delimiter:
                    if char not in ['[', ']']:
                        t_delimeter += char
                    elif char == "]":
                        delimiters.append(t_delimeter)
                        t_delimeter = ""
                        
                for _ in delimiters:
                    numbers = numbers.replace(_, ",")

            numbers = numbers.replace(delimiter, ",")
        numbers = numbers.replace("\n", ",")

        return int(sum(num for num in map(int, numbers.split(',')) if num < 1000))