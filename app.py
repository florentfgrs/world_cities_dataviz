import streamlit as st
from data import prepare_data, download_data


st.title("World Cities")

download_data()


@st.cache_data
def load_data():
    return prepare_data()


data = load_data()

## Combobox
countries = [p for p in data["cou_name_en"].unique().to_list() if p is not None]
selected_country = st.selectbox("Select a country:", sorted(countries))

if selected_country:

    ## Table
    filtered_cities = (
        data.filter(data["cou_name_en"] == selected_country)
        .sort("population", descending=True)
        .head(100)
    )

    col1, col2 = st.columns(2)

    # Table
    with col1:
        st.subheader(f"The 100 largest cities in {selected_country}")
        st.dataframe(filtered_cities.select("name", "population").to_pandas())

    ## Map
    with col2:
        st.map(
            filtered_cities.to_pandas(), latitude="lat", longitude="long", size="size"
        )

    st.bar_chart(
        data=filtered_cities.sort("population").to_pandas(),
        x="name",
        y="population",
        x_label="Cities",
        y_label="Population (millions)",
    )
