import streamlit as st
import requests

# Set page structure
st.set_page_config(page_title="ATP Tennis Prediction Engine", layout="centered")

st.title("🎾 ATP Tennis Prediction Engine")
st.write("Real-time data pipeline connected directly to the odds markets.")

# Hardcoding your API Key so the app loads instantly
API_KEY = "1069eccbb7b9bbabe99b4dfa886e5a39"

# Broad sport key targeting upcoming elite tennis lines
SPORT_KEY = "tennis_atp_wimbledon" 

url = f"https://api.the-odds-api.com/v4/sports/{SPORT_KEY}/odds/?apiKey={API_KEY}&regions=us&markets=h2h"

st.info("🔄 Querying active board data from The-Odds-API...")

try:
    response = requests.get(url)
    
    if response.status_code == 401:
        st.error("🔒 Unauthorized access. Please double check that the API key is completely correct.")
    elif response.status_code != 200:
        st.error(f"⚠️ Market server returned status code: {response.status_code}")
    else:
        data = response.json()
        
        if not data:
            st.warning("📅 No active tournament matches found on the board right now. Check back when lines open!")
        else:
            st.success(f"🔥 Successfully retrieved {len(data)} live match lines!")
            
            # Print out each match dynamically onto the website interface
            for match in data:
                home_player = match.get('home_team', 'Player 1')
                away_player = match.get('away_team', 'Player 2')
                
                with st.container():
                    st.markdown(f"### ⚔️ {home_player} vs {away_player}")
                    
                    if match.get('bookmakers'):
                        first_book = match['bookmakers'][0]
                        book_name = first_book['title']
                        outcomes = first_book['markets'][0]['outcomes']
                        
                        p1, p2 = outcomes[0]['name'], outcomes[1]['name']
                        odds1, odds2 = outcomes[0]['price'], outcomes[1]['price']
                        
                        st.write(f"**Market Source:** {book_name}")
                        st.write(f"📈 Decimal Odds ➡️ **{p1}**: `{odds1}` | **{p2}**: `{odds2}`")
                    else:
                        st.write("⏳ Match is scheduled, but betting lines haven't opened yet.")
                    
                    st.markdown("---")

except Exception as e:
    st.error(f"An unexpected connection error occurred: {e}")
