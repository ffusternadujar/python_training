def sentence_formatter(sentence):
    if sentence.startswith(("cómo", "qué", "cuándo", "dónde", "por qué", "quién")):
        sentence += "?"
    else:
        sentence += "."
    return sentence.capitalize()

input_storage = []
while True:
    input_value = input("Say something: ")
    if input_value == "\end":
        break
    input_storage.append(sentence_formatter(input_value))

print(" ".join(input_storage))



