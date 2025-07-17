import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
from google.genai import types
import sys

sys_input = sys.argv[1]
messages = [
    types.Content(role="user", parts=[types.Part(text=sys_input)]),
]
client = genai.Client(api_key=api_key)



def main():
    print("Hello from ai-agent!")
    if len(sys_input) <= 1:
        sys.exit(1)
    else:
        respones = client.models.generate_content(model = "gemini-2.0-flash-001", 
                                              contents = messages)
        print(respones.text)
        print(f"Prompt tokens: {respones.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {respones.usage_metadata.candidates_token_count}")
    
if __name__ == "__main__":
    main()
