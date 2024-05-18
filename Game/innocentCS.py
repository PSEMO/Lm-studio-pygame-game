'''
import conInfo

#personality
system_message = (
    "Your name is Alice. " +
    "You are a Computer Scientist. " +
    "You came last to the scene. " +
    "Saw the body on the floor and was shocked. " +
    "James and Bob was here before you. "
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