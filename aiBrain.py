with open("C:\\Users\\RITIK KISHOR YELANE\\OneDrive\\Desktop\\AI Assitance\\Project 4\\aiBrain.txt", "r") as f:
    API = f.read()
    f.close()

import openai
from dotenv import load_dotenv

openai.api_key = API
load_dotenv()
completion = openai.Completion()


def ReplyBrain(question, chat_log=None):
    FileLog = open("C:\\Users\\RITIK KISHOR YELANE\\OneDrive\\Desktop\\AI Assitance\\Project 4\\chatlog.txt", "r")
    chat_log_template = FileLog.read()
    FileLog.close()
    if chat_log == None:
        chat_log = chat_log_template
    prompt = f"{chat_log}You : {question}\nJarvis : "
    response = completion.create(
        model="text-davinci-003",
        prompt=prompt,
        # tempreture = 0.5,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + \
        f"\nYou : {question} \nJarvis : {answer}"
    FileLog = open("C:\\Users\\RITIK KISHOR YELANE\\OneDrive\\Desktop\\AI Assitance\\Project 4\\chatlog.txt", "w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer
