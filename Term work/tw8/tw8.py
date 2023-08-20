'''

Problem Statement: Exam Score Analysis and Visualization
An exam has been conducted for a class of students. The exam data is stored in a CSV file,
containing the student names and their scores. Develop a Python program to analyse the exam
scores, calculate key statistics, and visualize the data to gain insights into the students&#39;
performance.

'''

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("exam_scores.csv")
mean_score = data['Score'].mean()
median_score = data['Score'].median()
std_dev = data['Score'].std()

print(f"Mean Score: {mean_score:.2f}")
print(f"Median Score: {median_score:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")

# Histogram
plt.hist(data['Score'], bins=10, edgecolor='black')
plt.title("Exam Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()

# Box plot
plt.boxplot(data['Score'])
plt.title("Exam Score Distribution")
plt.ylabel("Score")
plt.show()


