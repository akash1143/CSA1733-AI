% Define diet suggestions based on diseases
diet_suggestion(high_blood_pressure, 'Eat low-sodium foods and reduce salt intake. Avoid processed foods and snacks. Include plenty of fruits, vegetables, and whole grains.').
diet_suggestion(diabetes, 'Follow a balanced diet with controlled carbohydrate intake. Choose whole grains, lean proteins, and healthy fats. Monitor portion sizes and limit sugary foods.').
diet_suggestion(high_cholesterol, 'Include heart-healthy fats like avocados and nuts. Choose lean proteins and limit saturated fats. Increase fiber intake with fruits, vegetables, and whole grains.').
diet_suggestion(celiac_disease, 'Avoid gluten-containing grains such as wheat, barley, and rye. Opt for gluten-free alternatives like rice, corn, and quinoa. Check food labels carefully.').
diet_suggestion(osteoporosis, 'Consume foods rich in calcium and vitamin D, such as dairy products, leafy greens, and fortified cereals. Include protein sources for bone health.').
diet_suggestion(iron_deficiency_anemia, 'Eat iron-rich foods like red meat, poultry, fish, and beans. Include vitamin C-rich foods to enhance iron absorption. Avoid excessive tea and coffee consumption.').
diet_suggestion(obesity, 'Focus on portion control and balanced meals. Include plenty of fruits, vegetables, and lean proteins. Limit sugary and high-calorie foods. Exercise regularly.').

% Query to get diet suggestion based on disease
get_diet_suggestion(Disease, Suggestion) :-
    diet_suggestion(Disease, Suggestion).
