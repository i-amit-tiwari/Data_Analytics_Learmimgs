data_points = [10, 25, 5, 42, 18]
print(data_points[0])    # Output: 10
print(data_points[-1])   # Output: 18 (last element)
print(data_points[1:4])  # Output: [25, 5, 42] (index 1 up to, but not including, 4)

data_points[2] = 8       # Modify element at index 2
print(data_points)       # Output: [10, 25, 8, 42, 18]

data_points.append(50)   # Add to the end
print(data_points)       # Output: [10, 25, 8, 42, 18, 50]

data_points.sort()       # Sort in place
print(data_points)       # Output: [8, 10, 18, 25, 42, 50]

print(len(data_points))  # Output: 6 (number of elements)