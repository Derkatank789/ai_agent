import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys





def main():
    load_dotenv()

    sys_input = []
    sys_verbose = "--verbose" in sys.argv
    for mes in sys.argv[1:]:
        if not mes.startswith("--"):
            sys_input.append(mes)
    
   
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    

    

    if len(sys_input) <= 0:
        print('Usage: python main.py "your prompt here" [--verbose]')
        sys.exit(1)
    else:
        user_input = " ".join(sys_input)
        messages = [types.Content(role="user", parts=[types.Part(text = user_input)]),]
        respones = client.models.generate_content(model = "gemini-2.0-flash-001", 
                                              contents = messages)
        print("Response:")
        print(respones.text)
        if sys_verbose:
            print(f"User prompt: {sys_input}")
            print(f"Prompt tokens: {respones.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {respones.usage_metadata.candidates_token_count}")
    
if __name__ == "__main__":
    main()
