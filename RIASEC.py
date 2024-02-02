import streamlit as st

questions = [
    "I prefer to work by myself most of the time.",
    "I like to work on cars",
    "I like to do puzzles",
    "I am good at working independently",
    "I like to work in teams",
    "I am an ambitious person, I set goals for myself",
    "I like to organize things, (files, desks/offices)",
    "I like to build things",
    "I like to read about art and music",
    "I like to have clear instructions to follow",
    "I like to try to influence or persuade people", 
    "I like to do experiments",
    "I like to teach or train people",
    "I like trying to help people solve their problems",
    "I like to take care of animals",
    "I wouldn’t mind working 8 hours per day in an office",
    "I like selling things",
    "I enjoy creative writing",
    "I enjoy science",
    "I am quick to take on new responsibilities",
    "I am interested in healing people",
    "I enjoy trying to figure out how things work",
    "I like putting things together or assembling things",
    "I am a creative person",
    "I pay attention to details",
    "I like to do filing or typing",
    "I like to analyze things (problems/ situations)",
    "I like to play instruments or sing",
    "I enjoy learning about other cultures",
    "I would like to start my own business",
    "I like to cook",
    "I like acting in plays",
    "I am a practical",
    "I like working with numbers or charts",
    "I like to get into discussions about issues",
    "I am good at keeping records of my work",
    "I like to lead",
    "I like working outdoors",
    "I would like to work in an office",
    "I’m good at math",
    "I like helping people",
    "I like to draw",
    "I like to give speeches"
]

# Options (the same for each question)
options = {
    1: "Strongly Agree",
    2: "Agree",
    3: "Somewhat Agree", 
    4: "Somewhat Disagree", 
    5: "Disagree",
    6: "Strongly Disagree"
}

# To assign a value to each of the options
raisec_style = {
    1: "R",
    2: "A",
    3: "I",
    4: "S",
    5: "E",
    6: "C"
}

# Function to calculate the RAISEC score
def calculate_raisec_style(answers):
    results = {"R": 0, "I": 0, "A": 0, "S": 0, "E": 0, "C": 0}
    for answer in answers:
        # Directly map answer to learning style
        if answer in raisec_style:
            results[raisec_style[answer]] += 1
    return results

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
st.title('RAISEC Assessment')

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
            if st.session_state.current_question < len(questions) - 1:
                # Move to the next question
                st.session_state.current_question += 1
            else:
                # Calculate and display the results after the last question
                result = calculate_raisec_style(st.session_state.answers)
                st.subheader("Your Learning Style Preferences:")
                for style, count in result.items():
                    st.write(f"{style}: {count}")

                # Sort the learning styles by count in descending order
                sorted_styles = sorted(result.items(), key=lambda x: x[1], reverse=True)

                # Extract the top two learning styles
                top_style = sorted_styles[0]
                second_top_style = sorted_styles[1]

                # Display a custom message based on the highest and second-highest learning styles
                message = f"You have the highest count in {top_style[0]} learning ({top_style[1]} counts) and the second-highest in {second_top_style[0]} learning ({second_top_style[1]} counts)."
                
                # You can add more specific advice or career guidance based on top_style[0] and second_top_style[0]
                # For example:
                if top_style[0] == "Visual" and second_top_style[0] == "Aural":
                    message += " This combination is suitable for careers that involve visual and auditory skills, such as graphic design or music production."
                # Add more conditions as needed for other combinations

                st.subheader("Custom Career Advice Based on RAISEC TEST:")
                st.write(message)

# Function to get a unique message based on the total score
def get_message_for_score(score):
    if score <= 35:
        return "Your style is highly independent and proactive."
    elif score <= 70:
        return "Your working style is independent with a preference for occasional collaboration."
    elif score <= 105:
        return "Your working style balances independence and teamwork."
    elif score <= 140:
        return "Your working style leans towards collaboration, with some preference for independence."
    elif score <= 175:
        return "Your working style is highly collaborative, preferring teamwork over working alone."
    else:
        return "Unique message for your score range or an error message if the score is out of the expected range."
