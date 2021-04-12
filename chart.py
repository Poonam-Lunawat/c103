import pandas as pd
import plotly_express as px

df= pd.read_csv("line_chart.csv")

#df= pd.read_csv("csv files/data.csv")


fig = px.line(df, x="Year", y="Per capita income", color = "Country", title="Per Capita income")
#fig= px.bar(df,x="Country", y="InternetUsers")
fig.show()