from src.stat1 import getDescStats, makeGraph
import os


def test_get_stat():
    testDf = getDescStats()
    assert testDf[3] == 4.3
    assert testDf[4] == 5.1
    assert testDf[5] == 5.8


def test_graph():
    makeGraph()
    assert os.path.isfile("answer.png")
