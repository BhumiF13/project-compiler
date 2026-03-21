def normalize(text):
    text = text.lower()
    words_to_remove = ["the", "with", "value"]

    words = text.split()
    words = [word for word in words if word not in words_to_remove]

    return " ".join(words)