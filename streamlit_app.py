#Day 1 of the 30 days challenge
import streamlit as st

st.write('Hello world!')

#Day 3
st.header('Greetings')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

     #day 5
     # 
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('Using the st.write() function')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({'first column': [1, 2, 3, 4], 'second column': [10, 20, 30, 40] })

st.write(df)

# Example 4
st.caption('DataFrame')
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
import streamlit as st


# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

#Example 6

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

#Example 7

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')