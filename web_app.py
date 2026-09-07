from flask import Flask, render_template, request
from modules.url_analyzer import analyze_url

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/url-analyzer", methods=["GET", "POST"])
def url_analyzer_page():
    result = None
    submitted_url = ""
    error = None

    if request.method == "POST":
        submitted_url = request.form.get("url", "").strip()

        if not submitted_url:
            error = "请输入有效的 URL"
        else:
            result = analyze_url(submitted_url)

            if result is None:
                error = "URL 无效"

    return render_template(
        "url_analyzer.html",
        result=result,
        submitted_url=submitted_url,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)