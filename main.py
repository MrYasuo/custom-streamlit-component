import streamlit as st

from st_dataframe_component import st_custom_slider

test = [
    {
        '_field': 'HT_FI_2190.PV',
        'Min': 17.4,
        'Max': 234.4,
        'Group': 'Dry Gas Seal',
        'Description': 'RD COMP. PRIMARY SEAL LEAKAGE DE',
        'Unit': 'mbar',
        'LLL': 0.0,
        'LL': 0.0,
        'L': 0.0,
        'H': 100.0,
        'HH': 300.0,
        'HHH': 790.0,
        'Flag': 1,
        'Evaluation': 'LOW - NORMAL;HIGH - PREALARM;'
    },
    {
        '_field': 'HT_FI_2191.PV',
        'Min': 2.9,
        'Max': 410.9,
        'Group': 'Dry Gas Seal',
        'Description': 'RD COMP. PRIMARY SEAL LEAKAGE NDE',
        'Unit': 'mbar',
        'LLL': 0.0,
        'LL': 0.0,
        'L': 0.0,
        'H': 100.0,
        'HH': 300.0,
        'HHH': 790.0,
        'Flag': 2,
        'Evaluation': 'LOW - NORMAL;HIGH - ALARM;'
    },
    {
        '_field': 'HT_LI_2180B.PV',
        'Min': 82.58,
        'Max': 82.61,
        'Group': 'Lube Oil System',
        'Description': 'OIL RESERVOIR',
        'Unit': '%',
        'LLL': 50.0,
        'LL': 50.0,
        'L': 55.0,
        'H': 65.0,
        'HH': 70.0,
        'HHH': 70.0,
        'Flag': 2,
        'Evaluation': 'HIGH - ALARM;'
    },
]

st.set_page_config(layout="wide")
v_custom = st_custom_slider(test)
