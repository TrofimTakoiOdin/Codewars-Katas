# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/python
def reverse(text):
    return "".join(list(reversed(text)))

def reverse_words(text):
    text = " ".join(list(map(reverse, text.split(" "))))
    return text


