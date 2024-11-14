import streamlit as st

# App title and introduction
st.title("Promoting Healthy Light and Screen Use Habits")
st.write("""
This tool helps assess your screen use habits, readiness to adopt healthier lighting and screen practices, and provides tailored support to help you make informed choices for your well-being.
""")

# Section 1: Screen Use Habits Assessment
st.header("Step 1: Understanding Your Screen Use Habits")

# Expanded questions in Step 1
# Question 1: Estimated hours of daily screen time
screen_time = st.selectbox("How many hours a day do you estimate you spend with screens?", 
                           options=["Less than 2 hours", "2-4 hours", "4-6 hours", "6-8 hours", "More than 8 hours"])

# Question 2: Devices frequently used
devices = st.multiselect("Which of these devices do you interact with daily? Select all that apply.",
                         options=["Smartphone", "Tablet", "Laptop", "Desktop Computer", "Television", "Smart Watch", "E-Reader", "Gaming Console", "Other"])

# Question 3: Awareness of potential health effects
awareness = st.radio("Are you aware of any potential health impacts from frequent screen use?",
                     options=["Yes, I am aware", "No, I am not aware", "I've heard some information"])

# Additional questions in Step 1
handheld_with_lights = st.radio("Do you use handheld devices while other lights are on?",
                                options=["Yes", "No", "Sometimes"])

screen_time_dark = st.radio("Do you often use your devices in the dark?",
                            options=["Yes", "No", "Sometimes"])

phone_morning = st.radio("Do you use your phone first thing in the morning?", 
                         options=["Yes", "No"])

phone_bedtime = st.radio("How long do you use your phone before going to sleep?", 
                         options=["Less than 10 minutes", "10-30 minutes", "30-60 minutes", "More than 1 hour"])

morning_wait_time = st.selectbox("How long do you wait after waking up before using your phone?",
                                 options=["Immediately", "Within 15 minutes", "15-30 minutes", "More than 30 minutes"])

electronics_before_bed = st.radio("How many hours before bed do you stop using electronics?",
                                  options=["I use them until bed", "30 minutes", "1 hour", "2+ hours"])

device_distance = st.radio("At what distance do you typically view your devices?",
                           options=["Less than 12 inches", "12-18 inches", "18-24 inches", "More than 24 inches"])

eye_insurance = st.radio("Do you have eye care insurance or regularly visit an eye care professional?", 
                         options=["Yes", "No"])

# Calculate the Screen Use Score with additional questions
score = 0
if screen_time == "Less than 2 hours":
    score += 10
elif screen_time == "2-4 hours":
    score += 20
elif screen_time == "4-6 hours":
    score += 40
elif screen_time == "6-8 hours":
    score += 60
else:
    score += 80
score += len(devices) * 5
if awareness != "No, I am not aware":
    score += 10
if handheld_with_lights == "Yes":
    score += 5
if screen_time_dark == "Yes":
    score += 10
if phone_morning == "Yes":
    score += 5
if phone_bedtime == "More than 1 hour":
    score += 10
elif phone_bedtime == "30-60 minutes":
    score += 5
if morning_wait_time == "Immediately":
    score += 10
elif morning_wait_time == "Within 15 minutes":
    score += 5
if electronics_before_bed == "I use them until bed":
    score += 10
if device_distance == "Less than 12 inches":
    score += 10
elif device_distance == "12-18 inches":
    score += 5
if eye_insurance == "Yes":
    score -= 5
score = min(score, 100)

# Display score and provide initial feedback
st.write("### Your Screen Use Score: ", score, "%")
if score > 50:
    st.write("Your screen use habits indicate room for improvement. Below, we’ll provide tailored suggestions to support healthier habits.")

# Section 2: Readiness Assessment
st.header("Step 2: Assess Your Awareness and Readiness")

# Awareness scale
awareness_scale = st.radio("How would you rate your awareness of health impacts related to artificial light and screen use?",
                           options=["Very aware", "Slightly aware", "Minimally aware", "No awareness"])

# Additional Readiness Questions
readiness_desire = st.radio("How interested are you in learning more or taking steps to reduce health impacts?",
                            options=["Not interested", "Considering it", "Would like to but unsure how", "Actively taking steps"])

readiness_actions_taken = st.radio("Have you taken any steps to reduce potential health impacts of screen and light use?",
                                   options=["None", "Thinking about it", "Some steps", "Consistent changes"])

barriers = st.multiselect("What barriers prevent you from reducing screen time? Select all that apply.",
                          options=["Work or study requirements", "Entertainment", "Communication needs", "Habits or routines", "Lack of awareness", "Cost of alternatives", "Other"])

