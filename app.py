import streamlit as st
from huggingface_hub import InferenceClient
import datetime
st.set_page_config(page_title="AI Study Assistant", layout="wide")
st.title("AI Powered Study Assistant")
st.caption("Simplistic Learning Companion")
HF_TOKEN=st.secrets["HF_TOKEN"]
client=InferenceClient(model="meta-llama/Meta-Llama-3-8B-Instruct",token=HF_TOKEN)
def ask_ai(prompt):
    response=client.chat_completion(messages=[{"role":"user","content":prompt}],max_tokens=400,temperature=0.7)
    return response.choices[0].message.content
st.sidebar.header("Learning Tools")
feature=st.sidebar.selectbox("Choose a feature",["Explain Topic","Simplify Notes","Quiz Generator","Concept Dependency Map","Feynman Mode","Study Goal Planner","One-Page Revision Sheet"])
st.sidebar.markdown("---")
st.sidebar.caption("Built For Students")
st.markdown("Learning Space")
if feature=="Explain Topic":
    variable_1=st.text_input("Enter the topic you want explained")
    if st.button("Explain"):
        if variable_1:
            prompt=f"Explain the topic '{variable_1}' in simple terms suitable for a beginner.Use examples and step by step explanation."
            with st.spinner("Generating explanation..."):
                result=ask_ai(prompt)
                st.subheader("Explanation")
            st.write(result)
        else:
            st.warning("Please enter a topic to explain.")
elif feature=="Simplify Notes":
    variable_2=st.text_area("Paste your notes here", height=200)
    if st.button("Simplify"):
        if variable_2:
            prompt=f"Simplify the following notes for better understanding on the topic '{variable_2}'.Provide a concise summary with key points."
            with st.spinner("Simplifying notes..."):
                result=ask_ai(prompt)
                st.subheader("Simplified Notes")
            st.write(result)
        else:
            st.warning("Please paste your notes to simplify.")
elif feature=="Quiz Generator":
    variable_3=st.text_area("Enter the topic for quiz generation",height=200)
    if st.button("Generate Quiz"):
        if variable_3:
            prompt=f"Generate a 5-question quiz on the topic '{variable_3}' with multiple choice answers and provide the correct answer for each question.Include some conceptual,application-based and short-answer questions."
            with st.spinner("Generating quiz..."):
                result=ask_ai(prompt)
                st.subheader("Quiz")
            st.write(result)
        else:
            st.warning("Please enter a topic for quiz generation.")
elif feature=="Concept Dependency Map":
    variable_4=st.text_area("Enter the concept to create a dependency map for", height=200)
    if st.button("Create Concept Dependency Map"):
        if variable_4:
            prompt=f"Create a concept dependency map for the concept '{variable_4}'.List the prerequisite concepts and their relationships in a hierarchical format."
            with st.spinner("Creating concept dependency map..."):
                result=ask_ai(prompt)
                st.subheader("Concept Dependency Map")
            st.write(result)
        else:
            st.warning("Please enter a concept to create a dependency map for.")
elif feature=="Feynman Mode":
    variable_5=st.text_input("Concept name")
    variable_6=st.text_area("Explain the concept in a way that teaches the child", height=200)
    if st.button("Apply Feynman Technique"):
        if variable_6:
            prompt=f"A student explains the concept '{variable_5}' as follows: '{variable_6}'.Identify any gaps in understanding and provide a clearer, simplified explanation suitable for a student."
            with st.spinner("Applying Feynman Technique..."):
                result=ask_ai(prompt)
                st.subheader("Feynman Technique Result")
            st.write(result)
        else:
            st.warning("Please enter the concept explanation to apply Feynman Technique.")
elif feature=="Study Goal Planner":
    variable_7=st.text_input("Exam/Goal Name")
    variable_8=st.date_input("Exam/Goal Date", min_value=datetime.date.today())
    variable_9=st.text_area("List the topics to cover (separated by commas)", height=150)
    if st.button("Generate Study Plan"):
        if variable_9:
            days_left=(variable_8 - datetime.date.today()).days
            prompt=f"Create a study plan for the exam/goal '{variable_7}' scheduled on '{variable_8}'.The topics to cover are: '{variable_9}'.Distribute the topics evenly over the next {days_left} days and include daily study goals and revision sessions."
            with st.spinner("Generating study plan..."):
                result=ask_ai(prompt)
                st.subheader("Study Plan")
            st.write(result)
        else:
            st.warning("Please enter the topics to cover for the study plan.")
else:
    variable_10=st.text_input("Topic Nme")
    variable_11=st.text_area("Paste Notes(optional)", height=200,placeholder="you can paste your class notes here or leave it blank")
    if st.button("Generate Revision Sheet"):
        prompt=f"Create a one-page revision sheet for the topic '{variable_10}'.Use the following notes if provided: '{variable_11}'.Include key concepts, formulas, definitions,ommon mistakes or exam traps.Keep it concise and exam-oriented."
        with st.spinner("Generating revision sheet..."): 
            result=ask_ai(prompt)
            st.subheader("One-Page Revision Sheet")
        st.write(result)
    else:
        st.warning("Please enter the topic name to generate a revision sheet.")

st.markdown("---")
st.caption("Developed by Athul Antony")
