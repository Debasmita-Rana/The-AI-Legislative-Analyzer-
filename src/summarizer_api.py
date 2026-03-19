import requests

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"

def summarize_text(text):
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

        data = {
            "contents": [{
                "parts": [{
                    "text": f"Summarize this policy in simple language:\n{text}"
                }]
            }]
        }

        response = requests.post(url, json=data, timeout=5)

        result = response.json()

        return result["candidates"][0]["content"]["parts"][0]["text"]

    except:
       
        return text[:300] + "..."