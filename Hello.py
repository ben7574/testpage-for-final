import streamlit as st

def analyze_responses(responses):
    working_styles = {
        "Autonomous Style": [0, 0, 0, 0, 0],
        "Supportive Style": [0, 0, 0, 0, 0],
        "Directive Style": [0, 0, 0, 0, 0],
        "Conceptual Style": [0, 0, 0, 0, 0],
        "Social Style": [0, 0, 0, 0, 0],
        "Structural Style": [0, 0, 0, 0, 0],
        "Analytical Style": [0, 0, 0, 0, 0]
    }

    for i in range(len(responses)):
        for j in range(len(responses[i])):
            working_styles[list(working_styles.keys())[i]][j] = responses[i][j]

    total_scores = {}
    for style, scores in working_styles.items():
        total_scores[style] = sum(scores)

    best_style = max(total_scores, key=total_scores.get)

    return total_scores, best_style


def main():
    st.title("Working Style Questionnaire")

    st.write("Complete this questionnaire to gain an indication of your working style.")
    st.write("Score each of the following statements on a scale of 0 to 6 where:")
    st.write("0 is 'Not at all typical of you'")
    st.write("6 is 'Very typical of you at work'")
    st.write("There is no right or wrong answer. Use the full extent of the scale, answer each question honestly and as you feel or see yourself at work.")

    questions = {
        "Autonomous Style": [
            "How do you approach working independently on projects or tasks?",
            "How do you set goals and objectives for yourself?",
            "How do you prioritize your tasks and manage your workload?",
            "How do you handle challenges or obstacles when working independently?",
            "How do you stay motivated and committed to achieving your goals?"
        ],
        "Supportive Style": [
            "How do you offer support and encouragement to your peers?",
            "How do you respond when someone asks for help or assistance?",
            "How do you contribute to a positive and inclusive team environment?",
            "How do you handle feedback or constructive criticism from others?",
            "How do you prioritize the well-being and needs of others in your team or group?"
        ],
        "Directive Style": [
            "How do you take charge in group settings or team projects?",
            "How do you set goals and objectives for yourself or others?",
            "How do you make decisions when faced with uncertainty or ambiguity?",
            "How do you motivate yourself and others to achieve goals?",
            "How do you handle challenges or setbacks in your projects or tasks?"
        ],
        "Conceptual Style": [
            "How do you approach solving creative or open-ended problems?",
            "How do you respond to unexpected changes or disruptions?",
            "How do you generate new ideas or approaches to tasks?",
            "How do you handle ambiguity or uncertainty?",
            "How do you approach projects or tasks that require outside-the-box thinking?"
        ],
        "Social Style": [
            "How do you collaborate with peers on group projects?",
            "How do you handle conflicts or disagreements with peers?",
            "How do you build relationships with classmates or colleagues?",
            "How do you communicate your ideas or thoughts to others?",
            "How do you contribute to group discussions or activities?"
        ],
        "Structural Style": [
            "How do you organize your tasks or assignments?",
            "How do you manage your time effectively?",
            "How do you handle multiple tasks or projects simultaneously?",
            "How do you ensure your work is thorough and accurate?",
            "How do you approach long-term assignments or projects?"
        ],
        "Analytical Style": [
            "How do you approach solving a problem?",
            "How do you feel about working with data or numbers?",
            "How do you handle complex tasks or assignments?",
            "When making decisions, what is your approach?",
            "How do you respond to challenges or obstacles?"
        ]
    }

    responses = []

    for style, qs in questions.items():
        st.write(f"### {style}")
        st.write("Please rate the following statements:")
        for i, question in enumerate(qs):
            response = st.slider(f"{i+1}. {question}", 0, 6, 0)
            responses.append(response)

    st.write("Thank you for completing the questionnaire!")

    total_scores, best_style = analyze_responses([responses])

    st.write("### Total Scores:")
    for style, score in total_scores.items():
        st.write(f"- {style}: {score}")

    st.write("### Best Working Style:")
    st.write(f"The best working style for you is: **{best_style}**")


if __name__ == "__main__":
    main()
