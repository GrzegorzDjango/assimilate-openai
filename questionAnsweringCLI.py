#!/user/bin/env python


import openai
import os
import click

def submit_question(text):
    print(os.getenv("OPENAI_API_KEY"))
    key = "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"
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = text
    result = openai.Completion.create(
        prompt=prompt,
        temperature=0,
        max_tokens=300,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=0,
        model="text-davinci-002"
    )["choices"][0]["text"].strip("\n")
    return result

@click.command()
@click.argument('text')
def main(text):
    print(submit_question(text))

if __name__ == "__main__":
    main()