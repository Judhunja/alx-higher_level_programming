#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    b = sentence[0] if len(sentence) > 0 else None

    return (a, b)


if __name__ == "__main__":
    multiple_returns(sentence)
