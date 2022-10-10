
import dash
from dash import Dash, dcc, html, Input, Output
from dash import dcc
import pandas as pd
import plotly.express as px
from api_center import Api

# data = pd.read_csv("C:\\Users\\admin\\csv\\apps\\app_1\\avocado.csv")
# data = data.query("type == 'conventional' and region == 'Albany'")
obj=Api()

str_small_bags = obj.sum_of_small_bags() 
str_big_bags = obj.sum_of_big_bags()
str_xl_bags = obj.sum_of_xl_bags()
str_data = obj.get_data()
# print(small_bags['message'],big_bags['message'],xl_bags['message'])

small_bags = str_small_bags['message'][0]
big_bags = str_big_bags['message'][0]
xl_bags = str_xl_bags['message'][0]
datas = str_data['message']
list_of_month=[]
month_total= []

for i in datas:

    x = list(i)
    print(len(x))
    if len(x)>2:
        list_of_month.append(i[1])
        month_total.append(i[2])




list_of_no_bags= [small_bags,big_bags,xl_bags]
list_of_nmaes = ["small","big","xl"]



# data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
# data.sort_values("Date", inplace=True)
# df = pd.DataFrame(data)

# ds = df.sum()
# print(df.sum())
# print(ds['Small Bags'])
app = dash.Dash(__name__)

@app.callback(
    Output("graph", "figure"), 
    Input("names", "value"), 
    Input("values", "value"))

def generate_chart(names, values):
    df = px.data.tips() # replace with your own data source
    fig = px.pie(df, values=values, names=names , hole=.3)
    return fig


app.layout = html.Div(
    children=[
        html.H1(
            children="Avocado Analytics",
        ),
        html.P(
            children="Analyze the behavior of avocado prices"
            " and the number of avocados sold in the US"
            " between 2015 and 2018",
        ),
    #    dcc.Graph(figure=generate_chart()),

        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": ["small","large","xl"],
                        "y": [small_bags,big_bags,xl_bags],
                        "type": "bar",
                    },
                ],
                "layout": {"title": "Average Price of Avocados"},
            },
        ),
        html.Div("Small Bags"),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x":list_of_month,
                        # "x": data["Date"],
                        "y": month_total,
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Avocados Sold"},
            },
        ),
    ]
)



if __name__ == "__main__":
    app.run_server(debug=True)