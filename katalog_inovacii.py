import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(page_title="Katalóg výsledkov experimentálneho vzdelávania a inovácií", page_icon=":spiral_note_pad:", layout="wide")

with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Search
with stylable_container(
    key="filter",
    css_styles="""
     a, html, p, h1, h2, h3 {
        font-family: "Source Sans Pro", "Arial", sans-serif;
     }

     button {
        font-family: "Source Sans Pro", "Arial", sans-serif;
        background-color: #126dff;
        border: 2px solid transparent;
        border-radius: 5px;
     }
    
     div[data-baseweb="select"] {
          border: 2px solid #0b0c0c;
          border-radius: 0;
          background-color: transparent;        
     }

     /* Vyhladavanie */
     div[data-baseweb="input"] {
          border: 2px solid #0b0c0c;
          border-radius: 0;             
     }
     
     .st-dl {
        outline: 3px solid #ffdf0f; /*yellow*/
        outline-offset: 0;
        box-shadow: inset 0 0 0 2px;
        border-radius: 0;
        border-bottom-color: transparent;
        border-top-color: transparent;
        border-right-color: transparent;
        border-left-color: transparent;
    }
    
    div[data-baseweb="select"] > div {
        border-bottom-right-radius: 0rem;
        border-bottom-left-radius: 0rem;
        border-top-right-radius: 0rem;
        border-top-left-radius: 0rem;
        background-color: transparent;        
     }

     div[data-baseweb="notification"] {
          border-radius: 0;
          color: black;
          background-color: #dee0e2;
    }
    
    p {
        font-size: 1rem !important;
    }
    
     """):

    c1, c2, c3 = st.columns(3)
    with c1:
        query = st.text_input('Vyhľadávanie', '', key=1, placeholder="Zadajte hľadaný výraz",
                              label_visibility='collapsed')

    # Selectbox
    druhy_inovacii = ['-', 'Výchovno-vzdelávacie programy',
                      'Formy, metódy a prostriedky výchovy a vzdelávania',
                      'Formy a spôsoby hodnotenia detí a žiakov', 'Koncepcie inkluzívneho vzdelávania',
                      'Formy riadenia škôl a školských zariadení', 'Preventívne a rozvojové programy']

    stupne_vzdelania = ['-', 'Predprimárne', 'Základné vzdelanie', 'Stredné vzdelanie', 'Vyššie odborné vzdelanie']

    col1, col2, col3 = st.columns(3)

    with col1:
        s_zameranie = st.selectbox('Obsahové zameranie inovácie', ['-'], index=0)
    with col2:
        s_druh = st.selectbox('Druh inovácie', druhy_inovacii, index=0)
    with col3:
        s_skupina = st.selectbox('Stupeň vzdelania', stupne_vzdelania, index=0)
        if 'Základné vzdelanie' in s_skupina:
            s_cyklus = st.multiselect('Cyklus', ['1.','2.','3.'], default=['1.','2.','3.'], placeholder='Vyber možnosť')

# Results
url = "https://www.minedu.sk/ziadost-ozapis-inovacie-vo-vychove-avzdelavani-do-katalogu-vysledkov-experimentalneho-overovania-ainovacii/"
st.info('**Katalóg je aktuálne prázdny.**')
# st.info('**[Nová žiadosť](%s)**' % url)

# H1: Názov inovácie + (názov subjektu)
# H2: Popis inovácie
# H2: Obsahové zameranie inovácie
# H2: Spôsob použitia inovácie
# H2: Vymedzenie skupiny žiakov
# H2: Aplikačná prax(ak je)



