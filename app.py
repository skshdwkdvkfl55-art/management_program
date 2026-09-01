# ========================================================
# [과제] 23장 개인 지출 관리 프로그램 (Flask 로컬 웹 서버)
# 작성자 : [본인 이름]
# 파트너(짝) : [짝 이름]
# 작성일 : 2026-09-01
# ========================================================

from flask import Flask, render_template, request, redirect, url_for
from storage import load_expenses, save_expenses
from summary import calculate_total, calculate_by_category

app = Flask(__name__)
FILE_PATH = "expenses.csv"


# 1. 메인 홈 페이지 (지출 목록 및 총액 조회)
@app.route("/")
def index():
    expenses = load_expenses(FILE_PATH)
    total = calculate_total(expenses)
    return render_template("index.html", expenses=expenses, total=total)


# 2. 새 지출 등록 페이지 (화면 표시 & 데이터 저장 처리)
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        date = request.form.get("date", "").strip()
        category = request.form.get("category", "").strip()
        description = request.form.get("description", "").strip()
        amount_str = request.form.get("amount", "").strip()
        
        # 유효성 검사 (빈 값 방지 및 숫자 변환)
        if date and category and description and amount_str.isdigit():
            amount = int(amount_str)
            if amount > 0:
                expenses = load_expenses(FILE_PATH)
                expenses.append({
                    "date": date,
                    "category": category,
                    "description": description,
                    "amount": amount
                })
                save_expenses(FILE_PATH, expenses)
                return redirect(url_for("index"))  # 저장 후 메인 홈으로 이동!
                
    return render_template("add.html")


# 3. 지출 요약 통계 페이지
@app.route("/summary")
def summary():
    expenses = load_expenses(FILE_PATH)
    total = calculate_total(expenses)
    category_totals = calculate_by_category(expenses)
    return render_template("summary.html", total=total, category_totals=category_totals)


# 로컬 웹 서버 실행 (포트 5000번)
if __name__ == "__main__":
    app.run(debug=True, port=5000)