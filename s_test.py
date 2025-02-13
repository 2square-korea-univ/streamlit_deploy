import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("st.write() 활용 예시")

# 1. 텍스트 출력 (Markdown 지원)
st.write("## 마크다운 제목")
st.write("* 강조된 텍스트 *")

# 2. 데이터프레임 출력
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
st.write("### 데이터프레임")
st.write(df)

# 3. 그래프 출력 (Matplotlib)
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 2])
st.write("### Matplotlib 그래프")
st.pyplot(fig)
