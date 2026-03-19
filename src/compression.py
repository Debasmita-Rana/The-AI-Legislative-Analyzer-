import requests

API_KEY = "YOUR_SCALEDOWN_API_KEY_HERE"

def compress_text(text):
    try:
        url = "https://api.scaledown.ai/v1/compress"  # keep attempt

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "text": text
        }

        response = requests.post(url, json=data, headers=headers, timeout=5)

       
        result = response.json()

        if "compressed_text" in result:
            return result["compressed_text"]

    except:
        pass  

    
    sentences = text.split(".")
    return ". ".join(sentences[:5])