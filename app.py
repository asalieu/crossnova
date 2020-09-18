import dash
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
import numpy as np
import psycopg2
import copy


## define custom CSS
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

colors = {
    'background': '#e1eff5',
    'text': '#7FDBFF'
}

## setting up the trigger the dash app service 
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)  


## Initiate connection to postgrsql database hosted on the cloud 

## IMPORTANT NOTE: I could had created a seperate file for this such as .env wherein i can pass the login credentials 
## and access it using the process.env method but just to keep it clean,easy to access by reader/examiner
## i opted to keep all in .py file
 
try:
   connection = psycopg2.connect(user="vojcmcxwzvdrkn",
                                  password="5f605df0eefa7870a7044273ce4ebcd6305a29bbdf648611c8e02e805610cfcb",
                                  host="ec2-54-217-234-157.eu-west-1.compute.amazonaws.com",
                                  port="5432",
                                  database="d4qc47j8lm0le4")
   cursor = connection.cursor()
   postgreSQL_select_Query = "select car_purchase_price,car_sale_price,car_brand from auto"

   cursor.execute(postgreSQL_select_Query)
   print("Selecting rows from mobile table using cursor.fetchall")
   auto_records = cursor.fetchall()    
    
    
## Catch and handel connection related issues to postgrsql database here 
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")         




## preprocessing the data and setting to numpy array

df = pd.DataFrame((np.array(auto_records)))
la=df.columns = ['pur_price','sale_price','car_brand'] 



 
fig = px.scatter(df,x=df['pur_price'],y=df['sale_price'],color=df['car_brand'])

## Setting the app layout 
app.layout = html.Div(
    children=[
        
    html.H3("CrossNova Docker Dash Application with PostgrSQL", style={'text-align':'center','color':'darkblue'}),
    ## select using multi select dropdown    
    dcc.Dropdown(
        id='demo-dropdown',
        options=[           
            {'label': 'pur_price', 'value':'Pur_price'},
            {'label': 'sale_price', 'value':'Sale_price'},                       
        ], 
        placeholder="select axis", 
        multi=True,
        value=['pur_price','sale_price'],     
        style={'width':'230px'},
    ),
    html.Br(),   

    html.Div(id="dd-output-container",style={'backgroundColor':colors['background']}),
    html.Br(),
    
    dcc.Graph(id="tbl_auto", figure=fig,style={'margin':'auto','width':'50%'})
])


## Connect plotly graph
 
@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('demo-dropdown', 'value')])
def update_output(selected_value): 
        container= "You have selected: {}".format(selected_value) 
# Plotly Express 
        return (selected_value,fig)      

if __name__ == '__main__':
    app.run_server('localhost',9000)