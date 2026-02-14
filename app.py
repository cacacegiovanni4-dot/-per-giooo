import streamlit as st
from datetime import datetime

# ==============================================================================
# 🐔 AREA CONFIGURAZIONE (MODIFICA QUI SOTTO) 🐔
# ==============================================================================

# 1. I VOSTRI NOMI
NOME_LEI = "Giorgia"
NOME_LUI = "Giovanni"

# 2. DATA FIDANZAMENTO
ANNO = 2024
MESE = 6    
GIORNO = 23

# 3. LE 5 DOMANDE DEL QUIZ
LISTA_DOMANDE = [
    {
        "domanda": "1. Cosa abbiamo mangiato alla nostra prima uscita?",
        "opzioni": ["Bistecca", "Pizza", "Sushi", "Pasta"],
        "corretta": "Sushi"
    },
    {
        "domanda": "2. Dove ci siamo dati il nostro primo vero bacio?",
        "opzioni": ["Panchine campo Italia", "Porto Sorrento", "Praiano", "Sotto casa tua"],
        "corretta": "Panchine campo Italia"
    },
    {
        "domanda": "3. Chi aveva torto nell'incidente",
        "opzioni": ["Giovanni", "Giorgia", "Nessuno", "Entrambi"],
        "corretta": "Giorgia"
    },
    {
        "domanda": "4. Quanto sei una bambina minuscola?",
        "opzioni": ["Tanto", "Tantissimissimissimissimo", "Tantissimissimo", "Tantissimo"],
        "corretta": "Tantissimissimissimissimo"
    },
    {
        "domanda": "5. Pensi anche tu che ci sposeremo?",
        "opzioni": ["Si", "Si", "Si", "Si"],
        "corretta": "Si"
    }
]

# 4. FOTO E CANZONE
LISTA_FOTO = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg"] 
LINK_CANZONE = "https://www.youtube.com/watch?v=34oWyWjqp88" 

# 5. TESTI
TITOLO_LETTERA = "Amore mio..."
TESTO_LETTERA = """
Zao crocca ti volevo solo dire che ti amo tantissimo e che sembra passato tanto ma è 
ancora decisamente poco perchè io non vedo l'ora di sposarti ciao ti amo sei una bambina.
"""
MESSAGGIO_FINALE_SORPRESA = "BACINI INFINITIIII TUTTI PER TEEE❤️"

# ==============================================================================
# FINE CONFIGURAZIONE
# ==============================================================================

st.set_page_config(page_title=f"Per {NOME_LEI} ❤️", page_icon="🥰")

# --- CSS MIGLIORATO PER MOBILE ---
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        .stApp { 
            background-color: #ffeef2; 
        }

        h1, h2, h3, h4, h5, h6, p, span, div, label, .stMarkdown {
            color: #590d22 !important; 
        }

        h1 {
            color: #d60045 !important;
            font-weight: 800 !important;
            text-shadow: 1px 1px 0px rgba(255,255,255,0.5);
        }

        .stRadio div[role='radiogroup'] > label {
            background-color: rgba(255,255,255,0.8);
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 5px;
            border: 1px solid #ff99ac;
            color: #590d22 !important;
        }

        .stButton button {
            background-color: #d60045 !important;
            color: white !important;
            border-radius: 20px;
            font-weight: bold;
            font-size: 18px;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown(f"<h1 style='text-align: center;'>❤️ ZAO PATATONA ❤️</h1>", unsafe_allow_html=True)
st.markdown("---")

# --- TIMER ---
st.markdown("<h3 style='text-align: center;'>⏳ Stiamo insieme da...</h3>", unsafe_allow_html=True)
start_date = datetime(ANNO, MESE, GIORNO)
diff = datetime.now() - start_date

col1, col2, col3 = st.columns(3)
col1.metric("Giorni", diff.days)
col2.metric("Ore", int(diff.seconds // 3600))
col3.metric("Minuti", int((diff.seconds // 60) % 60))

st.markdown("---")

# --- LETTERA ---
with st.expander(f"💌 Leggi la lettera per te", expanded=False):
    st.write(TESTO_LETTERA)

st.markdown("---")

# --- FOTO ---
st.markdown("<h3 style='text-align: center;'>📸 le nostre fotooo</h3>", unsafe_allow_html=True)
if LISTA_FOTO:
    tabs = st.tabs([f"Foto {i+1}" for i in range(len(LISTA_FOTO))])
    for i, tab in enumerate(tabs):
        tab.image(LISTA_FOTO[i], use_container_width=True) 

st.markdown("---")

# --- MUSICA (FIX PER MOBILE) ---
st.markdown("<h3 style='text-align: center;'>🎶 Play Me</h3>", unsafe_allow_html=True)

# Logica per estrarre l'ID di YouTube in modo sicuro
try:
    if "v=" in LINK_CANZONE:
        video_id = LINK_CANZONE.split("v=")[1].split("&")[0]
    elif "youtu.be" in LINK_CANZONE:
        video_id = LINK_CANZONE.split("/")[-1]
    else:
        video_id = None
        
    if video_id:
        # Usa HTML Iframe diretto invece di st.video (Carica meglio su mobile)
        st.markdown(f"""
            <div style="display: flex; justify-content: center;">
                <iframe width="100%" height="250" src="https://www.youtube.com/embed/{video_id}" 
                title="YouTube video player" frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                style="border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);"
                allowfullscreen></iframe>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Link canzone non valido")
except:
    st.markdown(f"[Clicca qui per ascoltarla su YouTube]({LINK_CANZONE})")

st.markdown("---")

# --- QUIZ ---
st.markdown("<h2 style='text-align: center; color: #d63384;'>❓ Quiz dell'Amore ❓</h2>", unsafe_allow_html=True)
st.caption("Rispondi correttamente a TUTTE le 5 domande per sbloccare il regalo!")

if 'quiz_superato' not in st.session_state:
    st.session_state.quiz_superato = False
if 'errore_quiz' not in st.session_state:
    st.session_state.errore_quiz = False

with st.form("quiz_form"):
    risposte_utente = []
    for i, q in enumerate(LISTA_DOMANDE):
        st.markdown(f"**{q['domanda']}**")
        risposta = st.radio(f"Domanda {i+1}", q['opzioni'], key=f"q_{i}", label_visibility="collapsed", index=None)
        risposte_utente.append(risposta)
        st.write("") 
    
    submit_btn = st.form_submit_button("💌 VERIFICA RISPOSTE")

    if submit_btn:
        punteggio = 0
        for i, r_utente in enumerate(risposte_utente):
            if r_utente == LISTA_DOMANDE[i]['corretta']:
                punteggio += 1
        
        if punteggio == 5:
            st.session_state.quiz_superato = True
            st.session_state.errore_quiz = False
        else:
            st.session_state.quiz_superato = False
            st.session_state.errore_quiz = True

if st.session_state.errore_quiz:
    st.error(f"mmmmm! Qualche risposta è sbagliata! Riprova patata 😜")

if st.session_state.quiz_superato:
    st.markdown("---")
    st.balloons()
    st.markdown(f"<h1 style='text-align: center; color: green !important;'>BRAVISSIMA! 🎉</h1>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif", use_container_width=True)
    
    st.success("🎁 HAI SBLOCCATO IL TUO REGALO:")
    st.markdown(f"<div style='text-align: center; border: 3px solid #d60045; padding: 20px; border-radius: 15px; background-color: white; color: #d60045;'><h2>{MESSAGGIO_FINALE_SORPRESA}</h2></div>", unsafe_allow_html=True)