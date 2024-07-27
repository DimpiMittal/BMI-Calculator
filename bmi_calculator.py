from pywebio.input import input_group, input, FLOAT
from pywebio.output import put_text, put_html
from pywebio import start_server

def bmi_calculator():
    # Inject custom CSS for styling and hiding the "Powered by PyWebIO" message
    put_html('''
    <style>
        body {
            background-color: #333; /* Dark grey background */
            color: #fff; /* White text color */
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
            border: 2px solid #ccc;
            padding: 20px;
            background-color: #444; /* Lighter grey background for container */
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            width: 100%;
        }
        input {
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
            width: calc(100% - 22px); /* Adjusting width to account for padding and border */
            box-sizing: border-box;
            background-color: #555; /* Slightly lighter grey for input background */
            color: #fff; /* White text color for inputs */
        }
        button {
            padding: 10px 20px;
            margin: 10px 0;
            border-radius: 5px;
            border: none;
            background-color: #007bff;
            color: #ffffff;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .pywebio_footer, .footer {
            display: none !important; /* Hide the "Powered by PyWebIO" message */
        }
        h1 {
            color: #fff; /* White text color for the heading */
            text-align: center;
        }
    </style>
    ''')

    # Add a heading at the top
    put_html('<h1>BMI Calculator</h1>')

    # Container for the inputs and result
    put_html('<div class="container">')

    # Using input_group to better organize the inputs with labels and placeholders
    data = input_group("BMI Calculator", [
        input("Height", name="height", type=FLOAT, placeholder="Input your height (cm)"),
        input("Weight", name="weight", type=FLOAT, placeholder="Input your weight (kg)")
    ])

    height = data['height']
    weight = data['weight']

    bmi = weight / (height / 100) ** 2

    if bmi <= 16:
        put_text('Your BMI is: %.1f. Category: Severely underweight' % bmi)
    elif bmi <= 18.5:
        put_text('Your BMI is: %.1f. Category: Underweight' % bmi)
    elif bmi <= 25:
        put_text('Your BMI is: %.1f. Category: Normal' % bmi)
    elif bmi <= 30:
        put_text('Your BMI is: %.1f. Category: Overweight' % bmi)
    elif bmi <= 35:
        put_text('Your BMI is: %.1f. Category: Moderately obese' % bmi)
    else:
        put_text('Your BMI is: %.1f. Category: Severely obese' % bmi)

    put_html('</div>')

if __name__ == '__main__':
    start_server(bmi_calculator, port=8080, debug=True)
