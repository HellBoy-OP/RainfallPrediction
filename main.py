import numpy as np
import onnxruntime as rt
from flask import Flask, render_template, request

app = Flask(__name__)
session = rt.InferenceSession("model.onnx")


def is_valid_date(year: int, month: int):
    if year < 1950 or year > 2050:
        return False

    if month < 1 or month > 12:
        return False

    return True


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        form_data = request.form

        year = form_data.get("year")
        month = form_data.get("month")

        if not year or not month:
            return render_template(
                "index.html", month_post=0, result_post="Enter a valid date to get prediction.",
            )

        try:
            year = int(year)
            month = int(month)
        except ValueError:
            return render_template(
                "index.html", month_post=0, result_post="Enter a valid date to get prediction.",
            )

        if not is_valid_date(year, month):
            return render_template(
                "index.html", month_post=0, result_post="Enter a valid date to get prediction.",
            )

        input_name = session.get_inputs()[0].name
        label_name = session.get_outputs()[0].name

        data = np.array([[year, month]], dtype=np.float32)
        pred_onx = session.run([label_name], {input_name: data})[0]

        res = str(round(pred_onx[0, 0], 2))
        result = f"The rainfall prediction is {res} mm."

        return render_template(
            "index.html", month_post=month, year_post=year, result_post=result
        )

    return render_template("index.html", month_post=0, result_post="")


if __name__ == "__main__":
    app.run(debug=True)
