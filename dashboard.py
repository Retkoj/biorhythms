from datetime import datetime

import streamlit as st
from dateutil.relativedelta import relativedelta

from biorhytms_calculation import calculate_biorhythm_position

st.header('Biorhythm')

birth_date = st.date_input("Select date of birth", min_value=(datetime.today() - relativedelta(years=100)))
target_date = st.date_input("Select target date", datetime.today())

if birth_date > target_date:
    st.error("Birth date should be before target date")
time_delta_days = (target_date - birth_date).days
st.write(f'{time_delta_days} days between birth date and specified date')
physical_current_pos, emotional_current_pos, mental_current_pos = calculate_biorhythm_position(birth_date, target_date)

st.write(f'Physical currently at: {physical_current_pos}')
st.write(f'Emotional currently at: {emotional_current_pos}')
st.write(f'Physical currently at: {mental_current_pos}')


