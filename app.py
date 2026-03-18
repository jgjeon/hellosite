import streamlit as st

st.title("간단 계산기")

# 숫자 입력
num1 = st.number_input("첫 번째 숫자", value=0.0)
num2 = st.number_input("두 번째 숫자", value=0.0)

# 연산 선택
operation = st.selectbox("연산 선택", ["더하기", "빼기", "곱하기", "나누기"])

# 계산 버튼
if st.button("계산"):
    if operation == "더하기":
        result = num1 + num2
    elif operation == "빼기":
        result = num1 - num2
    elif operation == "곱하기":
        result = num1 * num2
    elif operation == "나누기":
        if num2 == 0:
            st.error("0으로 나눌 수 없습니다")
            result = None
        else:
            result = num1 / num2

    if result is not None:
        st.success(f"결과: {result}")
