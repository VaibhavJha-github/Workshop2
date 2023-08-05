import sys

def generate_histogram(data):
    total_count = sum(count for word, count in data)
    for word, count in data:
        percentage = (count / total_count) * 100
        rounded_percentage = round(percentage)
        bar_length = int(rounded_percentage / 2)
        bar = "" bar_length
        print(f"{word.ljust(10)} [{bar:<50}] {rounded_percentage}%")

if name == "main":
    word_data = []
    for line in sys.stdin:
        word, count = line.strip().split()
        count = int(count)
        word_data.append((word, count))

    generate_histogram(word_data)
