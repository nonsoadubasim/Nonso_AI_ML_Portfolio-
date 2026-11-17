import streamlit as st

st.set_page_config(
    page_title="Adubasim Nonso Miracle | AI/ML Portfolio",
    page_icon="🤖",
    layout="wide",
)

st.markdown(
    """
    <style>
        .stApp {
            background-color: #0B1120;
            color: #F8FAFC;
        }

        section[data-testid="stSidebar"] {
            background-color: #111827;
        }

        h1 {
            color: #D4AF37 !important;
            font-size: 45px !important;
            font-weight: 800 !important;
        }

        h2, h3, h4 {
            color: #D4AF37 !important;
        }

        p, li {
            color: #E2E8F0;
            font-size: 16px;
        }

        .stMarkdown hr {
            border-color: #D4AF37;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #111827;
            border: 1px solid #B89635;
            border-radius: 12px;
            padding: 12px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
st.sidebar.markdown("---")
st.sidebar.subheader("Navigation")

page = st.sidebar.radio(
    "Explore my portfolio",
    ["Home", "About Me", "Skills", "Projects", "Contact"],
)

st.sidebar.title("My Profile")
st.sidebar.write("👨‍💻 Adubasim Nonso Miracle")
st.sidebar.write("Aspiring AI & Machine Learning Engineer")
st.sidebar.markdown("---")
st.sidebar.subheader("My Interests")
st.sidebar.write("🤖 Artificial Intelligence")
st.sidebar.write("🧠 Machine Learning")
st.sidebar.write("📊 Data Analysis")
st.sidebar.write("🐍 Python Programming")
st.sidebar.markdown("---")
st.sidebar.success("Always learning. Always building.")

if page == "Home":

    
        st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #111827, #1E293B);
            padding: 40px;
            border-radius: 18px;
            border: 1px solid #D4AF37;
            text-align: center;
        ">
            <h1 style="color: #D4AF37; font-size: 48px;">
                ADUBASIM NONSO MIRACLE
            </h1>
            <h3 style="color: white;">
                Aspiring AI & Machine Learning Engineer
            </h3>
            <p style="color: #CBD5E1; font-size: 18px;">
                Building intelligent solutions through Python,
                Artificial Intelligence and Data Analysis.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
        col1, col2 = st.columns([1, 2])

        with col1:
            st.image("image/nonso.jpg", width=250)

            with col2:

                st.subheader("Aspiring AI & Machine Learning Engineer | Data Analyst")
        st.write(
        """
        Welcome to my portfolio!

        I am passionate about Artificial Intelligence,
        Machine Learning, Python programming, and Data Analysis.
        """
    )

        st.header("About Me")
        st.markdown(
        """
        <div style="
            background-color: #111827;
            padding: 25px;
            border-radius: 15px;
            border-left: 5px solid #D4AF37;
        ">
            <p style="font-size: 17px; line-height: 1.8; color: #E2E8F0;">
                I am an aspiring AI and Machine Learning Engineer
                with a strong interest in Artificial Intelligence and Data Analysis.

                I enjoy developing my programming skills, exploring
                machine learning technologies, and building practical
                projects that solve real-world problems.

                My goal is to continuously grow as a technology
                professional and contribute to innovative AI solutions.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

        st.write("")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Projects Built", "4")
        with col2:
            st.metric("Technical Skills", "10")
        with col3:
            st.metric("Career Focus", "AI / ML")

elif page == "About Me":
    st.header("Career Goals")

    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.subheader("🤖 AI & Machine Learning")
            st.write(
                """
                Developing my knowledge of machine learning,
                deep learning, and intelligent AI applications.
                """
            )

    with col2:
        with st.container(border=True):
            st.subheader("📊 Data Science & Analytics")
            st.write(
                """
                Improving my ability to analyze data,
                discover insights, and solve problems.
                """
            )

    st.header("Technical Skills")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Programming & Data")
        st.write("🐍 Python")
        st.write("🐼 Pandas")
        st.write("🔢 NumPy")
        st.write("📊 Matplotlib")
        st.write("📈 Scikit-learn")

    with col2:
        st.subheader("AI & Machine Learning")
        st.write("🤖 Machine Learning")
        st.write("🔥 PyTorch")
        st.write("🧠 Hugging Face Transformers")
        st.write("🌐 Streamlit")
        st.write("📉 Data Analysis")

elif page == "Skills":
    st.header("Technical Skills")

    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.subheader("Programming & Data")
            st.write("🐍 Python")
            st.write("🐼 Pandas")
            st.write("🔢 NumPy")
            st.write("📊 Matplotlib")
            st.write("📈 Scikit-learn")

    with col2:
        with st.container(border=True):
            st.subheader("AI & Machine Learning")
            st.write("🤖 Machine Learning")
            st.write("🔥 PyTorch")
            st.write("🧠 Hugging Face Transformers")
            st.write("🌐 Streamlit")
            st.write("📉 Data Analysis")

elif page == "Projects":
    st.header("My Projects")

    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.subheader("📊 Student Performance Analysis")
            st.link_button(
    "View Project on GitHub",
    "https://github.com/nonsoadubasim/Student_Performance_Analysis"
)

            st.write("Analyzed student scores using Python and Pandas.")

        with st.container(border=True):
            st.subheader("🤖 AI Spam Detector")
            st.link_button(
    "View Project on GitHub",
    "https://github.com/nonsoadubasim/Ai_spam_detector"
    
            )    
    
            st.write("Built a machine learning model to classify messages as spam or ham.")

    with col2:
        with st.container(border=True):
            st.subheader("💰 Sales Data Analysis")
            st.link_button(
    "View Project on GitHub",
    "https://github.com/nonsoadubasim/Sale_Data_Analysis"
)
            st.write("Analyzed sales data, revenue, and product performance.")

        with st.container(border=True):
            st.subheader("🧠 Sentiment and Word Prediction App")
            st.link_button(
    "View Project on GitHub",
    "https://github.com/nonsoadubasim/AI-Sentiment-and--word-prediction-App"
            )
    
            st.write("Built an AI application using Streamlit and Hugging Face Transformers.")

elif page == "Contact":
    st.header("Contact Me")
    st.write("I am open to learning opportunities, collaborations, and networking.")
    st.markdown(
        "[📧 Email Me](mailto:Miracleadubasim@gmail.com)"
    )
    st.markdown(
    "[![GitHub](https://img.shields.io/badge/GitHub-Visit%20My%20Profile-black?logo=github)](https://github.com/nonsoadubasim)"
)

st.markdown(
    "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect%20With%20Me-blue?logo=linkedin)](https://www.linkedin.com/in/nonsoadubasimtech/)"
)

st.markdown("---")
st.markdown(
    "<h4 style='text-align: center;'>Built with using Python and Streamlit</h4>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center;'>© 2026 Adubasim Nonso Miracle. All Rights Reserved.</p>",
    unsafe_allow_html=True,
)