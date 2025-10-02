import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>Phân tích cảm xúc</title></head>
<body>
  <h2>Demo AI phân tích cảm xúc</h2>
  <form method="POST">
    <textarea name="text" rows="5" cols="40" placeholder="Nhập văn bản..."></textarea><br><br>
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

# Khi chạy local trực tiếp, app sẽ bind tới PORT do Render cung cấp (nếu có)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
