from openai import OpenAI
from app.core.config import settings
import openai

openai.api_key = settings.OPENAI_API_KEY

client = OpenAI()

def test_openAI():
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Write a haiku about recursion in programming."
            }
        ]
    )
    print(completion.choices[0].message)
    return completion.choices

def text_to_embeddings(text: str):

    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )

    # print(response.data[0].embedding)

    return response.data[0].embedding
