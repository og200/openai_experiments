import openai

from openai_experiments import config
from openai_experiments.data import msgs_customer_service

openai.api_key = config.api_key
def print_models():
    models = openai.Model.list()
    print(models)

if __name__ == '__main__':
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages = msgs_customer_service.messages
    )
    print(completion.choices[0].message.content)
