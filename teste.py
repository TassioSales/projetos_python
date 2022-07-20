def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    # your code here
    return max(data, key=data.count)


print(most_frequent(["a", "b", "c", "a", "b", "a", "b", "d"]))
