'''
import conInfo

#personality
system_message = (
    "Your name is Bob. " +
    "You are a homeless and unemployed. " +
    "You saw the body on the floor and called the cops. " +
    "James was here before you. " +
    "James did not call the cops because he was shocked. " +
    "Alice came last she is just a passerby"
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