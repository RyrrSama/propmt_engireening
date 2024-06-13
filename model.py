# Default import
import os
from pathlib import Path

# OpenAI imports
from openai import OpenAI

# Local imports
import utils
import constants as CONSTANTS

# Get client object
CLIENT = OpenAI(api_key=os.environ["LLAMA_API_TOKEN"], base_url=os.environ["BASE_URL"])

# Get user prompt
USER_PROMPT = utils.read_prompt(Path(CONSTANTS.PROMPT_FILE).resolve())


def get_weather(location):
    return "1001"


def communicate(user_input=USER_PROMPT):
    """Communicate with model"""
    # Communicate with OpenAI
    MODEL_RESPONSE = CLIENT.chat.completions.create(
        model=os.environ["MODEL_NAME"],
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "Get weather for given location.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "Location name to get weather information e.g : India, delhi",
                            }
                        },
                        "required": ["location"],
                    },
                },
            }
        ],
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that can access external functions. PLease provide responses based on the information from these function calls.",
            },
            {"role": "user", "content": user_input},
        ],
        tool_choice="auto",
    )
    return MODEL_RESPONSE
