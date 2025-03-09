import openai
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from crud import update_translation_task

import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def perform_translation(task: int, text: str, languages: list, db: Session):
    translations = {}
    for lang in languages:
        try:
            response.openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": f"you are a helpful assistant that translates test into {lang}."},
                    {"role":"user","content":text}
                ],
                max_tokens=1000
            )
        except Exception as e:
            print(f"Error translation to {lang}:{e}")
            translations[lang] = f"Error:{e}"
        except Exception as e:
            print(f"Unexpected errro:{e}")
            translations[lang] = f"Unexpected error: {e}"
            
            update_translation_task(db,task_id,translations)