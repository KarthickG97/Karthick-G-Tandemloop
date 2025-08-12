a = int(input("Enter a number: "))

series = []
current = 1

# Generate the series
for i in range(a):
    series.append(current)
    current += 2


# Print the result
print(", ".join(str(num) for num in series))