from datetime import datetime as dt

def logger(text, data):
    time = dt.now().strftime("%H:%M:%S")
    log_string = f"{time}; {text}; {data}\n"
    with open ("log.csv", "a") as file:
        file.write(log_string)