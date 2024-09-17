import streamlit as st

st.markdown("""
<style>
.st-emotion-cache-czk5ss.e16jpq800{
    visibility: hidden;
}
.st-emotion-cache-mnu3yk.ef3psqc5{
    visibility: hidden;
}
.st-emotion-cache-15ecox0.ezrtsby0{
    visibility: hidden;
}

</style>            
""", unsafe_allow_html=True)

# Survey form
st.title('Test_Survey')

# Question 1
q1 = st.selectbox(
        'What is the occupation of the person who contributes the most to the running of your household?',
        [
            'Worker',
            'Trader/Shopkeeper',
            'Clerical/sales/supervisory',
            'Executive',
            'Self‐employed professionals',
            'Businessman / Industrialist',
            'Farmer'
        ]
    )

    # Display questions based on Q1 response
if q1 == 'Worker':
        q2 = st.selectbox(
            'Which option applies best to his/her occupation?',
            ['Unskilled Worker', 'Skilled Worker']
        )

elif q1 == 'Trader/Shopkeeper':
        q3 = st.selectbox(
            'Which option applies best to his/her occupation?',
            ['Petty Trader', 'Shop Owner']
        )

elif q1 == 'Clerical/sales/supervisory':
        q4 = st.selectbox(
            'Which option applies best to his/her occupation?',
            ['Clerk / Salesman', 'Supervisory Level']
        )

elif q1 == 'Executive':
        q5 = st.selectbox(
            'Which option applies best to his/her occupation?',
            ['Officer / Executive – Junior', 'Officer / Executive – Middle / Senior']
        )

elif q1 == 'Businessman / Industrialist':
        q6 = st.selectbox(
            'Which option applies best to his/her occupation?',
            ['Businessman/Industrialist (No Employees)', 
             'Businessman/Industrialist (1 – 9 Employees)', 
             'Businessman/Industrialist (10+ Employees)']
        )

elif q1 == 'Farmer':
        q7 = st.selectbox(
            'Which option applies best to his/her occupation?',
            ['Farming on own land', 'Farming on leased land']
        )

# Question 8
q8 = st.multiselect(
        'Does your family have the following members?',
        ['Male member above 21 years', 'Female member above 21 years', 'None of the above']
    )

if 'Male member above 21 years' in q8:
        q9 = st.radio(
            'Do you have a male in the age group 18 to 20 in your household?',
            ['Yes', 'No']
        )

if 'Female member above 21 years' in q8:
        q10 = st.radio(
            'Do you have a female in the age group 18 to 20 in your household?',
            ['Yes', 'No']
        )

# Male Education
if 'Male member above 21 years' in q8:
        if q9 == 'Yes':
            male_education = st.selectbox(
                'Considering ALL the male member in the age group 18-20 years; what is the HIGHEST EDUCATED Male member’s education qualification?',
                [
                    'No formal education',
                    'Upto Class 5 standard',
                    'Class 6 – 9th standard',
                    'Class 10 ‐14 standard',
                    'Degree Regular (e.g. B.A., B.Sc., B.Com., M.A., M.Com)',
                    'Degree Professional (e.g. B.E., B.Tech., MTech., C.A., M.B.B.S., L.L.B., MBA)'
                ]
            )
        else:
            male_education = st.selectbox(
                'Considering ALL the male members above 21 years; what is the HIGHEST EDUCATED Male member’s education qualification?',
                [
                    'No formal education',
                    'Upto Class 5 standard',
                    'Class 6 – 9th standard',
                    'Class 10 ‐14 standard',
                    'Degree Regular (e.g. B.A., B.Sc., B.Com., M.A., M.Com)',
                    'Degree Professional (e.g. B.E., B.Tech., MTech., C.A., M.B.B.S., L.L.B., MBA)'
                ]
            )

    # Female Education
if 'Female member above 21 years' in q8:
        if q10 == 'Yes':
            female_education = st.selectbox(
                'Considering ALL the female member in the age group 18-20 years; what is the HIGHEST EDUCATED Female member’s education qualification?',
                [
                    'No formal education',
                    'Upto Class 5 standard',
                    'Class 6 – 9th standard',
                    'Class 10 ‐14 standard',
                    'Degree Regular (e.g. B.A., B.Sc., B.Com., M.A., M.Com)',
                    'Degree Professional (e.g. B.E., B.Tech., MTech., C.A., M.B.B.S., L.L.B., MBA)'
                ]
            )
        else:
            female_education = st.selectbox(
                'Considering ALL the female members above 21 years; what is the HIGHEST EDUCATED Female member’s education qualification?',
                [
                    'No formal education',
                    'Upto Class 5 standard',
                    'Class 6 – 9th standard',
                    'Class 10 ‐14 standard',
                    'Degree Regular (e.g. B.A., B.Sc., B.Com., M.A., M.Com)',
                    'Degree Professional (e.g. B.E., B.Tech., MTech., C.A., M.B.B.S., L.L.B., MBA)'
                ]
            )

if st.button('Submit'):
        st.write('Survey responses submitted!')
        # Process and save survey data here

