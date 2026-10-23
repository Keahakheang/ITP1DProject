import streamlit as st
import mylibrary

st.set_page_config(page_title="Attraction Recommendation App", page_icon="🗺️")

if "saved_favorites" not in st.session_state:
    st.session_state.saved_favorites = []

st.title("Smart Attraction Recommender")
st.write("Find places to visit based on your preferences.")

st.sidebar.header("Filter Preferences")

categories = ["nature", "great views", "shows", "theme park"]
selected_categories = st.sidebar.multiselect(
    "Choose categories:",
    categories,
    default=[]
)

free_only = st.sidebar.checkbox("Show free attractions only")

if free_only:
    max_price = 0
else:
    max_price = st.sidebar.slider(
        "Maximum ticket price ($):",
        min_value=0,
        max_value=100,
        value=100,
        step=1
    )

target_age = st.sidebar.selectbox(
    "Who is visiting?",
    ["All Ages", "Kids", "Teens", "Adults", "Seniors"]
)

attractions = mylibrary.get_attractions_data()
recommendations = mylibrary.get_recommendations(
    attractions,
    selected_categories,
    max_price,
    free_only,
    target_age
)

st.header("Recommended Attractions")
st.write("Found", len(recommendations), "attraction(s).")

if len(recommendations) == 0:
    st.write("No attractions match your filters. Try changing them.")

for attraction in recommendations:
    st.image(attraction["image"], width=400)
    st.subheader(attraction["name"])
    st.write(attraction["description"])
    st.write("Categories:")

    for category in attraction["categories"]:
        st.write("-", category)

    if attraction["is_free"]:
        st.write("Price: Free")
    else:
        st.write("Price: $" + str(attraction["price"]))

    attraction_id = attraction["id"]

    if attraction_id in st.session_state.saved_favorites:
        if st.button("Remove from favorites", key="favorite_" + str(attraction_id)):
            st.session_state.saved_favorites.remove(attraction_id)
            st.rerun()
    else:
        if st.button("Save to favorites", key="favorite_" + str(attraction_id)):
            st.session_state.saved_favorites.append(attraction_id)
            st.rerun()

st.header("Saved Favorites")
favorite_count = 0

for attraction in attractions:
    if attraction["id"] in st.session_state.saved_favorites:
        st.write(attraction["name"])
        favorite_count = favorite_count + 1

if favorite_count == 0:
    st.write("You have not saved any attractions yet.")
