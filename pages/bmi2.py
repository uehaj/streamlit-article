import streamlit as st

def bmi(height, weight):
    return weight / (height / 100) ** 2

def main():
    if not (height := st.number_input("身長(cm)")):
        return
    if not (weight := st.number_input("体重(kg)")):
        return
    if height > 0 and weight > 0:
        bmi_value = bmi(height, weight)
        st.markdown(f"BMI= {bmi_value:.2f}")
    else:
        st.markdown("身長と体重を入力してください")

if __name__ == "__main__":
    main()
