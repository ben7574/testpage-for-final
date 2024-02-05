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
        # Directly map answer to RAISEC test
        if answer in raisec_style:
            results[raisec_style[answer]] += 1
    return results

# Initialize session state
st.session_state.setdefault('current_question', 0)
st.session_state.setdefault('answers', [0] * len(questions))

# Title of the app
st.title('RAISEC Assessment')

# Display only the current question
current_q_and_o = questions_and_options[st.session_state.current_question]
question = current_q_and_o["question"]

# Use a form to ensure answers are submitted before moving to the next question
with st.form(key=f'question_{st.session_state.current_question}'):
    st.session_state.answers[st.session_state.current_question] = st.radio(
        question, 
        list(options.keys()), 
        format_func=lambda x: options[x]
    )
    submitted = st.form_submit_button('Next')

    if submitted:
        if st.session_state.current_question < len(questions_and_options) - 1:
            # Move to the next question
            st.session_state.current_question += 1
        else:
            # Calculate and display the results after the last question
            result = calculate_raisec_style(st.session_state.answers)
            st.subheader("Your RIASEC Test result says:")
            for style, count in result.items():
                st.write(f"{style}: {count}")


    # Sort the RAISEC styles by count in descending order
    sorted_styles = sorted(result.items(), key=lambda x: x[1], reverse=True)

    # Extract the top three RAISEC styles
    top_styles = sorted_styles[:3]

    message = f"You have the highest counts in: {', '.join([f'{style[0]} ({style[1]} counts)' for style in top_styles])}."

 # You can add more specific advice or career guidance based on top_style[0] and second_top_style[0]
            # For example:
        if top_style[0] == "R" and second_top_style[0] == "A" and third_top_style[0] == "S":
                message += " This allows you to study Law."
            # Add more conditions as needed for other combinations

    st.subheader("Custom Career Advice Based on RAISEC TEST:")
    st.write(message)
