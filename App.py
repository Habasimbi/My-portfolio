from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import os
#find more emojis here https:/./www.webfx.com/tools/emoji-chaet-sheet/
st.set_page_config(page_title="my portfolio", page_icon=":tada:", layout="wide")
def load_lottieurl(url):
    r = requests.get(url)
    if r. status_code !=200:
        return None
    return r.json()
# Function to load Lottie animation from URL
def local_css(file_name):
    try:
        print(f"Attempting to load CSS file from: {file_name}")
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file not found: {file_name}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

print(f"Current working directory: {os.getcwd()}")
local_css("style.css")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Call to load local CSS
local_css("style.css")
#----LOAD ASSETS----
lottie_coding = load_lottieurl("https://lottie.host/d69dfbad-54cd-4df5-9fbb-3e7d300f3205/Iqt3yL73CC.json")
img_contact_form = Image.open("Images/image.png")
img_lottie_animation = Image.open("Images/fat.png")
#---- HEARDER SECTION ----
with st.container():
    st.subheader("Hi,I am sandra :wave:")
    st.write("A Software Engineer From Zambia")
    st.write("I am passionate about cybersecurity, IoT, and app development, exploring how to secure IoT systems, create secure apps, and innovate with emerging tech")
    st.write("https://www.youtube.com/watch?v=7BLAmLX5S0Q")
   #---- WHAT I DO ---- 
with st.container():
   st.write("---")
   left_column, right_column = st.columns(2)
   with left_column:
           st.header("what i do")
           st.write("##")
           st.write(
           """
           A motivated final student at DMI St. Eugene University pursuing a degree in
Computer Science with a strong passion for both development, IoT, and
Cyber security, seeking opportunities to explore and excel in these dynamic
Fields. Proficient in programming languages such as Java, Python, and C++.
And Skilled in database management using SQL with experience in web
Development utilizing HTML, CSS, and JavaScript. Eager to learn and apply
Cyber security principles to secure digital assets and mitigate potential threats.
Proactive in seeking out opportunities for hands-on experience, internships,
And certifications to further enhance skills and knowledge in both
Development, IoT, and cyber security. Committed to leveraging technology for
Innovation while prioritizing the protection of data and systems against cyber
Threats.
"""

)
           st.write("[linkedIn profile >](www.linkedin.com/in/sandra-habasimbi-910023259)")
           with right_column:
               st_lottie(lottie_coding, height=300, key="")
               #----PROJECTS----
               with st.container():
                   st.write("---")
                   st.header("My pojects")
                   st.write("##")
                   image_column, text_column = st.columns((1,2))
                   with image_column:
                       st.image(img_lottie_animation)
                       with text_column:
                           st.subheader("intergrate lottie animation inside your streamlit App")
                           st.write(
                           """ learn hoe to use files in streamlit!
                           animations make out web app engaging and fun, and lottie files are the easiest way in this tutorial, i will sow exactly how to do it
                           """
                           )
                           st.markdown("[watch video...](www.youtube.com/@jasmine5604)")
                           #----CONTACT----
                           with st.container():
                               st.write("---")
                               st.header("Get in touch with me")
                               st.write("##")
                               #Documentation:https//formsubmit.co/!!! change email address!!!
                               contact_form = """
                               <form ation ="https://formsubmit.co/sandrahabasimbi@gmail.com" method="POST">
                               <input type="text" name="name" placeholder="your name" required>
                               <input type="email" name="email" placeholder= "your Email" required>
                               <textarea name+"message" placeholder="your message here" required></textarea>
                               <button type="submit">Send</button>
                               </form>
                               """
                               import streamlit as st

# Create two columns in the same line
column1, colunm2 = st.columns(2)

# Add content to the first column
with column1:
    st.markdown(contact_form, unsafe_allow_html=True)

# Add an empty space or other content to the second column
with colunm2:
    st.empty()

         

                               
                               





               


