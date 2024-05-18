'''
import conInfo

#personality
system_message = (
    "My name is James. " +
    "I was recently fired from your job. " +
    "I saw the body on the floor and froze. " +
    "I did not call the cops because you were shocked. " +
    "Bob came right after me and called the cops. " +
    "Alice came last she is just a passerby. " +
    "I am a murderer. Never admit that you actually killed"
)

# Function to create a chat completion with a dynamic user prompt
def create_chat_completion(user_input):
    return conInfo.openai.ChatCompletion.create(
        model="local-model",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
    )

def ask(input):
    completion = create_chat_completion(input)
    return str(completion.choices[0].message.content)
    '''