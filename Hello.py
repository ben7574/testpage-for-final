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

# Initialize session state
st.session_state.setdefault('current_question', 0)
st.session_state.setdefault('answers', [0] * len(questions))

# Title of the app
st.title('Working Style Assessment')

def calculate_working_style_score(answers):
    results = {"Not at all typical of you": 0, "Rarely typical of you": 0, "Occasionally typical of you": 0, "Sometimes typical of you": 0, "Often typical of you": 0, "Usually typical of you": 0, "Very typical of you at work": 0}
    for answer in answers:
        # Directly map answer to working_style
        if answer in options:
            results[options[answer]] += 1
    return results

# Define a callback function to handle the "Next" button click
def handle_next():
    # Increment the current question index or calculate and display the results
    if st.session_state.current_question < len(questions) - 1:
        st.session_state.current_question += 1
        display_question()
    else:
        # All questions answered, calculate and display the results
        display_results()

# Use st.empty() to create placeholders for your question and form
question_placeholder = st.empty()
form_placeholder = st.empty()

# Function to display the current question
def display_question():
    question = questions[st.session_state.current_question]
    question_placeholder.markdown(question)  # Use the placeholder to display the question
    # Generate a unique key for the form using the current question index
    form_key = f'question_{st.session_state.current_question}'
    
    # Display the radio buttons for options using the form placeholder
    with form_placeholder.form(key=form_key):
        answer = st.radio("", list(options.keys()), format_func=lambda x: options[x])
        submitted = st.form_submit_button('Next')
        if submitted:
            # Store the selected answer
            st.session_state.answers[st.session_state.current_question] = answer
            handle_next()

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
if st.session_state.current_question < len(questions):
    display_question()
else:
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
