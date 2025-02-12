import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load the data from the CSV file
@st.cache_data
def load_data():
    data = pd.read_csv('data.csv')
    data = data[['Nama Peserta', 'Jumlah Course yang Telah Diselesaikan', 'Progress Belajar Percentage', 'Remark Progress Belajar']]
    return data

# Function to calculate the countdown
def countdown(target_date):
    now = datetime.now()
    time_left = target_date - now
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return days, hours, minutes, seconds

# Main function to run the Streamlit app
def main():
    # Menampilkan Last Updated di bagian atas dengan teks kecil
    st.markdown(f"<p style='font-size:12px; text-align:right; color:gray;'>Last Updated: 12-02-2025 at 08.30 WIB </p>", unsafe_allow_html=True)

    # Set target date for countdown (28 February 23:59)
    target_date = datetime(2025, 2, 28, 23, 59, 0)  

    # Calculate countdown
    days_left, hours_left, minutes_left, _ = countdown(target_date)

    # Display countdown at the top
    st.write(f"### Waktu Tersisa Hingga Program Berakhir: {days_left}d {hours_left}h {minutes_left}m")

    st.title("Progress Belajar Peserta Advanced Data Analytics")

    # Load the data
    data = load_data()

    # Create a pie chart for the progress
    st.write("### Persentase Progress Belajar")

    # Calculate the counts for each progress category
    progress_counts = data['Remark Progress Belajar'].value_counts()

    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(progress_counts, labels=progress_counts.index, autopct='%1.1f%%', startangle=90, textprops={'color': 'white'})
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

    # Tambahkan informasi tambahan di bawah tabel
    st.write("### Informasi Tambahan")
    st.markdown("""
    - **Rekomendasi course saat ini adalah telah menyelesaikan course bagian 5 "Google Advanced Data Analytics Capstone"**
    - **Panduan Peserta:** [Link Panduan Peserta](https://docs.google.com/document/d/1lmDdTRtfZdrdRBXlYXOaN56pKj0qNFvEM_EbW-LOn_U/edit?usp=sharing)
    - **Cek Sertifikat:** [Link Cek Sertifikat](https://www.coursera.org/accomplishments)
    - **Jika ada kesalahan nama pada sertifikat, silahkan mengisi form di link berikut:** [Link Form Ganti Nama](https://coursera.support/s/learner-help-center-contact-us)
    """)

# Run the app
if __name__ == "__main__":
    main()
