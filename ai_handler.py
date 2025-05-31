def ask_jarvis(message: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Sən Jarvis adında ağıllı, nəzakətli və məntiqli bir virtual dostsan. "
                        "İstifadəçiyə yalnız Azərbaycan dilində cavab ver. Cavabların əsasən ciddi və faydalı olmalıdır, "
                        "lakin əgər söhbət mövzusu uyğundursa, yüngül, səmimi və ağıllı zarafatlar da edə bilərsən. "
                        "İnsanlara hörmətli davran və köməkçi olmağa çalış."
                    )
                },
                {"role": "user", "content": message}
            ],
            max_tokens=1000,
            temperature=0.85
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception:
        return "Bağışlayın, sistemdə xəta baş verdi. Bir az sonra yenidən cəhd edin."
