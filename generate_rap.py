import os
import csv
from datetime import datetime

from dotenv import load_dotenv
import openai


def generate_rap_song():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY not found in environment")
    client = openai.OpenAI(api_key=api_key)

    prompt = (
        "Write a creative and emotionally expressive rap song with at least two verses "
        "and either a chorus or a refrain. Format the output with section labels and clear line breaks."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.8,
        )
        lyrics = response.choices[0].message.content.strip()
    except Exception:
        # Fallback to text-davinci-003 if ChatCompletion fails
        response = client.completions.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=500,
            temperature=0.8,
        )
        lyrics = response.choices[0].text.strip()

    timestamp = datetime.now().isoformat()
    with open("rap_songs.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([timestamp, lyrics])

    print("Rap song generated and saved.")


if __name__ == "__main__":
    generate_rap_song()
