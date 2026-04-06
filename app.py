import logging

logging.basicConfig(level=logging.INFO)

def add(a, b):
    logging.info("Addition operation performed by Divyani")
    return a + b

if __name__ == "__main__":
    print(add(2, 3))