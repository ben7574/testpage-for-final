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

def display_question(question):
    st.write(f"### {question['style']}")
    response = st.radio(f"{question['number']}. {question['text']}",
                        options=["Not at all typical of you",
                                 "Rarely typical of you",
                                 "Occasionally typical of you",
                                 "Sometimes typical of you",
                                 "Often typical of you",
                                 "Usually typical of you",
                                 "Very typical of you at work"], index=3)
    return response

def main():
    st.title("Working Style Questionnaire")

    st.write("Complete this questionnaire to gain an indication of your working style.")
    st.write("Score each of the following statements on a scale of 0 to 6 where:")
    st.write("0 is 'Not at all typical of you'")
    st.write("6 is 'Very typical of you at work'")
    st.write("There is no right or wrong answer. Use the full extent of the scale, answer each question honestly and as you feel or see yourself at work.")

    questions = [
        {"style": "Autonomous Style", "number": 1, "text": "How do you approach working independently on projects or tasks?"},
        {"style": "Autonomous Style", "number": 2, "text": "How do you set goals and objectives for yourself?"},
        {"style": "Autonomous Style", "number": 3, "text": "How do you prioritize your tasks and manage your workload?"},
        {"style": "Autonomous Style", "number": 4, "text": "How do you handle challenges or obstacles when working independently?"},
        {"style": "Autonomous Style", "number": 5, "text": "How do you stay motivated and committed to achieving your goals?"},
        {"style": "Supportive Style", "number": 1, "text": "How do you offer support and encouragement to your peers?"},
        {"style": "Supportive Style", "number": 2, "text": "How do you respond when someone asks for help or assistance?"},
        {"style": "Supportive Style", "number": 3, "text": "How do you contribute to a positive and inclusive team environment?"},
        {"style": "Supportive Style", "number": 4, "text": "How do you handle feedback or constructive criticism from others?"},
        {"style": "Supportive Style", "number": 5, "text": "How do you prioritize the well-being and needs of others in your team or group?"},
        {"style": "Directive Style", "number": 1, "text": "How do you take charge in group settings or team projects?"},
        {"style": "Directive Style", "number": 2, "text": "How do you set goals and objectives for yourself or others?"},
        {"style": "Directive Style", "number": 3, "text": "How do you make decisions when faced with uncertainty or ambiguity?"},
        {"style": "Directive Style", "number": 4, "text": "How do you motivate yourself and others to achieve goals?"},
        {"style": "Directive Style", "number": 5, "text": "How do you handle challenges or setbacks in your projects or tasks?"},
        {"style": "Conceptual Style", "number": 1, "text": "How do you approach solving creative or open-ended problems?"},
        {"style": "Conceptual Style", "number": 2, "text": "How do you respond to unexpected changes or disruptions?"},
        {"style": "Conceptual Style", "number": 3, "text": "How do you generate new ideas or approaches to tasks?"},
        {"style": "Conceptual Style", "number": 4, "text": "How do you handle ambiguity or uncertainty?"},
        {"style": "Conceptual Style", "number": 5, "text": "How do you approach projects or tasks that require outside-the-box thinking?"},
        {"style": "Social Style", "number": 1, "text": "How do you collaborate with peers on group projects?"},
        {"style": "Social Style", "number": 2, "text": "How do you handle conflicts or disagreements with peers?"},
        {"style": "Social Style", "number": 3, "text": "How do you build relationships with classmates or colleagues?"},
        {"style": "Social Style", "number": 4, "text": "How do you communicate your ideas or thoughts to others?"},
        {"style": "Social Style", "number": 5, "text": "How do you contribute to group discussions or activities?"},
        {"style": "Structural Style", "number": 1, "text": "How do you organize your tasks or assignments?"},
        {"style": "Structural Style", "number": 2, "text": "How do you manage your time effectively?"},
        {"style": "Structural Style", "number": 3, "text": "How do you handle multiple tasks or projects simultaneously?"},
        {"style": "Structural Style", "number": 4, "text": "How do you ensure your work is thorough and accurate?"},
        {"style": "Structural Style", "number": 5, "text": "How do you approach long-term assignments or projects?"},
        {"style": "Analytical Style", "number": 1, "text": "How do you approach solving a problem?"},
        {"style": "Analytical Style", "number": 2, "text": "How do you feel about working with data or numbers?"},
        {"style": "Analytical Style", "number": 3, "text": "How do you handle complex tasks or assignments?"},
        {"style": "Analytical Style", "number": 4, "text": "When making decisions, what is your approach?"},
        {"style": "Analytical Style", "number": 5, "text": "How do you respond to challenges or obstacles?"}
    ]

    responses = []

    for question in questions:
        response = display_question(question)
        responses.append(response)

    st.write("Thank you for completing the questionnaire!")

    total_scores, best_style = analyze_responses([responses])

    st.write("### Total Scores:")
    for style, score in total_scores.items():
        st.write(f"- {style}: {score}")

    st.write("### Best Working Style:")
    st.write(f"The best working style for you is: **{best_style}**")

    # Custom message based on the best style
    if best_style == "Autonomous Style":
        st.write("You have a strong tendency towards working independently and taking ownership of your tasks and goals. You prefer to set your own pace and direction.")
    elif best_style == "Supportive Style":
        st.write("You excel in supporting and collaborating with others, valuing teamwork and cooperation. You prioritize building positive relationships and helping your peers.")
    elif best_style == "Directive Style":
        st.write("You have a directive approach, taking charge and setting clear goals. You prefer to make decisions and guide others towards achieving objectives.")
    elif best_style == "Conceptual Style":
        st.write("You thrive in creative and innovative environments, enjoying problem-solving and exploring new ideas. You are adaptable and open-minded.")
    elif best_style == "Social Style":
        st.write("You excel in social interactions and teamwork, valuing collaboration and communication. You prioritize building strong relationships and contributing to group dynamics.")
    elif best_style == "Structural Style":
        st.write("You have strong organizational and time management skills, preferring structure and order in your work. You prioritize efficiency and thoroughness.")
    elif best_style == "Analytical Style":
        st.write("You have a logical and analytical approach, valuing data-driven decision-making and problem-solving. You prefer to analyze information and consider multiple perspectives.")

if __name__ == "__main__":
    main()
