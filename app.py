import requests
from flask import Flask, render_template, request
from scrapper import search_incruit

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword", "").strip()
    jobs = []
    error = None
    if not keyword:
        error = "검색어를 입력해 주세요."

    else:
        try:
            jobs = search_incruit(keyword)
        except requests.RequestException:
            app.logger.exception("채용 사이트 검색 요청 실패")
            error = "채용 사이트에 연결하지 못했습니다. 잠시 후 다시 검색해 주세요."
    return render_template("search.html", keyword=keyword, jobs=jobs, error=error)

if __name__ == "__main__":
    app.run(debug=True)
