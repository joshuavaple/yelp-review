import streamlit as st 
from yelpreview.utils.config import Config
from yelpreview.configs.config import CFGLog
from yelpreview.executor.inferrer import Inferrer

config = Config.from_json(CFGLog)
model_name = config.output.model_name

st.title("Streamlit example")

# write mark-down format
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
st.write(f"Selected trained model: {model_name}")
select_box = st.selectbox("Select the sub option", 
             ("option 1",
              "option 2"))
st.write(f"Selected option: {select_box}")

select_box = st.sidebar.selectbox("Select the main option", 
             ("option A",
              "option B"))
