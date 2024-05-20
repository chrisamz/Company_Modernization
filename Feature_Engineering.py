pip install pandas requests beautifulsoup4 tweepy

import pandas as pd
import requests
from bs4 import BeautifulSoup
import tweepy

def check_website_presence(domain):
    """Check if the company has a website."""
    try:
        response = requests.get(domain)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def get_social_media_activity(handle):
    """Check social media activity for a given handle using Twitter API."""
    # Replace with your own Twitter API credentials
    consumer_key = 'YOUR_CONSUMER_KEY'
    consumer_secret = 'YOUR_CONSUMER_SECRET'
    access_token = 'YOUR_ACCESS_TOKEN'
    access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
    
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    try:
        tweets = api.user_timeline(screen_name=handle, count=100, tweet_mode='extended')
        return len(tweets)
    except tweepy.TweepError:
        return 0

def check_use_of_digital_tools(domain):
    """Check for use of digital tools by scraping the company's website."""
    try:
        response = requests.get(domain)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Example of checking for presence of certain keywords/tools
        keywords = ['Shopify', 'WordPress', 'Google Analytics', 'Salesforce']
        tools_used = [kw for kw in keywords if kw.lower() in soup.text.lower()]
        return len(tools_used)
    except requests.exceptions.RequestException:
        return 0

def feature_engineering(companies_df):
    """Create features indicating technology adoption level for each company."""
    features = []
    for index, row in companies_df.iterrows():
        domain = row['website']
        twitter_handle = row['twitter_handle']
        
        website_presence = check_website_presence(domain)
        social_media_activity = get_social_media_activity(twitter_handle)
        digital_tools = check_use_of_digital_tools(domain)
        
        features.append({
            'company': row['company'],
            'website_presence': website_presence,
            'social_media_activity': social_media_activity,
            'digital_tools': digital_tools
        })
        
    features_df = pd.DataFrame(features)
    return features_df

if __name__ == "__main__":
    # Example usage:
    data = {
        'company': ['Company A', 'Company B'],
        'website': ['http://companya.com', 'http://companyb.com'],
        'twitter_handle': ['companya', 'companyb']
    }
    companies_df = pd.DataFrame(data)
    
    features_df = feature_engineering(companies_df)
    print("Feature Engineering Completed:")
    print(features_df)
