from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Phân tích cảm xúc</title>
</head>
<body>
    <h1>Demo phân tích cảm xúc văn bản</h1>
    <form method="POST">
        <textarea name="text" rows="5" cols="40"></textarea><br>
        <button type="submit">Phân tích</button>
    </form>
    {% if result %}
        <h3>Kết quả: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        text = request.form.get("text", "").lower()
        if any(word in text for word in ["vui", "hạnh phúc", "tốt"]):
            result = "😊 Tâm trạng: Vui"
        elif any(word in text for word in ["buồn", "chán", "khóc"]):
            result = "😢 Tâm trạng: Buồn"
        else:
            result = "😐 Không xác định"
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)

