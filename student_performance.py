import pandas as pd
import matplotlib.pyplot as plt

# Load student data
data = pd.read_csv("student_data.csv")

# Display the data
print("Student Data:")
print(data)

# Calculate average marks
average_marks = data["Marks"].mean()

print("\nAverage Marks:", average_marks)

# Find highest marks
highest_marks = data["Marks"].max()

print("Highest Marks:", highest_marks)

# Find lowest marks
lowest_marks = data["Marks"].min()

print("Lowest Marks:", lowest_marks)

# Display students who scored above average
above_average = data[data["Marks"] > average_marks]

print("\nStudents Above Average:")
print(above_average)

# Create a bar chart
plt.bar(data["Name"], data["Marks"])
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Performance Analysis")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
