from stats import calculate_stats
from report import print_stats, export_stats

def get_numbers():
    numbers = []
    for i in range(5):
        numbers.append(int(input("Enter a number: ")))
    return numbers

if __name__ == "__main__":
    nums = get_numbers()
    stats = calculate_stats(nums)
    print_stats(stats)
    export_stats(stats)