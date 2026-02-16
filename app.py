from flask import Flask, request, render_template_string

app = Flask(__name__)

students_db = {
    "surendra": {
        "name": "Surendra",
        "branch": "CSE",
        "selected": True,
        "company": "Google",
        "package": "24 LPA"
    },
    "rahul": {
        "name": "Rahul",
        "branch": "ECE",
        "selected": False
    }
}

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Placement Status Checker</title>

    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .container {
            width: 450px;
            background: rgba(255, 255, 255, 0.2);
            padding: 30px;
            border-radius: 15px;
            backdrop-filter: blur(12px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.25);
            text-align: center;
            color: white;
        }
        h1 {
            margin-bottom: 20px;
        }
        .search-box {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }
        .search-box input {
            flex: 1;
            padding: 10px;
            border-radius: 8px;
            border: none;
            outline: none;
        }
        .search-box button {
            padding: 10px 15px;
            background: #00eaff;
            color: black;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
        }
        .search-box button:hover {
            background: #00c4d6;
        }
        .card {
            margin-top: 20px;
            background: rgba(255,255,255,0.15);
            padding: 20px;
            border-radius: 12px;
            backdrop-filter: blur(10px);
            text-align: left;
        }
        .selected {
            color: #00ff99;
            font-weight: bold;
        }
        .rejected {
            color: #ff6969;
            font-weight: bold;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Placement Status Checker</h1>

    <form method="POST" class="search-box">
        <input type="text" name="student_name" placeholder="Enter Student Name" required>
        <button type="submit">Check</button>
    </form>

    {% if result %}
    <div class="card">
        <h2>Student Details</h2>

        <p><strong>Name:</strong> {{ result.name }}</p>
        <p><strong>Branch:</strong> {{ result.branch }}</p>

        {% if result.selected %}
            <p class="selected">Status: Selected</p>
            <p><strong>Company:</strong> {{ result.company }}</p>
            <p><strong>Package:</strong> {{ result.package }}</p>
        {% else %}
            <p class="rejected">Status: Not Selected</p>
        {% endif %}
    </div>
    {% endif %}
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        student_name = request.form.get("student_name").lower()
        result = students_db.get(student_name)

    return render_template_string(html_template, result=result)

if __name__ == "__main__":
    app.run(debug=True)
