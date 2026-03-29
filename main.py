from flask import Flask, request # Added 'request' to capture input
import calendar

doodhwale = Flask(__name__)

# 1. Added a Home route with a simple form to take input
@doodhwale.route("/")
def home():
    return '''
        <h2>Enter Month and Year</h2>
        <form action="/show" method="GET">
            Year: <input type="number" name="y" value="2025">
            Month: <input type="number" name="m" min="1" max="12">
            <input type="submit" value="Get Calendar">
        </form>
    '''

# 2. Changed the route to receive the form data
@doodhwale.route("/show")
def show_calendar():
    # Use request.args to get the 'y' and 'm' from the form
    year = int(request.args.get('y', 2025))
    month = int(request.args.get('m', 1))
    
    cal_html = calendar.month(year, month)
    return f"<pre>{cal_html}</pre><br><a href='/'>Back</a>"

if __name__ == "__main__":
    doodhwale.run(debug=True)