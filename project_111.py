import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import csv

df = pd.read_csv("project_111.csv")
data = df["claps"].tolist()

def randomSetOfMean(counter):
    dataset = []

    for i in range(0, counter):
        randomIndex = random.randint(0, len(data) - 1)
        value = data[randomIndex]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean

mean_list = []

for i in range(0, 100):
    setOfMean = randomSetOfMean(30)
    mean_list.append(setOfMean)

mean = statistics.mean(mean_list)
stdev_mean_list = statistics.stdev(mean_list)

print(mean)
print(stdev_mean_list)

first_stdev_start, first_stdev_end = mean - stdev_mean_list, mean + stdev_mean_list
second_stdev_start, second_stdev_end = mean - (stdev_mean_list * 2), mean + (stdev_mean_list * 2)
third_stdev_start, third_stdev_end = mean - (stdev_mean_list * 3), mean + (stdev_mean_list * 3)

'''
#For first sample
df = pd.read_csv("math1.csv")
data = df["Math_score"].tolist()

meanOfSampleOne = statistics.mean(data)
print(meanOfSampleOne)

fig = ff.create_distplot([mean_list], ["student marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [meanOfSampleOne, meanOfSampleOne], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.show()
'''
'''
#For second sample
df = pd.read_csv("math2.csv")
data = df["Math_score"].tolist()

meanOfSampleTwo = statistics.mean(data)
print(meanOfSampleTwo)

fig = ff.create_distplot([mean_list], ["student marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [meanOfSampleTwo, meanOfSampleTwo], y = [0, 0.17], mode = "lines", name = "MEAN of sample 2"))
fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = "lines", name = "STDEV of sample 1 end"))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = "lines", name = "STDEV of sample 2 end"))
fig.show()
'''

#For third sample
df = pd.read_csv("project_111.csv")
data = df["claps"].tolist()

meanOfSampleThree = statistics.mean(data)
print(meanOfSampleThree)

fig = ff.create_distplot([mean_list], ["number of claps"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [meanOfSampleThree, meanOfSampleThree], y = [0, 0.17], mode = "lines", name = "MEAN of sample 2"))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = "lines", name = "STDEV of sample 2 end"))
fig.add_trace(go.Scatter(x = [third_stdev_end, third_stdev_end], y = [0, 0.17], mode = "lines", name = "STDEV of sample 3 end"))
fig.show()

z_score = (mean - meanOfSampleThree) / stdev_mean_list
print(z_score)