import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

import sys

def main():
    sys_input = sys.argv
    print("Hello from ai-agent!")
    if len(sys_input) <= 1:
        sys.exit(1)
    else:
        respones = client.models.generate_content(model = "gemini-2.0-flash-001", 
                                              contents = sys_input[1])
        print(respones.text)
        print(f"Prompt tokens: {respones.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {respones.usage_metadata.candidates_token_count}")
    
if __name__ == "__main__":
    main()
