try:
    a, b = input("Select numbers: ").split()
    a, b = int(a), int(b)
except (ValueError, AttributeError, TypeError) as e:
    print("Error, try again", e)
else:
    for i in range(a, b + 1):
        print(i, end=" ")