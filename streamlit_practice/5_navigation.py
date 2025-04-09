import streamlit as st

### 아이콘은 다음 페이지에서 마음대로 가져다쓸 수 있습니다
### https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded
write_page = st.Page("pages_practice/1_write.py", title="글쓰기 페이지", icon=":material/edit_document:")
button_page = st.Page("pages_practice/2_button.py", title="버튼 페이지", icon=":material/switch:")

pg = st.navigation([write_page, button_page])

pg.run()