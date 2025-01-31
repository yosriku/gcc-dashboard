import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
@st.cache_data
def load_data():
    data = pd.read_csv('data.csv')
    data = data[['Nama Peserta', 'Jumlah Course yang Telah Diselesaikan', 'Progress Belajar Percentage','Remark Progress Belajar']]
    return data

# Main function to run the Streamlit app
def main():
    st.title("Progress Belajar Peserta Advanced Data Analytics")

    # Load the data
    data = load_data()

    # Create a pie chart for the progress
    st.write("### Persentase Progress Belajar")

    # Calculate the counts for each progress category
    progress_counts = data['Remark Progress Belajar'].value_counts()

    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(progress_counts, labels=progress_counts.index, autopct='%1.1f%%', startangle=90,textprops={'color': 'white'})
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Set the background color of the figure to transparent
    fig.patch.set_facecolor('none')
    fig.patch.set_alpha(0)

    # Display the pie chart in Streamlit
    st.pyplot(fig)

    # Add interactivity: Allow user to filter data based on 'Remark Progress Belajar'
    st.write("### Filter Data Berdasarkan Progress")
    selected_remark = st.selectbox("Pilih progress belajar", data['Remark Progress Belajar'].unique())

    # Filter the data based on the selected remark
    filtered_data = data[data['Remark Progress Belajar'] == selected_remark]

    # Display the filtered data
    st.write(f"### Data untuk {selected_remark}")
    st.write(filtered_data)

# Run the app
if __name__ == "__main__":
    main()