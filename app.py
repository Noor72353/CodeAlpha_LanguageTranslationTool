import requests
import streamlit as st

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered",
)

LANGUAGES = {
    "English": "en",
    "Urdu": "ur",
    "Arabic": "ar",
    "Chinese (Simplified)": "zh-CN",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Portuguese": "pt",
    "Russian": "ru",
    "Spanish": "es",
    "Turkish": "tr",
}

API_URL = "https://api.mymemory.translated.net/get"

st.title("🌍 Language Translation Tool")
st.write("Translate text between different languages.")
st.info("Choose your languages, enter text, and click Translate.")

text_to_translate = st.text_area(
    "Enter text to translate",
    placeholder="Type or paste your text here...",
    height=150,
)

col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "Translate from",
        list(LANGUAGES.keys()),
    )

with col2:
    target_language = st.selectbox(
        "Translate to",
        list(LANGUAGES.keys()),
        index=1,
    )

if st.button("Translate Text", type="primary", use_container_width=True):
    if not text_to_translate.strip():
        st.warning("Please enter some text to translate.")

    elif source_language == target_language:
        st.warning("Please select two different languages.")

    elif len(text_to_translate.strip().encode("utf-8")) > 500:
        st.warning(
            "Please shorten your text to 500 bytes or less "
            "for this translation service."
        )

    else:
        try:
            params = {
                "q": text_to_translate.strip(),
                "langpair": (
                    f"{LANGUAGES[source_language]}|"
                    f"{LANGUAGES[target_language]}"
                ),
            }

            with st.spinner("Translating your text..."):
                response = requests.get(
                    API_URL,
                    params=params,
                    timeout=20,
                )
                response.raise_for_status()
                data = response.json()

            if data.get("responseStatus") == 200:
                translated_text = data["responseData"]["translatedText"]

                st.session_state["translated_text"] = translated_text
                st.session_state["source_language"] = source_language
                st.session_state["target_language"] = target_language

                st.success("Translation completed successfully!")

            else:
                st.error(
                    "The translation service could not translate this text. "
                    "Try again later or choose another language pair."
                )

        except requests.Timeout:
            st.error("The request timed out. Please try again later.")

        except requests.RequestException:
            st.error(
                "Could not connect to the translation service. "
                "Check your internet connection and try again."
            )

        except (KeyError, ValueError):
            st.error(
                "The translation service returned an unexpected response."
            )

if "translated_text" in st.session_state:
    st.divider()
    st.subheader("Translated Text")

    st.caption(
        f"{st.session_state['source_language']} → "
        f"{st.session_state['target_language']}"
    )

    st.text_area(
        "Translation result",
        value=st.session_state["translated_text"],
        height=150,
        disabled=True,
    )

    st.code(st.session_state["translated_text"], language=None)

    st.caption("To copy the translation, select the text above and press Ctrl+C.")

    if st.button("Clear Translation"):
        for key in (
            "translated_text",
            "source_language",
            "target_language",
        ):
            st.session_state.pop(key, None)

        st.rerun()

st.divider()
st.caption("CodeAlpha AI Internship Project | Language Translation Tool")
