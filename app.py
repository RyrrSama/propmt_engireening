import os
import datetime
import json
from llamaapi import LlamaAPI

# Initialize the SDK
llama = LlamaAPI(os.environ["LLAMA_API_TOKEN"])
# Build the Request
api_request_json = {
    "model": os.environ["MODEL_NAME"],
    "messages": [
        {
            "role": "user",
            "content": "Hi how are you ??",
        },
        {"role": "system", "content": "You are a trained OPENAI assistent"},
    ],
}

# Execute the Request
response = llama.run(api_request_json)
