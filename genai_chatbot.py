from google import genai   # To install library : python -m pip install google-genai

# Replace the placeholder with your actual API key.
# Never share your API key publicly or upload it to GitHub.
key = "YOUR_GEMINI_API_KEY"   # Paste your Gemini API key here

client = genai.Client(api_key=key)   # The client uses the API key to authenticate requests to Google's API.

chat = client.chats.create(
    model="gemini-3.8-flash"
)


def completion(user_question):   # It accepts the user's question as an input parameter.
    try:
        response = chat.send_message(user_question)   # Send the user's question to Gemini.
        print(f"LUMORA: {response.text}")

    except Exception as e:
        print(f"LUMORA: Something went wrong: {e}")   # Display the error message instead of crashing immediately.


if __name__ == "__main__":
    print("LUMORA: Hi! I am LUMORA. How may I help you?")
    print("Type 'exit' to quit.\n")

    while True:
        user_question = input("You: ")

        if user_question.lower() in ["exit", "quit", "bye"]:   # Convert the input to lowercase and check for exit commands.
            print("LUMORA: Goodbye!")
            break

        completion(user_question)   # If the user did not request to exit, send the question to Gemini.
