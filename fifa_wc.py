import streamlit as st
import pandas as pd
from PIL import Image

# Custom CSS to change background color
custom_css = """
<style>
    .main {
        background-color: #FFFFFF;  /* Change this color to your desired background color */
    }
    .title {
        color: blue;  /* Change the color of the title */
        font-size: 36px;  /* Change the font size of the title */
    }
</style>
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

t1, t2 = st.columns((0.4, 0.4))

t1.image('fifawc.jpg', width=50)
t2.markdown("<h1 style='font-size: 20px; color: orange'>Fifa World Cup</h1>", unsafe_allow_html=True)

def load_data():
    data = pd.read_excel('C:\\Users\\LENOVO\\Documents\\Python_project\\fifa_world_cup.xlsx')
    return data

data = load_data()

with st.form("form_key"):
    st.write("Select Year")
    year_list = data['Year'].tolist()
    selected_year = st.selectbox('Select Year:', year_list)
    host = data.loc[data['Year'] == selected_year, 'Host'].values[0]
    winner = data.loc[data['Year'] == selected_year, 'Winner'].values[0]
    coach = data.loc[data['Year'] == selected_year, 'Winning_Coach'].values[0]

    submit_btn = st.form_submit_button("Submit")

if submit_btn:
    # Fetch the details based on the selected year
    details = data.loc[data['Year'] == selected_year].iloc[0]
    host = details['Host']
    winner = details['Winner']
    Coach = details['Winning_Coach']

    summary = pd.DataFrame({
        'Year': [selected_year],
        'Host': [host],
        'Winner': [winner],
        'Coach' : [Coach]
    })
    st.write("Summary:")
    st.table(summary)

    # Display the host country flag
    winner_flag_path = f'C:\\Users\\LENOVO\Documents\\Python_project\\flags/{winner}.png'

    try:
        winner_flag = Image.open(winner_flag_path)
        st.image(winner_flag, caption=f'{winner}', width=150)       
        
    except FileNotFoundError as e:
        st.warning(f"Flag image for {e.filename} not found.")
