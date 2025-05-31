import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def ask_jarvis(message: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # istəyirsənsə GPT-4-ə dəyişə bilərsən
            messages=[
                {"role": "system", "content": "Sən virtual dostsan və istifadəçiyə Azərbaycan dilində səmimi şəkildə cavab verirsən."},
                {"role": "user", "content": message}
            ],
            max_tokens=1000,
            temperature=0.8
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return "Bağışla, bir xəta baş verdi. Bir az sonra yenidən cəhd et."
