import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# ====================
# Ustawienia
# ====================
st.set_page_config(page_title="Zagadki i Obraz", layout="wide")
st.title("🧩 Misja - odkryj życzenia ślubne")

st.markdown("""
    <style>
        .stMainBlockContainer {
            padding-top: 8px !important;
        }
        .stAppHeader {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# ====================
# Funkcje pomocnicze
# ====================
def load_image_parts():
    parts = []
    for i in range(1, 5):
        parts.append(Image.open(f"parts/part{i}.png"))
    return parts

def pil_to_base64(img):
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()
    return f"data:image/png;base64,{img_str}"

def show_image_grid_html(unlocked):
    html = '<div style="display: flex; flex-wrap: wrap; width: 700px; margin: auto;">'
    for i in range(4):
        if unlocked[i]:
            img_data = pil_to_base64(image_parts[i])
        else:
            with open(f"locked{i}.png", "rb") as f:
                img_data = f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"
        html += f'<img src="{img_data}" style="width: 350px; height: 210px; margin: 0; padding: 0;" />'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

# ====================
# Główna logika
# ====================
image_parts = load_image_parts()

if "unlocked" not in st.session_state:
    st.session_state.unlocked = [False] * 4

riddles = [
    {
        "question": """
            <div style="
                border-left: 4px solid #3f51b5;
                background-color: #e8eaf6;
                padding: 16px;
                border-radius: 8px;
                margin-bottom: 8px;
                font-size: 18px;
                line-height: 1.6;
            ">
                🧩 <strong>Wiemy, że jesteście miłośnikami zagadek — dlatego życzenia nie przyjdą tak po prostu.</strong><br>
                Będziecie musieli na nie zapracować. W duecie, obowiązkowo, bo tylko razem dacie radę.<br>
                Oczywiście my, postaraliśmy się utrudnić Wam sprawę możliwie najbardziej 
                (żeby nie było zbyt dobrej atmosfery).<br>
                Ale nie martwcie się — trzymajcie się siebie i logiki, a wszystko pójdzie gładko.<br>
                Zawsze rozwiązywanie łamigłówek przychodziło Wam z łatwością, więc i tym razem liczymy na Wasze bystre umysły.<br>
                A tak przy okazji, bardzo lubimy ukrywać cyfry w tekście. 
                Może byście zrobili coś z tym faktem?
            </div>
            """,
        "answer": "13.01.2023",
        "placeholder": "",
        "img": None
    },
    {
        "question": """
            <div style="
                border-left: 4px solid #e91e63;
                background-color: #fff0f6;
                padding: 16px;
                margin-bottom: 6px;
                border-radius: 8px;
                font-size: 18px;
                line-height: 1.6;
            ">
                💌 <strong>Miłość to labirynt…</strong><br>
                Pełen zakrętów, niespodzianek i nieoczekiwanych ścieżek.<br>
                Czasem prowadzi przez śmiech, czasem przez ciszę — ale gdy idziecie razem, zawsze odnajdziecie wyjście.<br>
                Ten labirynt to doskonała okazja, by sprawdzić, jak dobrze odnajdujecie się w gąszczu decyzji, nieoczywistych dróg i zaskakujących rozwiązań.<br>
                Bo przecież w duecie nawet najbardziej kręta trasa staje się przygodą.
            </div>
            """,
        "answer": "152",
        "placeholder": "kod 3-cyfrowy",
        "img": Image.open("images/maze.png")
    },
    {
        "question": """
        <div style="
            border-left: 4px solid #009688;
            background-color: #e0f2f1;
            padding: 16px;
            border-radius: 8px;
            font-size: 18px;
            line-height: 1.6;
            margin-bottom: 12px;
        ">
            <strong>Wspólna podróż właśnie się zaczęła…</strong><br>
            Nie potrzebujecie mapy, by wiedzieć, dokąd iść — wystarczy, że trzymacie się za ręce.<br>
            Bo w miłości — jak w podróży — nie chodzi o to, by zawsze znać trasę,<br>
            ale by iść razem, krok po kroku, z uśmiechem, cierpliwością i otwartym sercem.
        </div>

        <div style="
            background-color: #fff3e0;
            padding: 14px;
            border-radius: 8px;
            font-size: 16px;
            margin-bottom: 8px;
            line-height: 1.6;
            border-left: 4px solid #fb8c00;
        ">
            <strong>A teraz czas na pierwszy wspólny krok —</strong>
            Wsłuchajcie się w kierunki, które poprowadzą Was dalej:<br>
                <strong style="font-size: 30px;">NN &nbsp;&nbsp; ESS &nbsp;&nbsp; ENWNE</strong>
            </div>
        </div>
        """,
        "answer": "175",
        "placeholder": "kod 3-cyfrowy",
        "img": None
    },
    {
        "question": """
            <div style="
                border-left: 4px solid #795548;
                background-color: #fbe9e7;
                padding: 16px;
                border-radius: 8px;
                font-size: 18px;
                margin-bottom: 8px;
                line-height: 1.7;
                color: #4e342e;
            ">
                📖 <strong>Najpiękniejsze historie nie zawsze są napisane wprost…</strong><br>
                Miłość też bywa subtelna — ukrywa się w drobnych gestach, spojrzeniach, chwilach ciszy.<br>
                Jak dobra książka, której sens odkrywamy dopiero wtedy,<br>
                gdy spojrzymy głębiej… <span style="white-space: nowrap;">albo z innej perspektywy</span>.
            </div>
        """,
        "answer": "17313",
        "placeholder": "kod 5-cyfrowy",
        "img": Image.open("images/bookshelf.png")
    }
]

# ====================
# Zakładki główne
# ====================
main_tabs = st.tabs(["🖼️ Obraz", "🔐 Zagadki"])

# ====================
# Zakładka z obrazem
# ====================
with main_tabs[0]:
    st.subheader("Ciekawe co tu jest ukryte?")
    show_image_grid_html(st.session_state.unlocked)
    st.markdown("""<p align="center" style="font-size: 20px; margin-top: 10px;"><strong>Dzwońcie do Werki gdy potrzeba pomocy, <br> Mati raczej nie odbierze czy to dzień czy w nocy.</strong></p>
""", unsafe_allow_html=True)

# ====================
# Zakładka z zagadkami
# ====================
with main_tabs[1]:
    st.subheader("UWAGA! Zagadki tylko dla ekspertów:")

    riddle_tabs = st.tabs([f"Zagadka {i+1}" for i in range(4)])

    for i, tab in enumerate(riddle_tabs):
        with tab:
            riddle = riddles[i]
            if i == 0 or st.session_state.unlocked[i - 1]:
                if not st.session_state.unlocked[i]:
                    st.markdown(f"{riddle['question']}", unsafe_allow_html=True)

                    if riddle["img"]:
                        img_data = pil_to_base64(riddle["img"])
                        if (i!=3):
                            st.markdown(f"""
                                <div style="display: flex; justify-content: center;">
                                    <img src='{img_data}' 
                                        style="max-width: 500px; width: 100%; height: auto; border-radius: 8px; padding-top: 4px; padding-bottom: 4px;" />
                                </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.markdown(f"""
                                <div style="display: flex; justify-content: center;">
                                    <img src='{img_data}' 
                                        style="max-width: 350px; width: 100%; height: auto; border-radius: 8px; padding-top: 4px; padding-bottom: 4px;" />
                                </div>
                            """, unsafe_allow_html=True)

                    answer = st.text_input(f"Wpisz kod:", key=f"answer_{i}", placeholder=riddle["placeholder"])
                    if st.button(f"Sprawdź kod", key=f"check_{i}"):
                        if answer.strip().lower() == riddle["answer"].lower():
                            st.session_state.unlocked[i] = True
                            st.rerun()
                            st.success("✅ Poprawna odpowiedź! Część odsłonięta.")
                        else:
                            if i==0:
                                if answer.strip().lower() == "1301":
                                    st.error("❌ Hmm, czy data nie ma aby innego formatu")
                                elif answer.strip().lower() == "13.01":
                                    st.error("❌ Hmm, a nie brakuje roku")
                                else:
                                    st.error("❌ Niepoprawna odpowiedź.")
                            else:
                                st.error("❌ Niepoprawna odpowiedź.")
                else:
                    st.success("✅ Chyba mamy do czynienia z zawodowcami.")
            else:
                st.info("🔒 Najpierw rozwiąż poprzednią zagadkę, aby odblokować tę zakładkę.")