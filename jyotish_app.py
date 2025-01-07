import streamlit as st
from datetime import datetime
from PIL import Image  # Importing required modules for image handling

# Function to calculate today's prediction
def daily_prediction():
    today = datetime.today().strftime('%d-%m-%Y')
    time = datetime.now().strftime('%H:%M:%S')
    return (f"Aaj ka din: {today} - Samay: {time}\n\n"
            "1. Aapka din shubh rahega.\n"
            "2. Aaj aapko naye avsar mil sakte hain.\n"
            "3. Aapka mann aur sharir dono energetic rahenge.\n"
            "4. Kaam mein safalta milegi.\n"
            "5. Aaj aapka din kaafi productive hoga.\n")

# Function for 'Current Situation' prediction
def current_situation():
    return ("Vartaman samay mein aap kuch challenges face kar rahe hain.\n"
            "1. Grah ki sthiti aapko financial growth aur personal life mein positive changes dikhayi deti hai.\n"
            "2. Aapko kuch personal aur professional decisions lene padenge.\n"
            "3. Aapki health ko lekar bhi thodi dhyan dena hoga.\n")

# Function to calculate marriage prediction based on age range
def marriage_prediction(dob):
    # Calculate age of the user
    current_year = datetime.now().year
    birth_year = dob.year
    age = current_year - birth_year
    
    # Marriage prediction based on age range (18-25 years for marriage)
    if age < 18:
        return "Aapke liye abhi shaadi ka samay nahi aaya hai. Kripya apne career aur padhai par dhyan de."
    elif 18 <= age <= 25:
        return "Aapke liye shadi ka yog abhi kaafi strong hai. Aapke liye 2023-2025 ke beech shaadi ke acchhe avsar hain."
    elif 26 <= age <= 30:
        return "Aap thoda late shaadi kar sakte hain, lekin 2026-2028 ke beech shaadi ka yog aayega."
    else:
        return "Aapki shaadi ho chuki hogi ya phir kuch aur zaroori faisle lene ka waqt hai."

# Streamlit application layout
def app():
    st.set_page_config(page_title="Jyotish Bhavishya Software", page_icon="🌟", layout="wide")
    
    # Display Image
    image_path = import streamlit as st
from datetime import datetime
from PIL import Image  # Importing required modules for image handling

# Function to calculate today's prediction
def daily_prediction():
    today = datetime.today().strftime('%d-%m-%Y')
    time = datetime.now().strftime('%H:%M:%S')
    return (f"Aaj ka din: {today} - Samay: {time}\n\n"
            "1. Aapka din shubh rahega.\n"
            "2. Aaj aapko naye avsar mil sakte hain.\n"
            "3. Aapka mann aur sharir dono energetic rahenge.\n"
            "4. Kaam mein safalta milegi.\n"
            "5. Aaj aapka din kaafi productive hoga.\n")

# Function for 'Current Situation' prediction
def current_situation():
    return ("Vartaman samay mein aap kuch challenges face kar rahe hain.\n"
            "1. Grah ki sthiti aapko financial growth aur personal life mein positive changes dikhayi deti hai.\n"
            "2. Aapko kuch personal aur professional decisions lene padenge.\n"
            "3. Aapki health ko lekar bhi thodi dhyan dena hoga.\n")

# Function to calculate marriage prediction based on age range
def marriage_prediction(dob):
    # Calculate age of the user
    current_year = datetime.now().year
    birth_year = dob.year
    age = current_year - birth_year
    
    # Marriage prediction based on age range (18-25 years for marriage)
    if age < 18:
        return "Aapke liye abhi shaadi ka samay nahi aaya hai. Kripya apne career aur padhai par dhyan de."
    elif 18 <= age <= 25:
        return "Aapke liye shadi ka yog abhi kaafi strong hai. Aapke liye 2023-2025 ke beech shaadi ke acchhe avsar hain."
    elif 26 <= age <= 30:
        return "Aap thoda late shaadi kar sakte hain, lekin 2026-2028 ke beech shaadi ka yog aayega."
    else:
        return "Aapki shaadi ho chuki hogi ya phir kuch aur zaroori faisle lene ka waqt hai."

# Streamlit application layout
def app():
    st.set_page_config(page_title="Jyotish Bhavishya Software", page_icon="🌟", layout="wide")
    
    # Display Image
    image_path = "https://github.com/umesh764/MY-JOTISH-APP/blob/main/shree%20ganesh.jpeg"  # Ensure this path is correct
    img = Image.open(image_path)
    st.image(img, caption="Shree Ganesh", width=150)
    
    # Title
    st.title("Jyotish Bhavishya Software")
    
    # Input fields for name and DOB
    name = st.text_input("Apna Naam Dijiye:")
    dob_input = st.text_input("Apna Janm Tithi (dd-mm-yyyy):")
    
    if name and dob_input:
        try:
            dob = datetime.strptime(dob_input, '%d-%m-%Y')
        except ValueError:
            st.error("Kripya sahi format mein DOB daalein (dd-mm-yyyy)")
            return
        
        # Prepare the predictions
        daily_pred = daily_prediction()
        current_sit = current_situation()
        marriage_pred = marriage_prediction(dob)

        # Display results in different tabs
        st.subheader("Aaj Ka Bhavishya")
        st.write(daily_pred)
        
        st.subheader("Vartaman Ka Bhavishya")
        st.write(current_sit)
        
        st.subheader("Shaadi Ka Bhavishya")
        st.write(marriage_pred)
    else:
        st.warning("Kripya apna naam aur janm tithi daalein.")

# Run the Streamlit app
if __name__ == "__main__":
    app()  # Ensure this path is correct
    img = Image.open(image_path)
    st.image(img, caption="Shree Ganesh", width=150)
    
    # Title
    st.title("Jyotish Bhavishya Software")
    
    # Input fields for name and DOB
    name = st.text_input("Apna Naam Dijiye:")
    dob_input = st.text_input("Apna Janm Tithi (dd-mm-yyyy):")
    
    if name and dob_input:
        try:
            dob = datetime.strptime(dob_input, '%d-%m-%Y')
        except ValueError:
            st.error("Kripya sahi format mein DOB daalein (dd-mm-yyyy)")
            return
        
        # Prepare the predictions
        daily_pred = daily_prediction()
        current_sit = current_situation()
        marriage_pred = marriage_prediction(dob)

        # Display results in different tabs
        st.subheader("Aaj Ka Bhavishya")
        st.write(daily_pred)
        
        st.subheader("Vartaman Ka Bhavishya")
        st.write(current_sit)
        
        st.subheader("Shaadi Ka Bhavishya")
        st.write(marriage_pred)
    else:
        st.warning("Kripya apna naam aur janm tithi daalein.")

# Run the Streamlit app
if __name__ == "__main__":
    app()
