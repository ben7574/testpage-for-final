import streamlit as st
from collections import Counter

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
# Define your questions, options, and other constants here

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = [0] * len(questions)

st.title('Working Style Assessment')

# Display the current question
if st.session_state.current_question < len(questions):
    question = questions[st.session_state.current_question]
    st.write(f"Question {st.session_state.current_question + 1}/{len(questions)}: {question}")
    form_key = f'question_form_{st.session_state.current_question}'  # Unique key for each form
    with st.form(key=form_key):
        selected_option = st.radio("Select an option:", list(options.values()), key=f'option_{st.session_state.current_question}')
        submitted = st.form_submit_button('Next')
        if submitted:
            # Save the selected option's score (assuming the options are 1-indexed)
            score = list(options.keys())[list(options.values()).index(selected_option)]
            st.session_state.answers[st.session_state.current_question] = score
            # Move to the next question
            if st.session_state.current_question < len(questions) - 1:
                st.session_state.current_question += 1
            else:
                # If it's the last question, calculate and display the results
                total_scores, best_style = analyze_responses(st.session_state.answers)
                st.write("### Total Scores:")
                for style, score in total_scores.items():
                    st.write(f"{style}: {score}")
                st.write("### Best Working Style:")
                st.write(f"The best working style for you is: **{best_style}**")
                # Display the custom message based on the best style
                # ... [Your logic for displaying the custom message]

# No need to call display_question() at the end

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
