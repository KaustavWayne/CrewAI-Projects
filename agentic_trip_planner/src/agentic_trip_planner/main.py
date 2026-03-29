import streamlit as st
import json
from datetime import datetime

from agentic_trip_planner.crew import run_crew
from agentic_trip_planner.tools.currency_tool import convert_currency

st.set_page_config(page_title="VoyageAI", page_icon="✈️", layout="wide")

# ---------- STYLE ----------
st.markdown("""
<style>
.card {
    background: white;
    padding: 16px;
    border-radius: 12px;
    margin-bottom: 12px;
    border: 1px solid #eee;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title("✈️ VoyageAI")
st.markdown("### AI Trip Planner (CrewAI)")

# ---------- SESSION ----------
if "trip_plan" not in st.session_state:
    st.session_state.trip_plan = None

# ---------- SIDEBAR ----------
with st.sidebar:
    st.header("Plan Your Trip")

    destination = st.text_input("Destination", "Tokyo")

    travel_date = st.date_input(
        "Travel Date",
        value=datetime.now().date(),
        min_value=datetime.now().date()
    )

    days = st.slider("Days", 1, 10, 3)
    travelers = st.number_input("Travelers", 1, 10, 2)
    budget = st.selectbox("Budget", ["low", "moderate", "luxury"])

    generate = st.button("🚀 Generate Plan")

# ---------- GENERATE ----------
if generate:
    with st.spinner("Planning your trip..."):
        result = run_crew({
            "destination": destination,
            "days": days,
            "budget": budget,
            "travelers": travelers,
            "travel_date": str(travel_date),
            "user_query": f"{days} day {budget} trip to {destination} starting {travel_date}"
        })

        st.session_state.trip_plan = result.raw

# ---------- DISPLAY ----------
if st.session_state.trip_plan:

    try:
        plan = json.loads(st.session_state.trip_plan)
    except:
        st.error("Invalid JSON output")
        st.stop()

    st.success(f"✅ Trip Ready for {destination}")
    st.caption(f"📅 Travel Date: {travel_date} | 👥 {travelers} Travelers")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🌍 Overview", "💰 Budget", "🏨 Hotels", "🚗 Transport", "🗓 Itinerary"
    ])

    # ---------- OVERVIEW ----------
    with tab1:
        dest = plan.get("destination", {})
        weather = plan.get("weather", {})

        st.markdown("### 🌍 Destination")
        st.markdown(f"<div class='card'>{dest.get('overview','')}</div>", unsafe_allow_html=True)

        st.markdown("#### Highlights")
        for h in dest.get("highlights", []):
            st.write("•", h)

        st.markdown("#### 🌤 Weather")
        st.markdown(f"<div class='card'>{weather.get('summary','')}</div>", unsafe_allow_html=True)

        for tip in weather.get("travel_advice", []):
            st.write("•", tip)

    # ---------- BUDGET ----------
    with tab2:
        budget_data = plan.get("budget", {})

        st.markdown("### 💰 Budget")

        st.markdown(f"""
        <div class='card'>
        <b>Category:</b> {budget_data.get("category","")} <br><br>
        <b>Daily:</b> {budget_data.get("daily_estimate",{}).get("local","")} 
        (~{budget_data.get("daily_estimate",{}).get("usd","")})<br><br>
        <b>Total:</b> {budget_data.get("total_estimate",{}).get("local","")} 
        (~{budget_data.get("total_estimate",{}).get("usd","")})
        </div>
        """, unsafe_allow_html=True)

        st.subheader("Breakdown")
        breakdown = budget_data.get("breakdown", {})

        for k, v in breakdown.items():
            title = k.replace("_", " ").title()

            if isinstance(v, dict):
                desc = v.get("description", "")
                local = v.get("local", "")
                usd = v.get("usd", "")

                st.markdown(f"""
                <div class='card'>
                <b>{title}</b><br><br>
                📝 {desc}<br>
                💰 {local} <br>
                💵 {usd}
                </div>
                """, unsafe_allow_html=True)

            else:
                st.markdown(f"""
                <div class='card'>
                <b>{title}</b><br><br>
                {v}
                </div>
                """, unsafe_allow_html=True)

    # ---------- HOTELS ----------
    with tab3:
        hotels = plan.get("hotels", {})

        st.markdown("### 🏨 Hotels")

        for category, items in hotels.items():
            st.subheader(category.capitalize())

            for h in items:
                name = h.get("name", "Hotel not available")
                location = h.get("location_advantage", "Good location")
                price = h.get("price_range", "Price not available")

                st.markdown(f"""
                <div class='card'>
                <b>{name}</b><br>
                📍 {location}<br>
                💰 {price}
                </div>
                """, unsafe_allow_html=True)

    # ---------- TRANSPORT ----------
    with tab4:
        transport = plan.get("transport", {})

        st.markdown("### 🚗 Transport & Flights")

        if isinstance(transport, list):
            local_transport = transport
        else:
            local_transport = transport.get("local_transport", [])

        if not local_transport:
            st.info("No transport data available")

        for t in local_transport:
            efficiency = t.get("efficiency", "Moderate")

            st.markdown(f"""
            <div class='card'>
            <b>{t.get("mode","Transport")}</b><br>
            🚀 Efficiency: {efficiency}<br>
            {t.get("best_use_case","")}
            </div>
            """, unsafe_allow_html=True)

    # ---------- ITINERARY ----------
    with tab5:
        itinerary = plan.get("itinerary", [])

        st.markdown("### 🗓 Day-wise Itinerary")

        for day in itinerary:
            with st.expander(f"Day {day.get('day')}"):
                st.write("🌅 Morning:", day.get("morning"))
                st.write("🌞 Afternoon:", day.get("afternoon"))
                st.write("🌙 Evening:", day.get("evening"))

    # ---------- CURRENCY ----------
    st.markdown("---")
    st.subheader("💱 Currency Converter")

    col1, col2, col3 = st.columns(3)

    amount = col1.number_input("Amount", value=1000.0)
    from_curr = col2.selectbox("From", ["INR", "USD", "JPY", "EUR"])
    to_curr = col3.selectbox("To", ["INR", "USD", "JPY", "EUR"])

    if st.button("Convert"):
        try:
            result = convert_currency.run(
                amount=amount,
                from_curr=from_curr,
                to_curr=to_curr
            )
            st.success(f"{amount} {from_curr} = {result:.2f} {to_curr}")
        except Exception as e:
            st.error(f"Conversion failed: {str(e)}")

else:
    st.info("👈 Enter details to generate trip")

st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    text-align: center;
    color: gray;
    font-size: 14px;
    padding: 10px 0;
    background-color: transparent;
}
</style>

<div class="footer">
© 2026 ✈️ VoyageAI • Made by <b>Kaustav Roy Chowdhury</b>
</div>
""", unsafe_allow_html=True)