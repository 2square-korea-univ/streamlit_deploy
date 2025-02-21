import streamlit as st
import sqlite3
import pandas as pd

def main():
    st.title('데이터베이스 테이블 조회')
    
    # 데이터베이스 연결
    conn = sqlite3.connect('C:\\Users\\PowerElec2-000\\Documents\\streamlit_deploy\\my_database.db')
    
    # 테이블 목록 조회
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    if len(tables) == 0:
        st.warning("데이터베이스에 테이블이 없습니다.")
    else:
        # 테이블 선택 드롭다운
        table_names = [table[0] for table in tables]
        # table_names = []
        # for table in tables:
        #     table_names.append(table[0])
        selected_table = st.selectbox('테이블을 선택하세요:', table_names)
        
        if selected_table:
            # 선택된 테이블의 데이터 조회
            query = f"SELECT * FROM {selected_table}"
            df = pd.read_sql_query(query, conn)
            
            # 데이터 표시
            st.subheader(f'{selected_table} 테이블 데이터')
            st.dataframe(df)
    
    conn.close()

if __name__ == '__main__':
    main()