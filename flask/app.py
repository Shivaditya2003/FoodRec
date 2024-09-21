from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Mapping dropdown values to integers starting from 0
dieting_level_map = {
    'strict': 0,
    'moderate': 1,
    'non-dieting': 2
}

spice_level_map = {
    'spicy': 0,
    'medium': 1,
    'mild': 2
}

time_of_day_map = {
    'breakfast': 0,
    'lunch': 1,
    'dinner': 2,
    'snack': 3
}

age_group_map = {
    'child': 0,
    'adult': 1,
    'senior': 2
}

cuisine_map = {
    'italian': 0,
    'chinese': 1,
    'mexican': 2,
    'indian': 3,
    'japanese': 4,
    'thai': 5,
    'greek': 6,
    'french': 7,
    'spanish': 8,
    'korean': 9,
    'vietnamese': 10,
    'turkish': 11,
    'moroccan': 12,
    'cuban': 13,
    'american': 14
}

# Mapping model output (integers) to string meal suggestions
meal_suggestions_map = {
    0: "Pasta Primavera",
    1: "Spicy Ramen",
    2: "Tacos",
    3: "Butter Chicken",
    4: "Sushi",
    5: "Pad Thai",
    6: "Greek Salad",
    7: "Croissant with Jam",
    8: "Paella",
    9: "Korean BBQ",
    10: "Pho",
    11: "Turkish Kebabs",
    12: "Moroccan Tagine",
    13: "Cuban Sandwich",
    14: "Burger and Fries"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('result.html', demand=None)
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Reading the form inputs and mapping them to numerical values starting from 0
        f1 = dieting_level_map[request.form['Dieting_Level']]
        f2 = spice_level_map[request.form['Spice_Level']]
        f3 = time_of_day_map[request.form['Time_of_Day']]
        f4 = age_group_map[request.form['Age_Group']]
        f5 = cuisine_map[request.form['Preferred_Cuisine']]

        # Creating input list
        input_df = [[f1, f2, f3, f4, f5]]

        # Load the model
        model_path = 'model.pkl'
        with open(model_path, 'rb') as f:
            loaded_model = pickle.load(f)

        # Predict the dish based on the input
        y_preds = loaded_model.predict(input_df)

        # Convert the integer prediction to a human-readable dish name
        suggested_meal = meal_suggestions_map.get(round(y_preds[0], 0), "Meal not found")

        return render_template('result.html', demand=suggested_meal)

    except Exception as e:
        print(f"Error occurred: {e}")
        return "An error occurred. Check the server logs for details."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
