from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import pandas as pd

views = Blueprint('views', __name__)

csv_file_path = r"C:/Users/Atharva/Desktop/Smart-Course-Recommendation-Engine/FLASK WEB APPLICATION/data/merged2.csv"

# Read data from the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)


@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/recommendations')
@login_required
def recommendations():
    return render_template("recommendation.html", user=current_user)

@views.route('/filter-courses', methods=['POST', 'GET'])
@login_required
def filter():
    if request.method == 'POST':
        keyword = request.form.get('filter_keyword')
        price = request.form.get('filter_price')
        rating = request.form.get('filter_rating')
        duration = request.form.get('filter_duration')
        selected_category = request.form.get('filter_category')

        # Start with the original DataFrame
        filtered_df = df.copy()

        if selected_category:
            filtered_df = filtered_df[filtered_df['Category'].str.contains(selected_category, case=False, na=False)]


        # Apply filters based on user input
        if keyword:
            filtered_df = filtered_df[filtered_df['Title'].str.contains(keyword, case=False,na = False)]

        if price:
            try:
                filtered_df = filtered_df[filtered_df['Price'] <= price]
            except ValueError:
                flash("Invalid price input. Please enter a valid number.")

        if rating:
            try:
                rating = float(rating)
                filtered_df = filtered_df[filtered_df['Rating'] == rating]
            except ValueError:
                flash("Invalid rating input. Please enter a valid number.")

 

        products = filtered_df.to_dict(orient='records')


        return render_template("filtered_courses.html", products=products)

    return render_template("filter_courses.html")