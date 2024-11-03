# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o")

# Invoke the model with a message
result = model.invoke("<Resort Adria has 34 standard rooms and 4 family suites, a restaurant with a seating capacity of 150, and a wellness and spa center."
                      "On Friday, 10/20/2024, 17 families arrived and stayed in standard rooms, including 1 family who stayed in a VIP family suite. Three families checked out of the hotel that day. "
                      "The total number of guests staying in the hotel on that day was 55. The restaurant operated on a half-board basis, with a turnover of €2000."
                      "The wellness center was used by 15 people,generating revenue of €100, and the accommodation sector generated revenue of €5300.>"
                      "<Your task is to act as the manager of the hospitality facility."
                      "Every day, we receive reports from the employees. Your task is to compile these reports into a suitable format once all information is collected."
                      "Create this format in HTML."
                      "Write down the percentage share of each sector in total revenue."
                      "Use the symbols % and €."
                      "Check if the percentages are correctly summed up."
                      "If you do not know the answer, say you don’t know and do not make assumptions. Instead, write: We don't have enough information on this."
                      "Write information on the total number of guests and occupied rooms. Include a list of arrivals and departures, VIP guests, average length of stay,"
                      "and revenue per sector (accommodation sector, restaurant, and wellness revenue).>")
# print("Full result:")
# print(result)
print("Content only:")
print(result.content)
