# %%
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np


# %%
df = pd.read_csv('train.csv')
df

# %%
df.head()

# %%
df.info()

# %%
## Checking for duplicates
duplicated_show = df.duplicated().sum()
print(duplicated_show)

# %%
## Checking for null values 
duplicated_show = df.isnull().sum()
print(duplicated_show)

# %%
## Lets handle the missing values in Postal Code missing values 
missing_values = df['Postal Code'].fillna('0', inplace=True) ## replacing the missing values with -1
print(missing_values)

# %%
df.info()

# %%
## Lets make sure the date in ORDER DATE AND SHIP DATE is in the correct format
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y', errors='coerce')

# %%
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y', errors='coerce')

# %%
df.info()

# %%

df['Order Month'] = df['Order Date'].dt.to_period('M')


# %%
## Total Sales by Region
import plotly.express as px
region_sales = df.groupby('Region')['Sales'].sum().reset_index()
fig1 = px.bar(region_sales, 
              x='Region', 
              y='Sales', 
              title='Total Sales by Region', 
              color='Sales', 
              color_continuous_scale='Viridis')
fig1.update_layout(xaxis_title='Region', yaxis_title='Total Sales')
fig1.show()

# %%
## Sales by Shipping Mode
fig2 = px.box(df, 
              x='Ship Mode', 
              y='Sales', 
              title='Sales Distribution by Shipping Mode', 
              color='Ship Mode', 
              log_y=True)
fig2.update_layout(xaxis_title='Shipping Mode', yaxis_title='Sales (log scale)')
fig2.show()

# %%
## Sales by Category and Sub-Category
category_sales = df.groupby(['Category', 'Sub-Category'])['Sales'].sum().reset_index()
fig3 = px.bar(category_sales, 
              x='Sub-Category', 
              y='Sales', 
              color='Category', 
              title='Sales by Category and Sub-Category', 
              barmode='group', 
              color_discrete_sequence=px.colors.qualitative.Pastel)
fig3.update_layout(xaxis_title='Sub-Category', yaxis_title='Total Sales')
fig3.show()

# %%
# Convert 'Order Month' to datetime by selecting the start of each month
df['Order Month'] = df['Order Month'].dt.to_timestamp()




# %%
## Monthly Sales Trends
monthly_sales = df.groupby('Order Month')['Sales'].sum()
monthly_sales_df = monthly_sales.reset_index()
fig = px.line(monthly_sales_df, x='Order Month', y='Sales', 
              title='Monthly Sales Trends', 
              markers=True, line_shape='linear', 
              template='plotly', 
              color_discrete_sequence=['coral'])
fig.update_layout(
    xaxis_title='Order Month',
    yaxis_title='Total Sales',
    xaxis_tickangle=-45,
    title_font=dict(size=14, family='Arial', weight='bold'),
    plot_bgcolor='white'
)
fig.show()



# %%
# Group by 'State' and calculate the total sales.
state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10).reset_index()
# Top 10 States by Sales
fig1 = px.bar(state_sales, 
              x='Sales', 
              y='State', 
              title='Top 10 States by Sales', 
              orientation='h',  
              color='Sales', 
              color_continuous_scale='viridis',  # 
              labels={'Sales': 'Total Sales', 'State': 'State'}, 
              text='Sales'  
)
fig1.update_layout(
    title=dict(
        text='Top 10 States by Sales', 
        font=dict(size=14, family='Montserrat', weight='bold')
    ),
    xaxis_title='Total Sales',
    yaxis_title='State',
    plot_bgcolor='white',
    xaxis=dict(showgrid=True, gridcolor='lightgray'),
    showlegend=False
)

# Show the plot
fig1.show()


# %%
import plotly.express as px

segment_sales = df.groupby('Segment')['Sales'].sum().reset_index()

fig2 = px.bar(segment_sales, 
              x='Segment', 
              y='Sales', 
              title='Sales by Customer Segment', 
              color='Sales',  
              color_continuous_scale='Magma', 
              labels={'Sales': 'Total Sales', 'Segment': 'Customer Segment'},  
              text='Sales' 
)
fig2.update_layout(
    title=dict(
        text='Sales by Customer Segment', 
        font=dict(size=16, family='Arial', weight='bold'),
        x=0.5
    ),
    xaxis_title='Customer Segment',
    yaxis_title='Total Sales',
    plot_bgcolor='white',
    xaxis=dict(
        tickangle=45,
        showgrid=True, 
        gridcolor='lightgray',
        ticks='outside',
        ticklen=6
    ),
    yaxis=dict(
        showgrid=True, 
        gridcolor='lightgray',
    ),
    showlegend=False,
    margin=dict(l=50, r=50, t=50, b=50)
)
fig2.show()




