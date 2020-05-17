import pandas as pd 
import numpy as np

def average(df):
    df["sumGrades"] = df["Grade"] * df["Users"]
    total_users = np.sum(df["Users"])
    total_grade = np.sum(df["sumGrades"])

    return total_grade/total_users
def gradeStats(filename='grades.csv'):
    df = pd.read_csv(filename)

    print(f"Average is: {average(df)}")


if __name__ == "__main__":
    gradeStats()