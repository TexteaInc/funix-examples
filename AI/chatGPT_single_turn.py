import os
import openai
openai.api_key = os.environ.get("OPENAI_KEY")

import typing

import funix

advertisement = """Tips:
* Enter your message, press Run, and wait for the response on the right. 
* Click "Source code" to see how simple it is to build AI/data apps in Funix.
* If you like it, give Funix a star on Github! Thanks! https://github.com/TexteaInc/funix
    """

@funix.funix(
    title="""ChatGPT single-turn, powered by [Funix](http://funix.io)""",
    description=advertisement,
    show_source=True
)
def ChatGPT_single_turn(prompt: str="Who is Cauchy?") -> str:
    completion = openai.ChatCompletion.create(
        messages=[{"role": "user", "content": prompt}],
        model="gpt-3.5-turbo"
    )
    return f'ChatGPT says:  {completion["choices"][0]["message"]["content"]}'