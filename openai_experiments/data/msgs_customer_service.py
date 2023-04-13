import openai_experiments
import pandas as pd
#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from pathlib import Path


location = Path(openai_experiments.__file__).parent / 'data' / 'customer_service_data_short.csv'

df = pd.read_csv(location)

# manual best agent calc
df['Sentiment'] = df['Text'].apply(lambda x: TextBlob(x).sentiment.polarity)
avg_sentiment_by_agent = df.groupby('Agent')['Sentiment'].mean()
best_agent = avg_sentiment_by_agent.idxmax()

print(avg_sentiment_by_agent)
print(f'The best agent is {best_agent} with an average sentiment score of {avg_sentiment_by_agent[best_agent]}')
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print()

#now lets have ChatGPT help
messages = [
     dict(
         role="system",
         content="""
            Please use the table df. Our goal is to identify the agent with the best customer sentiment. 
            The data contains customer service call logs. The first row contains the column description. 
            The Agent name is column Agent. The sentiment of the conversation is captured in column Text, but we also 
            need to take into account. The longer the call the better. The higher the customer rating the better. The 
            higher the sentiment score the better. We should take an average.  
         """
    ),
    # dict(
    #     role="system",
    #     content="""
    #         You are a customer service agent supervisor. Use the data about customer service calls to identify which
    #         agent performed best and why. The data shows which Agent performed the call. The key data to look at are sentiment in the user response in colum Text,
    #         customer wait time in column Customer Wait Time, Call Duration in column Chat Duration, Customer Rating in
    #         column Customer Rating, and Customer Comment in column Customer Comment. In your answer, please indicate any correlation with the
    #         Browser in column Browser, Operating System in column Operating System, and Geo Location in column Geo.
    #     """
    # ),
    dict(
        role="system",
        content="""
        You are a customer service agent supervisor. Use the data about customer service calls to identify which 
        agent performed best and why. 
    """
    ),
    dict(
        role="assistant",
        content="""
           Can you find a correlation between customer sentiment and other parameters in the data? Please calculate the 
           correlation coefficients. 
        """
    ),
]

