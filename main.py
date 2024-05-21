import pickle

from flask import Flask, render_template, request

app = Flask(__name__)

with open("model.pkl", "rb") as file:
    random_forest = pickle.load(file)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        form_data = request.form

        year = form_data.get("year")
        month = form_data.get("month")

        if not year or not month:
            return render_template("index.html", month_post=0, result_post="Enter a valid year and month to get prediction.")
        
        try:
            year = int(year)
            month = int(month)
        except ValueError:
            return render_template("index.html", month_post=0, result_post="Enter a valid year and month to get prediction.")

        if year < 1950 or year > 2050:
            return render_template("index.html", month_post=0, result_post="Year should be between 1950 and 2050.")

        res = random_forest.predict([[int(year), int(month)]])[0]
        result = f"The rainfall prediction is {round(res, 2)} mm."

        return render_template("index.html", month_post=month, year_post=year, result_post=result)

    return render_template("index.html", month_post=0, result_post="")


if __name__ == "__main__":
    app.run(debug=True)
