import pandas as pd


def minCol():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    )
    answer = df["sepal_length"].min()
    return answer
