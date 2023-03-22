def find_average(numbers: list[int]) -> float:

    if not numbers:
        return 0

    return sum(numbers) / len(numbers)
