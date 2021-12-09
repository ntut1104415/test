import streamlit as st
st.write('我們的組名: 隨便啦 先孤輪')

car_simulation = {'gas_warning':1, 'speed_limit':100, 'temp_warning':30,'rpm_limit':2000}
gas = st.number_input('油量的資料收集')
speed = st.number_input('車速的資料收集')
temp = st.number_input('溫度的資料收集')
rpm = st.number_input('轉速資料收集')
confirm_input=st.button('確認')
if confirm_input:
    if rpm >= car_simulation.get('rpm_limit'):
        st.write('轉速過高')
    else:
        st.write('正常') 
    if gas <= car_simulation.get('gas_warning'):
        st.write('油量足夠')
    else:
        st.write('油箱只剩', gas, '格! 準備加油!!')
    if speed>=car_simulation.get('speed_limit'):
       st.write('即將超速')
    else:
       st.write('安全')
    if temp>=car_simulation.get('temp_warning'):
       st.write('過熱')
    else:
       st.write('正常')
