import streamlit as st
import numpy as np
import pandas as pd

import data

st.title('Count')

st.subheader("Матриця компонентів", )
input_matrix = np.ones((4, 5))
input_matrix_st = st.data_editor(pd.DataFrame(input_matrix, index=[f"К{i+1}" for i in range(4)]))

st.divider()

tabs = st.tabs([f"Матриця згортання для П{i}" for i in range(1, 5)])
for i, tab in enumerate(tabs):
    with tab:
        st.write(pd.DataFrame(data.p[i]))

st.divider()

results_tabs = st.tabs([f"Обчислення для П{i}" for i in range(1, 5)])
for i, tab in enumerate(results_tabs):
    with tab:
        x, y = data.columns_for_calc[i]
        df_result = pd.DataFrame(data.count_calculation[i], columns=[f"Стан П{i+1}", x, y, "V1", "V2", "V1+V2", "min"])
        res_df = pd.DataFrame(data.count_p[i], index=["1", "2", "3", "4", "5", "∑", "∏"], columns=[f'П{i+1}'])
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(df_result, hide_index=True)
        with col2:
            st.dataframe(res_df)
        st.bar_chart(res_df.head())
        st.write(f"Кількість необхідних елементів: {res_df.iloc[6][f'П{i+1}']}")
