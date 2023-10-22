max_length = int(input())
num_headlines = int(input())
for _ in range(num_headlines):
    headline = input()
    if len(headline) <= max_length:
        print(headline)
    else:
        shortened_headline = headline[:max_length - 3] + "..."
        print(shortened_headline)
