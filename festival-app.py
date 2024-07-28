# imports ...
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import contextily as ctx
import plotly.express as px

# importing csv 

def load_data(data):
    return pd.read_csv(data)
# app interface
def main():
    st.title("2024 Global Festivals") 
    menu = ['Home', 'About']
    choices = st.sidebar.selectbox("MENU", menu)
    color = st.sidebar.color_picker(label='Color', value='#E255E2')
    festivals = load_data('Outputs/festivals_clean.csv')
    
    if choices == 'Home':
        
        with st.expander("Festival Data"):
            st.dataframe(festivals)
            
        fig = px.scatter_mapbox(festivals, lat ='Latitude', lon = 'Longitude',
                                hover_name='Festival_Name', hover_data='Country',
                                zoom= 1, height= 700, color_discrete_sequence=['magenta'], width= 700,
                                center={'lat':10,'lon': -50}
                                )            
        fig.update_layout(mapbox_style = "open-street-map")
        st.plotly_chart(fig)
        
        st.header("High Grossing Festivals")
        st.bar_chart(
            festivals,
            x = 'Festival_Name',
            y = 'Economic_Impact',
            color=color,
            height= 600,
        )
        
        st.header("Attendance Numbers versus Economic Impact")
        fig2 = px.scatter(
            festivals, x = 'Attendance_Numbers', y = 'Economic_Impact',
            height= 600, hover_name='Festival_Name', size="Economic_Impact"
            )

        st.plotly_chart(fig2)     

    elif choices == 'About':
        st.header("About the dataset: ")
        st.text("Src: https://www.kaggle.com/datasets/gorororororo23/aereregre")
        st.text("""
            This dataset includes information on various music festivals taking place across 
            Europe and other international locations in 2024. It provides details about the 
            festival's name, location, attendance, visitor demographics, economic impact, 
            and the music genres featured. This dataset is useful for analyzing trends in 
            music festivals, understanding visitor preferences, 
            and evaluating the economic significance of these events.

            Column Descriptions:
            Festival_Name: The official name of the music festival.
            Location: The city and country where the festival is held.
            Attendance_Numbers: The estimated number of attendees at the festival.
            Visitor_Demographics: The age range and interests of the attendees.
            Economic_Impact: The estimated economic impact of the festival, 
            often presented in local currency.
            Music_Genre: The primary genre or genres of music featured at the festival.
            """
        )

if __name__ == "__main__":
    main()



# data_path = 'Outputs/festivals_clean.csv'
# df = pd.read_csv(data_path) 

# st.dataframe(df)

# # mapping the festivals


# df.rename(columns={'Latitude':'latitude'}, inplace=True)
# df.rename(columns={'Longitude':'longitude'}, inplace=True)

# st.header("2024 Festivals")
# st.map(df, zoom= 1)
