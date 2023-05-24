from pytrends.request import TrendReq

DAILY_TOPICS = ["soap", "volcanoes", "bitcoin", "salad"]

class UI:
    """instantiates the menu for starting a podcast on a topic"""
    def __init__(self) -> None:
        
        pytrend = TrendReq()
        self.topics = pytrend.trending_searches(pn='united_kingdom').head(5)[0]
        
    def topic_selection(self):
        """gives the user a list of topics and returns the users choice"""
        
        print("What topic would you like to discuss today? "
              "You can choose from the following list of hot topics or decide your own:")
        for topic in self.topics:
            print(topic)

        choice = input("Your choice: ")
        return choice
            