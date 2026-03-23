import streamlit as st

# 영양성분별 제품 정보
product_dict = {
    "비타민B": "종근당 비타민B 컴플렉스 – 에너지 대사와 피로 회복",
    "마그네슘": "고려은단 마그네슘 – 근육 및 신경 기능 개선",
    "철분": "종근당 철분 엽산 비타민D 플러스 – 여성 빈혈 예방에 도움",
    "오메가3": "종근당 오메가3 – 혈행 개선과 눈 건강",
    "비타민D": "일동제약 비타민D3 2000IU – 뼈 건강과 면역력 강화",
    "포스파티딜세린": "하이큐포스파티딜세린 – 기억력 개선",
    "비타민C": "고려은단 비타민C 1000 – 항산화 및 면역력 증진",
    "아연": "뉴트리코어 아연 – 정상적인 면역 기능 유지",
    "프로폴리스": "종근당 프로폴리스 – 구강 건강 및 항산화",
    "L-테아닌": "뉴트립 릴렉스 L 테아닌 – 스트레스 및 집중력 향상",
    "아슈와간다": "뉴트리코스트 아슈와간다 – 피로 회복 및 활력 증진",
    "멜라토닌": "한미 멜라치오 – 수면 개선",
    "GABA": "셀핀다 발효 가바 – 긴장 완화 및 신경 안정",
    "엽산": "뉴트리코어 유기농 엽산 – 임신 준비 및 혈액 건강",
    "비타민B12": "뉴트리코스트 비타민 B12 – 신경 건강 및 피로 회복",
    "코엔자임Q10": "GNC 코엔자임Q10 – 심혈관 건강 지원",
    "루테인": "종근당 루테인 – 노화로 인한 눈 건강",
    "유산균": "락토핏 생유산균 골드 – 장 건강",
    "칼슘": "네이처메이드 칼슘 – 성장기 뼈 건강"
}

# 증상별 필요 영양성분
symptom_dict = {
    "피로": ["비타민B", "마그네슘", "아슈와간다", "코엔자임Q10"],
    "감기": ["비타민C", "프로폴리스", "아연"],
    "스트레스": ["L-테아닌", "GABA"],
    "불면": ["멜라토닌", "GABA"],
    "집중력 저하": ["포스파티딜세린", "오메가3", "비타민B12"],
    "빈혈": ["철분", "엽산"],
    "소화불량": ["유산균", "아연"],
    "심장 건강 걱정": ["오메가3", "코엔자임Q10"]
}

# 약물과의 상호작용 가능성이 있는 영양성분
drug_dict = {
    "항생제": ["아연", "철분"],
    "와파린": ["오메가3"],
    "항우울제": ["아슈와간다", "GABA"],
    "수면제": ["멜라토닌"],
    "혈압약": ["코엔자임Q10"]
}

# 주의 사항
side_effect_warning = {
    "비타민A": "비타민A는 과다 섭취 시 간 독성이 발생할 수 있으므로 주의하세요.",
    "철분": "철분은 과다 섭취 시 위장 장애를 유발할 수 있습니다.",
    "비타민D": "비타민D는 과다 섭취 시 고칼슘혈증이 발생할 수 있습니다."
}

# 중요도
priority = {
    "필수": "⭐⭐", 
    "보조": "⭐"}

# 구동
st.write("💊 아래 질문에 답하시면 적절한 영양제를 추천해 드립니다.")
st.write("⭐ 표시는 보조 성분, ⭐⭐ 표시는 주요 추천 성분입니다.")

symptoms = st.multiselect("🤖 어떤 증상이 있나요? (중복선택가능)", list(symptom_dict.keys()))
drugs = st.multiselect("🤖 복용 중인 약물이 있다면 선택해 주세요 (중복선택 가능)", list(drug_dict.keys()))
age = st.number_input("🤖 당신의 나이는 몇 살인가요?", min_value=1, max_value=100)
gender = st.radio("🤖 당신의 성별은 무엇인가요? ", ["남", "여"])

