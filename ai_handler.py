import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")  # ya da birbaşa 'your-api-key'

def ask_jarvis(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # ya da "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "Sən zarafatcıl və mehriban Azərbaycan dilində danışan virtual dostsan."},
                {"role": "user", "content": user_input},
            ],
            max_tokens=500,
            temperature=0.8,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"OpenAI xətası: {e}")
        return "Cavab hazırlanarkən problem baş verdi."
