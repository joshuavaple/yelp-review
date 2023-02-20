import streamlit as st 
from ..configs.config import CFGLog
# from ..utils.config import Config

# config = Config.from_json(CFGLog)

st.title("Streamlit example")

st.write("""
# Explore different classifiers
## 1. Linear classifiers
Linear regression \n
Logistic regression
## 2. Tree-based classifiers
XGBoost
""")

# whenever an option is selected in the FE, 
# the var will get assigned the selected value
select_box = st.selectbox("Select the sub option", 
             ("option 1",
              "option 2"))
st.write(f"Selected option: {select_box}")

select_box = st.sidebar.selectbox("Select the main option", 
             ("option A",
              "option B"))
