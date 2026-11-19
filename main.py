def divide(a, b):
    return a / b

if __name__ == "__main__":
    print(f"5/2 = {divide(5, 2)}")
    print(f"11/2 = {divide(11, 2)}")
    print(f"10/0 = {divide(10, 0)}")
    try:
        print(f"10/0 = {divide(10, 0)}")
    except ZeroDivisionError:
        print("Buta, nem lehet 0-val osztani!")