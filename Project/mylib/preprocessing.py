import pandas as pd
def predict_career(arr):    
    df = pd.DataFrame(arr,columns=['Problem_Solving_Skill', 'Analytical_Ability', 
                                           'Logical_Reasoning', 'Social_Responsibility', 
                                           'Maths_score_12th ','NATA_Score', 'Interest_in_Biology_subject',
                                           'Thinking_Reasoning_Skills', 'Negotiation_Skill',
                                           'Number_Of_Design_Language', 'Expansive_Thinking',
                                           'Assurity_About_Work', 'Nift_Exam_Score', 'Typography_Skill',
                                           'Critical_Thinking_Skill', 'NEET_Score',
                                           'Experimental_skill', 'Communication_Skill', 'PCM_percentage_12th',
                                           'Coding_skills', 'Score_12th_Sci ', 'Diagnostic_skill',
                                           'Understanding_scientific_literature',
                                           'able_to_do_Mental_calculation', 'interpret_prescriptions_accurately',
                                           'Ready_to_take_care_of_animals', 'Do_you_like_animals',
                                           ' selfless_concern_for_the_wellbeing_of_others',
                                           'Good_Verbal_Communication', 'Team_Player',
                                           'Preference_Technical_Management', 'Continuous_Learning',
                                           'Patience_person', ' memory_skills', 'Budget_for_Graduation',
                                           'Interest_research_field', 
                                           'do_work_in_Team','Self_learning_capability'])
    
    df1 = pd.get_dummies(df, columns = ['able_to_do_Mental_calculation', 
                                                    'interpret_prescriptions_accurately',
                                                    'Ready_to_take_care_of_animals', 'Do_you_like_animals',
                                                    ' selfless_concern_for_the_wellbeing_of_others',
                                                    'Good_Verbal_Communication', 'Team_Player',
                                                    'Preference_Technical_Management', 'Continuous_Learning',
                                                    'Patience_person', ' memory_skills', 'Budget_for_Graduation',
                                                    'Interest_research_field','do_work_in_Team',
                                                    'Self_learning_capability'])
    
    return df1
                       