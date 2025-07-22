import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from langchain import hub
from crewai.tools import tool
from typing import List


class LangSmithHubPromptCollector:

    def __init__(self, 
                 binary_location="/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary",
                 version_main=140,
                 headless=False):
        options = uc.ChromeOptions()
        options.binary_location = binary_location
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-notifications')
        options.add_argument('--disable-popup-blocking')

        self.driver = uc.Chrome(options=options, version_main=version_main, headless=headless)

    def collect_prompts(self, query):
        try:
            titles = self._get_titles(query)
            print(titles)
        except Exception as e:
            raise RuntimeError(f"An error occurred while collecting prompts: {e}")
        finally:
            self.driver.quit()

        prompts = self._get_prompts(titles)
        return prompts
    
    def _get_titles(self, query):
        titles= []
        query = query.strip()
        query = query.replace(" ", "+")
        query = query.replace("-", "+")
        url = f"https://smith.langchain.com/hub/search?q={query}"
        self.driver.get(url)
        time.sleep(5)
        elements = self.driver.find_elements(By.CLASS_NAME, "text-lg.font-medium")
        for element in elements:
            titles.append(element.text)
        return titles
    
    def _get_prompts(self, titles):
        prompts = []
        for title in titles:
            try:
                prompt_template = hub.pull(title)
                if prompt_template:
                    text = prompt_template.messages[0].prompt.template
                    if text and text not in prompts:
                        prompts.append(text)
            except Exception as e:
                print(f"Error occurred while fetching prompt for title '{title}': {e}")
        return prompts
    

@tool("Hub Prompt Collector")
def collect_tools_from_hub(query: str) -> List[str]:
    """
    Collects prompts from LangSmith Hub based on a search query.
    
    Args:
        query (str): The search query to find relevant prompts.
        
    Returns:
        List[str]: A list of collected prompts.
    """
    collector = LangSmithHubPromptCollector()
    print("collecting prompts from LangSmith Hub...", collector)
    return collector.collect_prompts(query)
