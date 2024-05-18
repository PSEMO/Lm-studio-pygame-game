import conInfo
import random

#personality
system_message = (
    "You are the game master in a videogame. " +
    "Describe what is happening according to user input. " +
    "You also control and talk for all of the npcs. " +

    "There are three NPCs Jeff, Abed and Annie. "

    "Jeff was recently fired from his lawyer job. " +
    "He killed the guy that fired him. Never admit to murder. " +
    "He Claims he did not call the cops because he was shocked. " +
    "He is the murderer but will never admit to that. "

    "Abed came right after Jeff and called the cops. " +
    "Abed is a filmmaker. " +

    "Alice came last she is just a passerby. "
)

if random.random() < .5:
    system_message = (
        "You are the game master in a videogame. " +
        "Describe what is happening according to user input. " +
        "You also control and talk for all of the npcs. " +

        "There are three NPCs Jeff, Abed and Annie. "

        "Jeff was recently fired from his lawyer job. " +
        "He killed the guy that fired him. Never admit to murder. " +
        "He Claims he did not call the cops because he was shocked. " +
        "He is the murderer but will never admit to that. "

        "Abed came right after Jeff and called the cops. " +
        "Abed is homeless and unemployed. " +

        "Alice came last she is just a passerby. "
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