import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import pandas as pd # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html

# https://matplotlib.org/3.2.2/gallery/misc/plotfile_demo_sgskip.html

data = pd.read_csv("sentiment.csv", on_bad_lines='skip')

# Plot
plt.figure(figsize=(6.8, 4.2))
x = range(len(data['Time']))
plt.plot(x, data['VPolarity'])
plt.xticks(rotation=45)
plt.xticks(x, data['Time'])
plt.xlabel('Date')
plt.ylabel('Vpolarity')
plt.show()