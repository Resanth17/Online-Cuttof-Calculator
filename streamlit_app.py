import streamlit as st
from streamlit_option_menu import option_menu

selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Engineering Cuttof Calculator", "Medial Cutoff Calculator", "Arts & Science Cutoff Calculator"],
        icons=["House", "Laptop", "Heart pulse", "Brush"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        )
if selected == "Home":
    import requests
    import streamlit as st
    from streamlit_lottie import st_lottie


    st.title(f"Cutoff Calculator")

    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_rocak6fq.json")


    st.subheader("Welcome To Cutoff Calculator 🖐🎓")
    st.title("Online Cutoff Calculator")

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Types of Cutoffs")
            st.write("##")
            st.write(
                """
                Click on the above options to calculate your
                - Engineering Cutoff (or)
                - Medical Cutoff (or)
                - Arts & Science Cutoff (or)

                """
                )
        with right_column:
            st_lottie(lottie_coding, height=300, key="thinking")

if selected == "Engineering Cutoff Calculator":
    import requests
    import streamlit as st
    from streamlit_lottie import st_lottie


    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_3rwasyjy.json")

    st.header("**Engineering Cutoff Calculation 💻🛠**")
    st.subheader("Engineering Cutoff Calculation")
    colChemistry, colPhysics, colMaths = st.columns(3)

    with colChemistry:
        Chemistry_marks = st.number_input("Enter your Chemistry Marks: ")
    with colPhysics:
        physics_marks = st.number_input("Enter your Physics Marks: ")
    with colMaths:
        Maths_marks = st.number_input("Enter your Maths Marks: ")

    Chemistry_Physics_Marks = (Chemistry_marks + physics_marks) / 2
    Maths_Marks = Maths_marks * 1
    Cutoff_Marks = round(Maths_Marks + Chemistry_Physics_Marks)

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("**Engineering Cutoff Marks**")
            st.subheader("Your Engineering Cutoff Marks out of 200 is: " + str(round(Cutoff_Marks,2)))
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")



if selected == "Medial Cutoff Calculator":
    import requests
    import streamlit as st
    from streamlit_lottie import st_lottie


    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_0fhlytwe.json")

    st.header("**Medical Cutoff Calculation 🥼🩺**")
    st.subheader("Medical Cutoff Calculation")
    colChemistry, colPhysics, colBiology = st.columns(3)

    with colChemistry:
        Chemistry_marks = st.number_input("Enter your Chemistry Marks: ")
    with colPhysics:
        physics_marks = st.number_input("Enter your Physics Marks: ")
    with colBiology:
        Biology_marks = st.number_input("Enter your Biology Marks: ")

    Chemistry_Physics_Marks = (Chemistry_marks + physics_marks) / 2
    Biology_Marks = Biology_marks * 1
    Cutoff_Marks = round(Biology_Marks + Chemistry_Physics_Marks)

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("**Medical Cutoff Marks**")
            st.subheader("Your Medical Cutoff Marks out of 200 is: " + str(round(Cutoff_Marks,2)))
        with right_column:
            st_lottie(lottie_coding, height=300, key="medical")


if selected == "Arts & Science Cutoff Calculator":
    import requests
    import streamlit as st
    from streamlit_lottie import st_lottie

    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_ybiszbil.json")

    st.header("**Arts & Science Cutoff Calculation 📔🧰**")
    st.subheader("Arts & Science Cutoff Calculation")
    colMainSubject1, colMainSubject2, colMainSubject3, colMainSubject4 = st.columns(4)

    with colMainSubject1:
        Main_subject1_marks = st.number_input("Enter your Main Subject 1 Marks: ")
    with colMainSubject2:
        Main_subject2_marks = st.number_input("Enter your Main Subject 2 Marks: ")
    with colMainSubject3:
        Main_subject3_marks = st.number_input("Enter your Main Subject 3 Marks: ")
    with colMainSubject4:
        Main_subject4_marks = st.number_input("Enter your Main Subject 4 Marks: ")

    Mainsubject1_Mainsubject2_Marks = (Main_subject1_marks + Main_subject2_marks) / 2
    Mainsubject3_Mainsubject4_Marks = (Main_subject3_marks + Main_subject4_marks) / 2
    Cutoff_Marks = round(Mainsubject3_Mainsubject4_Marks + Mainsubject1_Mainsubject2_Marks)

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("**Arts & Science Cutoff Marks**")
            st.subheader("Your Arts & Science Cutoff Marks out of 200 is: " + str(round(Cutoff_Marks,2)))
        with right_column:
            st_lottie(lottie_coding, height=300, key="science")
