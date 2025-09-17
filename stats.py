import math

def calculate_stats(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    high = max(numbers)
    low = min(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    std_dev = math.sqrt(variance)

    return {
        "Total": total,
        "Average": avg,
        "Highest": high,
        "Lowest": low,
        "Variance": variance,
        "Standard Deviation": std_dev
    }