import streamlit as st
import random
import datetime
import time

# 🌙 Set Page Config with Dark Theme
st.set_page_config(page_title="Eid Mubarak 🎉", page_icon="🌙", layout="wide")

# 🎨 Custom CSS for Digital Clock & Theme
st.markdown("""
    <style>
        .stApp {
            background-color: #222222;
            color: #ffffff;
        }
        .big-text {
            font-size: 32px;
            font-weight: bold;
            color: #6A0D;
            text-align: center;
            margin-top: 10px;
        }
        .eid-banner {
            width: 100%;
            border-radius: 10px;
        }
        .greet-box {
            background: #333333;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            border: 1px solid #ffffff;
        }
        .digital-clock {
            font-size: 24px;
            font-weight: bold;
            color: #6A0D;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# 🎉 List of Eid Greetings
eid_greetings = [
    "Eid Mubarak! 🌙 May your life be filled with joy and blessings!",
    "Wishing you and your family a blessed Eid filled with love and happiness! ✨",
    "Eid Mubarak! May this day bring peace, prosperity, and smiles to your heart! 💖",
    "On this joyous occasion, may Allah bless you with health and success. Eid Mubarak! 🎊",
    "May the magic of this Eid bring endless happiness to your life. Eid Mubarak! 🕌",
]

# 🌙 Function to Show Eid Countdown (3 Days of Eid)
def get_eid_countdown():
    today = datetime.date.today()
    eid_start_date = datetime.date(2025, 3, 31)  # Example Eid date (31st March 2025)
    eid_end_date = eid_start_date + datetime.timedelta(days=2)  # Eid lasts for 3 days

    if today < eid_start_date:
        days_left = (eid_start_date - today).days
        return f"Eid starts in {days_left} day(s)! 🎉"
    elif eid_start_date <= today <= eid_end_date:
        eid_day = (today - eid_start_date).days + 1
        return f"🎊 Eid Day {eid_day}! Enjoy the celebrations!"
    else:
        return "🎇 Eid has passed! Hope you had a great time! 😊"

# 🎊 Eid Mubarak Title
st.title("🌙 Eid Mubarak Greeting App 🎉")

# 🎇 Sidebar Eid Countdown
st.sidebar.image("Eid.webp" )
st.sidebar.markdown("## 🕰️ Eid Countdown")
st.sidebar.write(get_eid_countdown())

# 🕰️ Digital Clock (Live Update)
st.sidebar.markdown("## ⏳ Current Time")
clock_placeholder = st.sidebar.empty() 

# 🎉 Get User's Name for Personalized Greeting
name = st.text_input("Enter Your Name or Your Loved One's Name to Send Eid Wishes:", "")

# 🎊 Show Random Eid Greeting with User's Name
if st.button("Click for a Special Eid Greeting! 🎁"):
    greeting = random.choice(eid_greetings)
    personalized_greeting = f"*{name}*, {greeting}" if name else greeting
    st.markdown(f'<div class="greet-box"><p class="big-text">{personalized_greeting}</p></div>', unsafe_allow_html=True)

# 🎆 Eid Image Banner
st.image("eid-greet.png", caption="Eid Mubarak", use_container_width=True)

# 📬 Contact Section
st.sidebar.markdown("---")
st.sidebar.markdown("### 📬 Contact")
st.sidebar.write("📧 [Email Us](mailto:ismailahmedshahpk@gmail.com)")
st.sidebar.write("🔗 [LinkedIn](https://www.linkedin.com/in/ismail-ahmed-shah-2455b01ba/)")
st.sidebar.write("💬 [WhatsApp](https://wa.me/923322241405)")

# 🔄 **Real-time Digital Clock (Updates Every Second)**
while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S %p")
    clock_placeholder.markdown(f"<p class='digital-clock'>{current_time}</p>", unsafe_allow_html=True)
    time.sleep(1)
