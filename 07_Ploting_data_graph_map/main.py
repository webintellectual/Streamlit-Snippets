import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame(np.random.randn(100,3), columns=['a','b','c'])

st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)

fig, ax = plt.subplots()
ax.scatter(data['a'], data['b'])
plt.title("scatter")
st.pyplot(fig)

st.graphviz_chart('''
digraph{
    node1 -> node2
    node2 -> node3
    node3 -> node4
    node3 -> node1
}
''')

st.map()
city = pd.DataFrame({
    'awesome cities' : ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
    'lat' : [41.868171, 44.979840,  38.257972, 39.030575],
    'lon' : [-87.667458, -93.272474, -85.765187,  -95.702548]
})
st.map(city)