# OLA RIDE INSIGHTS PROJECT
import streamlit as st
import pandas as pd
import os 
print(os.listdir())

st.set_page_config(
    page_title="OLA Ride Insights",
    page_icon="🚖",
    layout="wide"
)

df = pd.read_csv(r"C:\Users\Komal\OneDrive\Desktop\ola\code\cleaned_ola_data.csv")

st.title("🚖 OLA Ride Insights Dashboard")

st.markdown("Professional Ride Sharing Analytics Project")

st.markdown("---")


st.sidebar.header("FILTERS")

# Vehicle Filter
vehicle_filter = st.sidebar.multiselect(
    "Select Vehicle Type",
    options=df["Vehicle_Type"].unique(),
    default=df["Vehicle_Type"].unique()
)

# Payment Filter
payment_filter = st.sidebar.multiselect(
    "Select Payment Method",
    options=df["Payment_Method"].unique(),
    default=df["Payment_Method"].unique()
)


filtered_df = df[
    (df["Vehicle_Type"].isin(vehicle_filter)) &
    (df["Payment_Method"].isin(payment_filter))
]

total_bookings = filtered_df.shape[0]

total_revenue = filtered_df["Booking_Value"].sum()

average_distance = filtered_df["Ride_Distance"].mean()

successful_rides = filtered_df[
    filtered_df["Booking_Status"] == "Success"
].shape[0]


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Bookings",
    f"{total_bookings:,}"
)

col2.metric(
    "Total Revenue",
    f"₹ {total_revenue:,.0f}"
)

col3.metric(
    "Average Distance",
    round(average_distance, 2)
)

col4.metric(
    "Successful Rides",
    f"{successful_rides:,}"
)



st.markdown("---")

st.subheader("OLA Ride Dataset")

st.dataframe(filtered_df)

st.markdown("---")

st.subheader("Bookings by Vehicle Type")

vehicle_counts = filtered_df["Vehicle_Type"].value_counts()

st.bar_chart(vehicle_counts)


st.markdown("---")

st.subheader("Revenue by Payment Method")

payment_revenue = filtered_df.groupby("Payment_Method")["Booking_Value"].sum()

st.bar_chart(payment_revenue)

st.markdown("---")

st.subheader("Bookings by Hour")

hourly_bookings = filtered_df.groupby("Hour")["Booking_ID"].count()

st.line_chart(hourly_bookings)

# ---------- BOOKINGS BY DAY ---------- #

st.markdown("---")

st.subheader("Bookings by Day")

day_bookings = filtered_df.groupby("Day_Name")["Booking_ID"].count()

st.bar_chart(day_bookings)

# ---------- CUSTOMER RATINGS ---------- #

st.markdown("---")

st.subheader("Average Customer Ratings")

customer_ratings = filtered_df.groupby("Vehicle_Type")["Customer_Rating"].mean()

st.bar_chart(customer_ratings)

# ---------- DRIVER RATINGS ---------- #

st.markdown("---")

st.subheader("Average Driver Ratings")

driver_ratings = filtered_df.groupby("Vehicle_Type")["Driver_Ratings"].mean()

st.bar_chart(driver_ratings)

# ---------- PEAK HOUR CATEGORY ---------- #

st.markdown("---")

st.subheader("Peak Hour Category")

peak_hours = filtered_df.groupby("Peak_Hour_Category")["Booking_ID"].count()

st.bar_chart(peak_hours)

# ---------- WEEKDAY VS WEEKEND ---------- #

st.markdown("---")

st.subheader("Weekend vs Weekday Bookings")

weekend_data = filtered_df.groupby("Is_Weekend")["Booking_ID"].count()

st.bar_chart(weekend_data)

# ---------- BOOKING STATUS ---------- #

st.markdown("---")

st.subheader("Booking Status Distribution")

booking_status = filtered_df.groupby("Booking_Status")["Booking_ID"].count()

st.bar_chart(booking_status)

# ---------- RIDE DISTANCE ANALYSIS ---------- #

st.markdown("---")

st.subheader("Average Ride Distance by Vehicle")

distance_data = filtered_df.groupby("Vehicle_Type")["Ride_Distance"].mean()

st.bar_chart(distance_data)

# ---------- REVENUE PER KM ---------- #

st.markdown("---")

st.subheader("Revenue Per KM")

revenue_km = filtered_df.groupby("Vehicle_Type")["Revenue_Per_KM"].mean()

st.bar_chart(revenue_km)

st.markdown("---")

st.markdown(
    "Created by Komal | OLA Ride Insights Project"
)