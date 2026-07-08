import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import io # io = Input/Output — used to capture printed info
import uuid
import firebase_admin
from firebase_admin import credentials, firestore

# AI setup
from groq import Groq
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
def ask_ai(prompt):
    r = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role": "user", "content": prompt}])
    return r.choices[0].message.content
def init_firebase():
    if "FIREBASE_SERVICE_ACCOUNT_PATH" in st.secrets:
        cred = credentials.Certificate(st.secrets["FIREBASE_SERVICE_ACCOUNT_PATH"])
    elif "firebase" in st.secrets and isinstance(st.secrets["firebase"], dict):
        cred = credentials.Certificate(st.secrets["firebase"])
    else:
        return None

    try:
        app = firebase_admin.get_app()
    except ValueError:
        app = firebase_admin.initialize_app(cred)
    return firestore.client(app)


def save_dataset_metadata(db, uploaded_file, df):
    if not db:
        return

    metadata = {
        "name": uploaded_file.name,
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "missing_values": int(df.isnull().sum().sum()),
        "numeric_columns": df.select_dtypes(include=np.number).columns.tolist(),
        "uploaded_at": firestore.SERVER_TIMESTAMP,
    }

    try:
        doc_ref = db.collection("dataset_metadata").document(str(uuid.uuid4()))
        doc_ref.set(metadata)
        st.success("Saved dataset metadata to Firestore.")
    except Exception as e:
        st.error(f"Failed to save metadata to Firestore: {e}")


st.set_page_config(page_title='AI Data Analyst', page_icon='n', layout='wide')
st.title('\n AI Data Analysis Tool')

uploaded_file = st.file_uploader('Upload CSV file', type=['csv'])

db = init_firebase()

if uploaded_file:
    # Read the CSV file into a DataFrame (table)
    df = pd.read_csv(uploaded_file)

    if db:
        save_dataset_metadata(db, uploaded_file, df)
    else:
        st.info("Firebase is not configured. Add service account credentials to st.secrets.")

    # Show 3 summary numbers at the top
    c1, c2, c3 = st.columns(3)
    c1.metric('Rows', df.shape[0])
    c2.metric('Columns', df.shape[1])
    c3.metric('Missing', df.isnull().sum().sum())

    # Show first 10 rows as a scrollable table
    st.dataframe(df.head(10), use_container_width=True)

    # Find all columns with numbers
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

    # Dropdown menu for chart type selection
    chart_type = st.selectbox('Chart type:', ['Histogram', 'Box Plot', 'Heatmap', 'Scatter','Bar chart','line chart'])
    # Draw the selected chart
    if chart_type == 'Histogram' and numeric_cols:
        col = st.selectbox('Column:', numeric_cols)
        fig = px.histogram(df, x=col)
        st.plotly_chart(fig, use_container_width=True)
    elif chart_type == 'Bar chart' and numeric_cols:
        col = st.selectbox('Column:', numeric_cols)
        fig = px.bar(df, x=df.index, y=col)
        st.plotly_chart(fig, use_container_width=True)
    elif chart_type == 'line chart' and numeric_cols:
        col = st.selectbox('Column:', numeric_cols)
        fig = px.line(df, x=df.index, y=col)
        st.plotly_chart(fig, use_container_width=True)  
    elif chart_type == 'Box Plot' and numeric_cols:
        col = st.selectbox('Column:', numeric_cols)
        fig = px.box(df, y=col)
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == 'Heatmap' and len(numeric_cols) > 1:
        corr = df[numeric_cols].corr()
        fig = px.imshow(corr, text_auto=True)
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == 'Scatter' and len(numeric_cols) >= 2:
        x_col = st.selectbox('X axis:', numeric_cols, index=0)
        y_col = st.selectbox('Y axis:', numeric_cols, index=1)
        fig = px.scatter(df, x=x_col, y=y_col)
        st.plotly_chart(fig, use_container_width=True)
        st.subheader('AI Auto-Analysis')

    if st.button('Generate AI Insights'):
        with st.spinner('Analyzing...'):
            buf = io.StringIO()
            df.info(buf=buf)
            info_text = buf.getvalue()

            prompt = (
                'You are an expert data analyst.'
                ' Dataset info: ' + info_text +
                ' Statistical summary: ' + df.describe().to_string() +
                ' Give: 1) What the dataset is about'
                ' 2) Key patterns and trends'
                ' 3) Anomalies or outliers'
                ' 4) Three business recommendations'
                ' 5) Most important columns'
            )

            st.write(ask_ai(prompt))

    custom_q = st.text_area(
        'Ask a custom question:',
        placeholder='What is the average salary by department?'
    )

    if st.button('Ask AI') and custom_q:
        with st.spinner('Processing...'):
            prompt = (
                'Dataset sample: ' + df.head(20).to_string() +
                ' Columns: ' + str(list(df.columns)) +
                ' Question: ' + custom_q
            )
            st.info(ask_ai(prompt))
st.footer('Made with ❤️ by [Srinivas](https://www.linkedin.com/in/srinivasj03)')