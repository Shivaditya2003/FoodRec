# DishDelight

Welcome to **DishDelight**!

At DishDelight, we believe that every meal should be an exceptional experience. We’re dedicated to transforming the way you dine by offering personalized menu recommendations that cater to your unique preferences, dietary needs, and current context. Our cutting-edge AI technology enhances your dining journey, making every meal not just enjoyable but unforgettable.

## Our Vision

Imagine a dining experience where every dish feels like it was made just for you. That’s the future we’re creating with DishDelight. We aim to take the guesswork out of choosing your next meal by leveraging advanced artificial intelligence to deliver tailored recommendations. Whether you’re revisiting an old favorite or exploring new culinary delights, our system ensures that each recommendation is spot-on.

## What We Do

### Personalized Recommendations

Our AI-driven system considers your past orders, dietary restrictions, and favorite cuisines to suggest dishes you’re most likely to enjoy.

### Real-Time Adaptation

We integrate real-time data like weather conditions and local events to ensure that our recommendations are relevant and timely.

### Smart Inventory Management

By aligning recommendations with the restaurant’s inventory, we help reduce food waste and enhance your dining experience.

## How It Works

1. **Data Collection:** We gather insights from your order history, user profiles, feedback forms, and real-time data to build a comprehensive understanding of your preferences.
2. **Intelligent Analysis:** Our sophisticated algorithms analyze patterns and predict what you’re likely to enjoy based on your profile and current conditions.
3. **Tailored Recommendations:** Using a blend of collaborative and content-based filtering, we generate suggestions that are both personalized and delightful.
4. **Seamless Integration:** Our system integrates smoothly with existing restaurant management tools, providing you with recommendations via tablets, mobile apps, and digital menu boards.

## Why Choose DishDelight?

- **Enhanced Experience:** Enjoy meals that are perfectly suited to your taste and current context.
- **Increased Satisfaction:** Discover new favorites and make every dining experience exceptional.
- **Reduced Waste:** Support sustainable dining practices with smart, inventory-based recommendations.

---

## Usage

1. Launch **VSCode**.
2. Open the `Model Training.ipynb` notebook.
3. Run the cells in the notebook to execute the code and see the results.
4. Feel free to modify the code or experiment with different models and parameters.

---

## Model Building and Selection

To predict the bike rental count, several machine learning models were implemented and evaluated. The following algorithms were utilized:

- Linear Regression
- Random Forest
- Extra Trees Regressor
- LightGBM
- XGBoost

After training and evaluating these models, **XGBoost** was chosen as the final model due to its superior performance in terms of accuracy and predictive power.

---

## Model Deployment

The selected **XGBoost** model was deployed using **Streamlit**, a Python library for building interactive web applications. The deployment allows users to input relevant features such as date, weather conditions, and time, and obtain the predicted bike rental count as the output.

---

## Project Structure
├── app.py # Main application file ├── model.pkl # Your model or data processing logic ├── static/ # Directory for static assets │ └── images/ # Folder for storing image files │ └── example.png # Example image ├── templates/ # Directory for HTML templates │ └── index.html # Main HTML file └── README.md # Documentation (optional)

---

## Deployment

You can access the deployed application [here](http://ec2-16-171-31-18.eu-north-1.compute.amazonaws.com:8080/).

---

Feel free to explore and contribute to the project!
