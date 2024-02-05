import streamlit as st

questions = [
    "I prefer to work by myself most of the time.",
    "By choice I start new tasks whilst I have yet to complete others.",
    "I tire of meetings that go on too long, for example for more than an hour.",
    "When I chat with colleagues it is about their families and home life.",
    "It is when there is a crisis that I manage best.",
    "For meetings I arrive either just in time or slightly late.",
    "I take accurate notice of the details.",
    "I think that you have to be tough and resilient to survive in this world.",
    "I enjoy the prospect of starting new projects or tasks.",
    "I find it hard to say no if a colleague or manager asks me to do something I do not want to do.",
    "I often find that I have left some preparations to the last minute.",
    "I regularly make more than one draft of my letters or reports before submitting them.",
    "I have a fast work rate.",
    "The well-being of acquaintances in work concerns me.",
    "I often choose to do more than one thing at a time.",
    "I am not particularly concerned with being popular.",
    "I become interested when hearing what work others are involved in.",
    "I actively involve myself so that people enjoy work.",
    "I could be described as a perfectionist.",
    "It is important that I am popular with most people.",
    "My work pattern shows me working fastest as time-scales are due.",
    "I like to have a number of projects on the go at any one time.",
    "I think that it is important to keep my feelings to myself.",
    "I make sure that I have crossed all the ’t’s and dotted all the 'i's.",
    "I produce work with no mistakes in it."
]
# Options (the same for each question)
options = {
    1: "Not at all typical of you",
    2: "Rarely typical of you",
    3: "Occasionally typical of you",
    4: "Sometimes typical of you",
    5: "Often typical of you",
    6: "Usually typical of you",
    7: "Very typical of you at work"
}

# Function to calculate the working style score
def calculate_working_style_score(answers):
    total_score = sum(answers)  
    # Sum the values of the answers
    return total_score


# Initialize session state
st.session_state.setdefault('current_question', 0)
st.session_state.setdefault('answers', [0] * len(questions))

# Define a callback function to increment the current question or display results
def handle_next():
    # Increment the current question index or calculate and display the results
    if st.session_state.current_question < len(questions) - 1:
        st.session_state.current_question += 1
    else:
        # Display results if it's the last question
        display_results()



# Title of the app
st.title('Working Style Assessment')

# Display only the current question
if st.session_state.current_question < len(questions):
    question = questions[st.session_state.current_question]

    # Use a form to ensure answers are submitted before moving to the next question
    with st.form(key=f'question_{st.session_state.current_question}'):
        answer = st.radio(
            question, 
            list(options.keys()), 
            format_func=lambda x: options[x]
        )
        submitted = st.form_submit_button('Next', on_click=handle_next)
        
        if submitted:
            # Store the answer
            st.session_state.answers[st.session_state.current_question] = answer

# Function to display results
def display_results():
    score = calculate_working_style_score(st.session_state.answers)
    st.subheader("Your Working Style Score:")
    st.write(score)
    
    # Display the unique message based on the score
    message = get_message_for_score(score)
    st.subheader("Your Working Style:")
    st.write(message)

# Check if all questions have been answered and show the results
if st.session_state.current_question == len(questions):
    display_results()

# Function to get a unique message based on the total score
def get_message_for_score(score):
    if score <= 35:
        return "Your working style is highly independent and proactive."
    elif score <= 70:
        return "Your working style is independent with a preference for occasional collaboration."
    elif score <= 105:
        return "Your working style balances independence and teamwork."
    elif score <= 140:
        return "Your working style leans towards collaboration, with some preference for independence."
    elif score <= 175:
        return "Your working style is highly collaborative, preferring teamwork over working alone."
    else:
        return "Unique message for your score range or an error message if the score is out of expected range."

