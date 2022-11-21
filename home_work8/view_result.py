def view(text, result):
    print("{} {}".format(text, result))

def input_data(text):
    return input(text)

def log_view(filename):
    with open(filename, "r") as data:
        print(data.read())