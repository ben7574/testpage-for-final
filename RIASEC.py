import streamlit as st
from collections import Counter

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
# Define the options
options = ["Strongly Agree", "Agree", "Somewhat Agree", "Somewhat Disagree", "Disagree", "Strongly Disagree"]

# Mapping from options to RAISEC categories
option_to_raisec = {
    "Strongly Agree": "R",
    "Agree": "A",
    "Somewhat Agree": "I",
    "Somewhat Disagree": "S",
    "Disagree": "E",
    "Strongly Disagree": "C"
}

# Initialize the session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []

# Title of the app
st.title('RAISEC Assessment')

# Display the current question
question = questions[st.session_state.current_question]

# Use a form to ensure answers are submitted before moving to the next question
with st.form(key=f'question_{st.session_state.current_question}'):
    choice = st.radio(question, options)
    submitted = st.form_submit_button('Next')

    if submitted:
        # Record the answer
        st.session_state.answers.append(option_to_raisec[choice])

        if st.session_state.current_question < len(questions) - 1:
            # Move to the next question
            st.session_state.current_question += 1
        else:
            # All questions answered, calculate and display the results
            counts = Counter(st.session_state.answers)
            most_common = counts.most_common(3)

            # Ensure there are always three categories (pad with None or a default category if less than three)
            most_common += [(None, None)] * (3 - len(most_common))

            # Display the most common RAISEC categories
            st.subheader("Your Top 3 RAISEC Categories:")
            for category, count in most_common:
                if category:
                    st.write(f"{category}: {count}")

            # Define specific messages for combinations of top 3 RAISEC categories
            combination_messages = {
                ('R', 'A', 'I'): "Message for combination R, A, I.",
                ('R', 'none', 'none'): "You are part of society R",
                # Define other combinations and their messages as needed
                # You can also define messages for single or two-category combinations
            }

            # Get the top categories, excluding None
            top_categories = tuple(category for category, count in most_common if category)

            st.write("")  # Adding a space before the custom advice section

            # Display the specific message for the top combination
            if top_categories in combination_messages:
                message = combination_messages[top_categories]
                st.subheader("Custom Advice Based on Your Top Categories:")
                st.write(message)
            else:
                st.write("No specific advice for this combination.")
