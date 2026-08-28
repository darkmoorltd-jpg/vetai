
import tempfile
import os

def text_to_speech(text, language="en-GB"):
    """Convert text to speech using gTTS."""
    try:
        from gtts import gTTS
        gtts_lang = {"en-GB": "en", "ha": "ha", "yo": "yo", "ig": "ig"}
        code = gtts_lang.get(language, "en")
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts = gTTS(text=text, lang=code)
        tts.save(tmp.name)
        with open(tmp.name, "rb") as f:
            audio_bytes = f.read()
        os.unlink(tmp.name)
        return audio_bytes, None
    except Exception as e:
        return None, str(e)
