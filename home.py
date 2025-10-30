import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Streamlit Multi-App", layout="wide")

# --- Initialize session state for navigation ---
if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"

# --- Top Navbar (using buttons) ---
st.write("### 🧭 Navigation")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏠 Home"):
        st.session_state.page = "🏠 Home"
with col2:
    if st.button("🖼️ Wallpaper Gallery"):
        st.session_state.page = "🖼️ Wallpaper Gallery"
with col3:
    if st.button("👥 Age Group Selection"):
        st.session_state.page = "👥 Age Group Selection"

st.divider()

# --- Navigation Handling ---
page = st.session_state.page

# ============= HOME PAGE =============
if page == "🏠 Home":
    st.title("🏠 Welcome to the Multi-App Dashboard")
    st.markdown("""
    Choose one of the available Streamlit apps below:
    """)

    st.markdown("### 🔗 Available Apps:")
    st.markdown("- 🖼️ [**Wallpaper Gallery**](https://age-categories1-a4mskxovtq8egu5htvndgu.streamlit.app/)")
    st.markdown("- 👥 [**Age Group Selection**](https://mdmu4pin3tbxhx5revmten.streamlit.app/)")
    st.info("Click any link above to open the app in a new tab.")

# ============= WALLPAPER GALLERY =============
elif page == "🖼️ Wallpaper Gallery":
    st.title("🖼️ Wallpaper Gallery")

    # Initialize state for info sections
    if "open_section" not in st.session_state:
        st.session_state.open_section = None

    def toggle_section(name):
        if st.session_state.open_section == name:
            st.session_state.open_section = None
        else:
            st.session_state.open_section = name

    # Buttons for 3 sections
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Info1"):
            toggle_section("Info1")
    with col2:
        if st.button("Info2"):
            toggle_section("Info2")
    with col3:
        if st.button("Info3"):
            toggle_section("Info3")

    st.markdown("---")

    if st.session_state.open_section == "Info1":
        c1, c2 = st.columns(2)
        with c1:
            st.image("https://wallpaperaccess.com/full/1239388.jpg", use_container_width=True)
            st.caption("Sunrise")
        with c2:
            st.image("https://wallpapers.com/images/hd/2560x1440-fall-sunrise-on-landscape-0471974z9mnguo68.jpg", use_container_width=True)
            st.caption("Sunrise Landscape")

    elif st.session_state.open_section == "Info2":
        c1, c2 = st.columns(2)
        with c1:
            st.image("https://images.wallpaperscraft.com/image/single/tulips_flowers_field_1369025_2560x1440.jpg", use_container_width=True)
            st.caption("Tulip Field")
        with c2:
            st.image("https://wallpapershome.com/images/pages/pic_h/10299.jpg", use_container_width=True)
            st.caption("Colorful Flower Field")

    elif st.session_state.open_section == "Info3":
        c1, c2 = st.columns(2)
        with c1:
            st.image("https://images.wallpaperscraft.com/image/single/starry_sky_mountains_stars_119711_2560x1440.jpg", use_container_width=True)
            st.caption("Starry Sky Over Mountains")
        with c2:
            st.image("https://cdn.bhdw.net/im/the-nighttime-beauty-of-clouds-and-moonlight-reflected-in-the-clear-93223_w635.webp", use_container_width=True)
            st.caption("Moonlight Reflections")

# ============= AGE GROUP SELECTION =============
elif page == "👥 Age Group Selection":
    st.title("👥 User Age Group Selection")

    users = [
        {"name": "Aarav", "age": 18, "gender": "Male", "age_group": "1-25"},
        {"name": "Priya", "age": 22, "gender": "Female", "age_group": "1-25"},
        {"name": "Rahul", "age": 24, "gender": "Male", "age_group": "1-25"},
        {"name": "Sneha", "age": 19, "gender": "Female", "age_group": "1-25"},
        {"name": "Kiran", "age": 25, "gender": "Male", "age_group": "1-25"},
        {"name": "Vikram", "age": 30, "gender": "Male", "age_group": "26-50"},
        {"name": "Meera", "age": 35, "gender": "Female", "age_group": "26-50"},
        {"name": "Raj", "age": 40, "gender": "Male", "age_group": "26-50"},
        {"name": "Pooja", "age": 45, "gender": "Female", "age_group": "26-50"},
        {"name": "Amit", "age": 50, "gender": "Male", "age_group": "26-50"},
        {"name": "Karthik", "age": 55, "gender": "Male", "age_group": "51-75"},
        {"name": "Anjali", "age": 60, "gender": "Female", "age_group": "51-75"},
        {"name": "Rajesh", "age": 65, "gender": "Male", "age_group": "51-75"},
        {"name": "Lakshmi", "age": 70, "gender": "Female", "age_group": "51-75"},
        {"name": "Sundar", "age": 75, "gender": "Male", "age_group": "51-75"},
        {"name": "Suresh", "age": 80, "gender": "Male", "age_group": "76-100"},
        {"name": "Kamala", "age": 85, "gender": "Female", "age_group": "76-100"},
        {"name": "Mohan", "age": 90, "gender": "Male", "age_group": "76-100"},
        {"name": "Leela", "age": 95, "gender": "Female", "age_group": "76-100"},
        {"name": "Raman", "age": 100, "gender": "Male", "age_group": "76-100"},
    ]

    st.subheader("🎚️ Select Age Group")
    age_options = ["1–25 🧒", "26–50 🧑‍💼", "51–75 👨‍🦳", "76–100 👵"]
    selected = st.radio("Choose an age group:", age_options, horizontal=True)

    group_meanings = {
        "1–25 🧒": "Students, early professionals",
        "26–50 🧑‍💼": "Working professionals, parents",
        "51–75 👨‍🦳": "Experienced elders, retirees",
        "76–100 👵": "Senior citizens"
    }

    selected_group = selected.split(" ")[0].replace("–", "-")
    filtered = [u for u in users if u["age_group"] == selected_group]

    st.subheader(f"📊 Users in Age Group: {selected}")
    st.table([[u["name"], u["age"], u["gender"], u["age_group"]] for u in filtered])
