import os
from dotenv import load_dotenv

from app.config.model_config import LLM_MODEL_NAME

from openrouter import OpenRouter

load_dotenv()


def generate_answer(prompt: str) -> str:
    with OpenRouter(
        api_key=os.getenv("OPENROUTER_API_KEY"),
    ) as open_router:

        res = open_router.chat.send(
            model=LLM_MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            stream=False,
        )

        return res.choices[0].message.content
