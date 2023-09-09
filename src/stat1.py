import pandas as pd
import matplotlib.pyplot as plt


def getDescStats():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    )
    answer = df["sepal_length"].describe()
    return answer


def makeGraph():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    )

    df.groupby("species").mean()["sepal_length"].plot.bar(
        title="Average Sepal Length per Iris Species",
        xlabel="Iris Species",
        ylabel="Average Sepal Length (cm)",
    )

    plt.savefig("answer.png")
