import streamlit as st 
import pandas as pd 
import plotly.express as px 

st.write("""
# Bangladesh COVID-19 Community Mobility Reports 
By [Md. Jubayer Hossain](https://jhossain.netlify.app/)

This dashboard aims to provide insights into what has changed in response to policies aimed at fighting COVID-19. The reports chart movement trends by geography across different categories such as retail and recreation, groceries and pharmacies, parks, transit stations, workplace, and residential.

Data Source: [Google COVID-19 Community Mobility Reports](https://www.google.com/covid19/mobility/)

""")

df = pd.read_csv("global_mobility_clean_data.csv")
df.columns = df.columns.str.title() 
df.sort_values(by='Date')


fig = px.line(df, x="Date", y=['Retail', 'Grocery', 'Parks','Transit', 'Workplaces', 'Residential'], 
                labels= {"value": "Changes", "variable": "Place Categories"},
                 width=900, height=600
                )
fig.update_layout(
    title = "Mobility Trend for for Different Places", 
    xaxis = dict(title = "Date"), 
    font_size=18
)
fig.update_xaxes(title_font_family="Arial")

st.plotly_chart(fig) 


st.write("""
### Place Categories
- **Grocery & pharmacy**: Mobility trends for places like grocery markets, food warehouses, farmers markets, specialty food shops, drug stores, and pharmacies.
- **Parks**: Mobility trends for places like local parks, national parks, public beaches, marinas, dog parks, plazas, and public gardens.
- **Transit stations**: Mobility trends for places like public transport hubs such as subway, bus, and train stations.
- **Retail & recreation**: Mobility trends for places like restaurants, cafes, shopping centers, theme parks, museums, libraries, and movie theaters.
- **Residential**: Mobility trends for places of residence.
- **Workplaces**: Mobility trends for places of work.

### Organization and Source Code 

* Organization: [Center for Health Innovation, Research, Action and Learning - Bangladesh (CHIRAL Bangladesh)](https://chiralbd.netlify.app/)
* Source Code: https://github.com/hossainlab/Community_Mobility
""")


