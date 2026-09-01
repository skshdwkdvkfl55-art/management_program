# ========================================================
# [과제] 23장 개인 지출 관리 프로그램 (콘솔 애플리케이션)
# 작성자 : [본인 이름]
# 파트너(짝) : [짝 이름]
# 작성일 : 2026-09-01
# ========================================================

# 우리가 만든 모듈에서 함수들 가져오기!
from storage import save_expenses, load_expenses
from summary import calculate_total, calculate_by_category
def add_expense(expenses):
    print("\n--- ➕ 새 지출 추가 ---")
    date = input("날짜 (YYYY-MM-DD): ").strip()
    category = input("카테고리 (예: 식비, 교통, 카페): ").strip()
    description = input("내용 (예: 점심, 버스, 커피): ").strip()
    
    # 1단계: 빈 문자열 검사
    if not date or not category or not description:
        print("⚠️ 날짜, 카테고리, 내용은 비워 둘 수 없습니다.")
        return
        
    # 2단계: 정수 변환 시도 및 예외 처리
    try:
        amount = int(input("금액 (원): "))
    except ValueError:
        print("⚠️ 금액은 반드시 정수(숫자)로 입력해 주세요.")
        return
        
    # 3단계: 0 이하의 비정상 금액 검사
    if amount <= 0:
        print("⚠️ 금액은 0보다 큰 값으로 입력해 주세요.")
        return
        
    # 모든 검사를 통과하면 딕셔너리로 묶어서 리스트에 추가!
    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }
    expenses.append(expense)
    print("✅ 지출 내역이 성공적으로 추가되었습니다.")


def show_expenses(expenses):
    if not expenses:
        print("\n⚠️ 등록된 지출 내역이 없습니다.")
        return
        
    print("\n=== 📋 전체 지출 내역 ===")
    number = 1
    for expense in expenses:
        # {expense['amount']:,} 를 쓰면 10000이 10,000으로 예쁘게 바뀝니다!
        print(f"{number}. {expense['date']} | {expense['category']} | {expense['description']} | {expense['amount']:,}원")
        number += 1

def main():
    file_path = "expenses.csv"  # 👈 4칸(Tab 1번) 들여쓰기
    
    # 4칸(Tab 1번) 들여쓰기
    expenses = load_expenses(file_path)
    print(f"\n📂 기존 지출 데이터 {len(expenses)}건을 불러왔습니다.")

    while True:                 # 👈 4칸(Tab 1번) 들여쓰기
        print("\n" + "=" * 35)  # 👈 8칸(Tab 2번) 들여쓰기
        print("     💰 개인 지출 관리 프로그램")
        print("=" * 35)
        print("1. 지출 추가")
        print("2. 지출 목록 조회")
        print("3. 지출 요약 보고서 (합계 & 카테고리)")
        print("4. CSV 파일 저장")
        print("0. 프로그램 종료")
        print("=" * 35)
        
        choice = input("메뉴 선택 >> ").strip()

        if choice == "1":
            add_expense(expenses)
            
        elif choice == "2":
            show_expenses(expenses)
            
        elif choice == "3":
            if not expenses:
                print("\n⚠️ 등록된 지출 내역이 없습니다.")
            else:
                total = calculate_total(expenses)
                cat_totals = calculate_by_category(expenses)
                
                print(f"\n📊 총 지출액: {total:,}원")
                print("--- 🏷️ 카테고리별 지출 ---")
                for cat, amt in cat_totals.items():
                    print(f"  • {cat}: {amt:,}원")
                    
        elif choice == "4":
            save_expenses(file_path, expenses)
            print("💾 CSV 파일에 안전하게 저장되었습니다.")
            
        elif choice == "0":
            save_expenses(file_path, expenses)
            print("\n👋 지출 내역을 저장하고 프로그램을 종료합니다. 수고하셨습니다!")
            break
            
        else:
            print("⚠️ 잘못된 메뉴 번호입니다. 0~4번 중에서 다시 선택해 주세요.")


if __name__ == "__main__":
    main()