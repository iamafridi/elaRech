import os
import base64
from dotenv import load_dotenv
from groq import Groq

# Load .env variables
load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Load image and encode
# image_path = "test1.png"
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# query = "Can you explain what's shown in this diagram and how it relates to photosynthesis?"
# Define query and client
def analysis_image_with_query(query, model, encoded_image):
    client = Groq(api_key=GROQ_API_KEY)
    # model = "meta-llama/llama-4-scout-17b-16e-instruct"

    # Prepare messages
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{encoded_image}"
                    }
                }
            ],
        }
    ]

    # Call model
    chat_completion = client.chat.completions.create(
        model=model,
        messages=messages
    )

    # Print response
    # print(chat_completion.choices[0].message.content)

    return chat_completion.choices[0].message.content
