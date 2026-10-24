# To install Openai library : python -m pip install openai
from openai import OpenAI, APIError, RateLimitError 

# Replace the placeholder with your actual API key.
# Never share your API key publicly or upload it to GitHub.
key = "YOUR_OPENAI_API_KEY"   # Paste your Openai API key here

messages = []   # Create an empty list to store the conversation history.
                # It will contain the user's messages and LUMORA's replies.

client = OpenAI(
    api_key=key,    # Create a connection to the OpenAI API using your API key. 
)


def completion(user_input):   # Define a function that processes the user's question.
    messages.append({         # Add the user's question to the conversation history.
        "role": "user",
        "content": user_input
    })

    try:
        # Send the conversation history to the OpenAI API.
        # The model generates a reply based on the messages provided.
        chat_completion = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )

        reply = chat_completion.choices[0].message.content   # Extract the text of the assistant's reply from the API response.

        messages.append({           # Save LUMORA's reply so it can be included in later conversations.
            "role": "assistant",
            "content": reply
        })

        print(f"LUMORA: {reply}")

    # Handle errors related to API rate limits or exhausted quota.
    except RateLimitError:
        print("LUMORA: API quota or rate limit error.")
        print("Please check your API billing and usage limits.")

    # Handle other errors reported by the OpenAI API.
    except APIError as e:
        print(f"LUMORA: An API error occurred: {e}")


if __name__ == "__main__":
    print(f"LUMORA: Hi I am LUMORA, How may I help you\n")
    while True:
        user_question = input()
        print(f"User: {user_question}")
        completion(user_question)        # Send the question to the completion function.
