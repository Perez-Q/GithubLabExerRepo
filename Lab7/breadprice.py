import pandas as pd
import matplotlib.pyplot as plt
rd = pd.read_csv('breadprice.csv') # Opens the csv file to be read.
years = rd['Year'].tolist() # Get the years first before it gets deleted.
rd.drop(columns = "Year", inplace = True)
rd.fillna(0, inplace = True) # for any null values will turn to 0 (Filler).
averages = []
for row in rd.index: # index are the rows in the csv file {0 to 10}.
    averages.append(rd.iloc[row].mean()) # it will locate the row and get the mean of the row and

rd.insert(12, "Averages", averages) # inserts from the position 12 of the columns, named "Averages", with the values of {average}.
print(rd.to_string())

x = years
y = averages
plt.plot(x,y)
plt.show()
