import plotly.express as px
import csv
import pandas as pd
import numpy as np

def plot(data):
    with open(data) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x="Marks In Percentage",y="Days Present")
        fig.show()

def getdatasource(data):
    coffee = []
    sleep = []
    with open(data) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            coffee.append(float(row["Marks In Percentage"]))
            sleep.append(float(row["Days Present"]))
    return {"x": coffee, "y": sleep}

def findcorr(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])

data = "d.csv"
datasource = getdatasource(data)
findcorr(datasource)
plot(data)