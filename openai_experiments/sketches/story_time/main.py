import re

from elevenlabs import generate, play, set_api_key, voices
import openai

from openai_experiments import config

from openai_experiments.sketches.story_time import example

set_api_key(config.xi_labs_api_key)
openai.api_key = config.api_key

prompt_example = "This story is set on a space station run by SpaceX and Oscar and Angela have to uncover a villanous plot to destroy the station by sabotage."

while 1:
    #prompt = input("What would you like your story to be about? ")
    prompt = prompt_example

    print('Writing your story...')
    completion = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[
            dict(
                role="system",
                content=f"You are a children's story writer. You write stories of 1000-1500 words. You always write your stories in chapters of 70-140 words each and you start each chapter with [CHAPTER] and the title of the chapter. After each chapter describe an illustartion that would best illustrate the chapter by writing [ILLUSTRATION: <description of illustration>], describe what the illustration should contain in a form suitable for passing to the AI image generation tool DALLE. Do not rely on the names of people or objects in the story, instead describe the characters and what is to be drawn. Use less than 40 words."
            ),
            dict(
                role="assistant",
                content=f"There are two children, a boy called Oscar and a girl called Angela. They go on an adventure where they solve a dangerous and exciting mystery. The story should be about: \n\n{prompt}"
            )
        ],
        stream=True
    )

    if False:
        text = ''
        for event in completion:
            fragment = event.choices[0].delta.get('content')
            print(fragment or '', end='')
            text += fragment or ''
        print()

    else:
        text = example.story

    chapters = re.split(r'\[CHAPTER (.*?)\]', text.strip())[1:]
    chapters = [chapters[i:i + 2] for i in range(0, len(chapters), 2)]
    for chapter in chapters:
        illustration = re.split(r'\[ILLUSTRATION: (.*?)\]', chapter[1].strip())[1]
        print(illustration)

    for x, i in enumerate(chapters):
        print(x, repr(i))

    break

    print('Reading it out...')
    audio = generate(
        text=text,
        voice="Oren Goldschmidt",
        model="eleven_monolingual_v1"
    )

    print('Here we go!')
    play(audio)