is_student = st.radio("🤖 당신은 학생인가요?", ["예", "아니오"])

if gender == "여":
    is_pregnant = st.radio("🤖 현재 임신 중인가요?", ["예", "아니오"])
else:
    is_pregnant = "아니오"

if is_student == "예":
    is_exam_period = st.radio("🤖 현재 수험 기간인가요?", ["예", "아니오"])
else:
    is_exam_period = "아니오"

is_vegetarian = st.radio("🤖 식단이 채식 위주인가요?", ["예", "아니오"])
low_sleep = st.radio("🤖 하루 수면 시간이 6시간 미만인가요?", ["예", "아니오"])
no_exercise = st.radio("🤖 일주일에 3회 이상 운동을 하지 않나요?", ["예", "아니오"])
poor_digestion = st.radio("🤖 소화가 잘 안 되나요?", ["예", "아니오"])
caffeine = st.radio("🤖 카페인을 자주 섭취하나요?", ["예", "아니오"])
memory_decline = st.radio("🤖 종종 기억력 저하를 느끼시나요?", ["예", "아니오"])

# 실행 버튼
if st.button("추천 받기"):

    nutrient_reasons = {}
    for s in symptoms:
        if s in symptom_dict:
            for nut in symptom_dict[s]:
                nutrient_reasons.setdefault(nut, []).append(f"'{s}' 증상")

    if age <= 19:
        nutrient_reasons.setdefault("칼슘", []).append("청소년")
    elif age >= 60:
        nutrient_reasons.setdefault("루테인", []).append("노년층")

    if is_pregnant == "예":
        for nut in ["엽산", "철분"]:
            nutrient_reasons.setdefault(nut, []).append("임신 중")

    if is_exam_period == "예":
        for nut in ["포스파티딜세린", "오메가3"]:
            nutrient_reasons.setdefault(nut, []).append("수험 기간")

    if is_vegetarian == "예":
        for nut in ["비타민B12", "철분", "오메가3"]:
            nutrient_reasons.setdefault(nut, []).append("채식 위주")

    if low_sleep == "예":
        for nut in ["멜라토닌", "GABA", "마그네슘"]:
            nutrient_reasons.setdefault(nut, []).append("수면 부족")

    if no_exercise == "예":
        for nut in ["비타민D", "마그네슘"]:
            nutrient_reasons.setdefault(nut, []).append("운동 부족")

    if poor_digestion == "예":
        for nut in ["아연", "유산균"]:
            nutrient_reasons.setdefault(nut, []).append("소화 불량")

    if caffeine == "예":
        for nut in ["마그네슘", "비타민B"]:
            nutrient_reasons.setdefault(nut, []).append("카페인 섭취")

    if memory_decline == "예":
        for nut in ["포스파티딜세린", "오메가3"]:
            nutrient_reasons.setdefault(nut, []).append("기억력 저하")

    excluded = []
    for drug in drugs:
        if drug in drug_dict:
            for avoid in drug_dict[drug]:
                if avoid in nutrient_reasons:
                    excluded.append(avoid)
                    del nutrient_reasons[avoid]

    if excluded:
        st.warning(f"⚠️ 제외된 성분 (약물 상호작용): {', '.join(excluded)}")

    st.write("✅ 추천 영양성분 및 제품:")
    for nut, reason_list in nutrient_reasons.items():
        stars = priority["필수"] if len(reason_list) >= 2 else priority["보조"]
        product = product_dict.get(nut, "제품 정보 없음")
        st.write(f"- {nut} ({stars}): {product}")
        if nut in side_effect_warning:
            st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⚠️ {side_effect_warning[nut]}")

    st.write("📌 추천 근거:")
    for nut, reason_list in nutrient_reasons.items():
        st.write(f"- {nut}: {', '.join(reason_list)}")
