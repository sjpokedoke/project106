import csv
import plotly.express as px
import numpy as np
import pandas as pd

def getDataSource(datapath):
    coffee = []
    sleep = []

    with open(datapath) as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return {"x": coffee, "y": sleep}

def plotFigure(datapath):
    df = pd.read_csv(datapath)
    fig = px.scatter(df, x="Coffee in ml", y="sleep in hours")
    fig.show()

def findCorr(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between coffee and hours of sleep: ")
    print(correlation[0,1])

def setup():
    datapath = "coffeedata.csv"
    datasource = getDataSource(datapath)
    findCorr(datasource)
    plotFigure(datapath)

setup()