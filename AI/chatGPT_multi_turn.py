import os, typing
import openai 
openai.api_key = os.environ.get("OPENAI_KEY")

advertisement = """Tips: 
* Enter your message, press Run, and wait for the response on the right. Your chat history will be fully displayed. 
* If your chat history is too long, it will be truncated to fit the 4096-token limit.
* Click "Source code" to see how simple it is to build AI/data apps in Funix.
* If you like it, give Funix a star on Github! Thanks! https://github.com/TexteaInc/funix
    """

token_limit = 3500

messages  = []  # list of dicts, dict keys: role, content, system 

def print_messages_html(messages):
    printout = ""
    for message in messages:
        line = message["content"].strip().replace("\n", " ")
        if message["role"] == "user":
            align, left, who = "left", "0%", "You"
        elif message["role"] == "assistant":
            align, left, who = "right", "30%", "ChatGPT"
        printout += f'<div style="position: relative; left: {left}; width: 70%"><b>{who}</b>: {line}</div>'
    return printout

def print_messages_markdown(messages):
    printout = ""
    for message in messages:
        if message["role"] == "user":
            mark, who =  "**", "You"
        elif message["role"] == "assistant":
            mark, who =  "_", "ChatGPT"
        line = message["content"].strip().replace("\n", " ")
        printout += f'{mark}{name}: {line}{mark}\n'
        if message["role"] == "assistant":
            printout += "\n"
    return printout

# TODO: Dynamically truncate the message list to maximize the token length
def truncate_messages(messages: typing.List[str], token_limit: int):
    """Truncate the message list to fit the token limit."""
    tokens = 0
    for reverse_index in range(-1, -len(messages), -1):
        message = messages[reverse_index]
        tokens += len(message["content"].split())
        if tokens > token_limit:
            return messages[reverse_index: ]
    return messages

import funix
@funix.funix(
    title = """ChatGPT multi-turn powered by [Funix](http://funix.io)""",
    description = advertisement,
    argument_labels = {
        "current_message" : "Enter your message here",
    },
    show_source=True 
)
def ChatGPT_multi_turn(
    current_message: str, 
    # model = typing.Literal['gpt-3.5-turbo'],
    max_tokens: range(20, 100, 20)=80,
    )  -> funix.hint.HTML:
    global messages 
    messages.append({"role": "user", "content": current_message})
    completion = openai.ChatCompletion.create(
        messages=messages,
        model='gpt-3.5-turbo',
        max_tokens=max_tokens,
    )
    chatgpt_response = completion["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": chatgpt_response})
    messages = truncate_messages(messages, token_limit)

    # return print_messages_markdown(messages)
    return print_messages_html(messages)
