import csv

with open('temperature.csv') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    rows = []
    for row in csv_reader:
        rows.append(row)

    country = input("Enter your country: ")
    city = input("Enter your city: ")

    month = input("Enter month: ")
    day = input("Enter day: ")
    year = input("Enter year: ")
    t = []
    for row in rows:
        if row[1] == month and row[2] == day and row[3] == year:
            try:
                t.append((float(row[4]) - 32) / 1.8)
            except ValueError:
                pass

    if t:
        print(f"Average temperature on {month}, {day}, {year} in {city}, {country} is {sum(t) / len(t):.2f}")
        print(f"Maximum temperature is {max(t):.2f} and minimum is {min(t):.2f}")
    else:
        print(f"No data on {month}, {day}, {year} in {city}, {country}")