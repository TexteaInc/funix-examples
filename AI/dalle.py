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
    title="""a Dall-E demo, powered by [Funix](http://funix.io)""",
    description=advertisement,
    show_source=True
)
def dalle(Prompt: str) -> funix.hint.Image:
    response = openai.Image.create(prompt=Prompt)
    return response["data"][0]["url"]