# Determine readiness stage based on responses
if awareness_scale == "No awareness" and readiness_desire == "Not interested":
    stage = "New to the Topic"
elif awareness_scale in ["Minimally aware", "Slightly aware"] and readiness_desire in ["Considering it", "Would like to but unsure how"]:
    stage = "Curious but Unsure"
elif awareness_scale == "Very aware" and readiness_desire == "Would like to but unsure how":
    stage = "Aware but Seeking Guidance"
elif awareness_scale == "Very aware" and readiness_desire == "Actively taking steps" and readiness_actions_taken in ["Some steps", "Consistent changes"]:
    stage = "Taking Positive Steps"
else:
    stage = "Balanced and Knowledgeable"

# Section 3: Personalized Support Based on Readiness Stage
st.header("Step 3: Your Personalized Support and Recommendations")
st.write(f"Based on your responses, you are in the **{stage}** stage.")

# Tailored support with enhanced recommendations
if stage == "New to the Topic":
    st.write("""
    **You’re just starting to learn about screen-related health impacts. Here are some tips to get you started:**
    - **Exposure to Natural Sunlight**: Morning sunlight helps your body naturally produce melatonin at night, which is vital not just for sleep but for immune health, antioxidant production, and regulating hormones like thyroid and adrenal.
    - **Potential Effects**: Excessive artificial light at night can disrupt sleep, increase risks of obesity, and cause excess daytime sleepiness.
    - **Simple Tips**:
        - **20-20-20 Rule**: Every 20 minutes, look 20 feet away for 20 seconds to reduce eye strain.
        - **Dim Lighting in the Evening**: Dim lights at night to reduce stimulation and help your body wind down.
        - **Resource Links**:
            - [DarkSky.org](https://www.darksky.org) - Information on light pollution and health.
            - [National Sleep Foundation](https://www.sleepfoundation.org) - Sleep health.
    """)

elif stage == "Curious but Unsure":
    st.write("""
    **You’re interested but may need guidance on practical steps to reduce exposure. Here’s how to start:**
    - **Use Blue Light Filters**: Enable blue light filters on devices and consider blue light glasses if using screens at night.
    - **Device Use in Bed**: Limit screen use in bed and aim to stop screen time at least 30 minutes before bed.
    - **Consider Light Colors**:
        - Use **warm light (below 3000K)** at night and dim it when possible.
        - Use **cool light (blue) during the day** to align with natural daylight, but reduce this light in the evening.
    - **Resources**:
        - [Flux - Blue Light Filter](https://justgetflux.com)
        - [All About Vision - Eye Health](https://www.allaboutvision.com)
    """)

elif stage == "Aware but Seeking Guidance":
    st.write("""
    **You’re aware and looking for concrete actions. Here are some targeted strategies:**
    - **Morning Sunlight Exposure**: Exposure to morning sunlight helps regulate melatonin production, supports immune health, and promotes overall well-being.
    - **Check Light Bulb Packaging**: Look for CCT ratings below 3000K for evening use and ensure these bulbs can be dimmed.
    - **Color Temperature Apps**: Install apps to manage screen color temperature (e.g., blue during the day, warmer at night).
    - **Specific Tips**:
        - Use lamps over ceiling lights in the evening to reduce brightness.
        - Take micro-breaks: Stretch, walk, or take deep breaths every hour.
        - Resource Links:
            - [Eye Health Exercises](https://www.aao.org/eye-health/tips-prevention/computer-usage)
    """)

elif stage == "Taking Positive Steps":
    st.write("""
    **You’re already implementing good practices! Consider these advanced tips:**
    - **Fine-tune Light Levels**: Adjust light intensity and color to match your schedule (cooler during the day, warmer at night).
    - **Track Progress**: Use apps like [Sleepio](https://www.sleepio.com) to monitor sleep improvement.
    - **Add Movement Breaks**: Regular movement improves focus, reducing dependency on screens.
    - **Ongoing Resources**:
        - [Headspace](https://www.headspace.com) for relaxation.
        - [All About Vision](https://www.allaboutvision.com) for eye health guidance.
    """)

elif stage == "Balanced and Knowledgeable":
    st.write("""
    **You have excellent habits. Here’s how to stay on track:**
    - **Stay Consistent**: Keep monitoring light sources and device settings.
    - **Be a Role Model**: Share your knowledge with others.
    - **Resources for Maintaining Balance**:
        - [American Academy of Sleep Medicine](https://aasm.org)
        - [National Institute of Occupational Safety and Health](https://www.cdc.gov/niosh)
    """)

st.write("Thank you for using this app! We hope it provides a supportive way to enhance your screen habits without stress.")
