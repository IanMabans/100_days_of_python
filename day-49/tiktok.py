import os
import csv
import time
import random
import pandas as pd
from tiktokapi import TikTokApi
from bs4 import BeautifulSoup
from proxy_requests import ProxyRequests


# Function to scrape TikTok videos
def scrape_tiktok(keyword, num_videos=100, use_proxy=True):
    # Initialize TikTok API
    api = TikTokApi.get_instance()

    # Initialize list to store scraped data
    scraped_data = []

    # Search TikTok for the keyword
    search_results = api.search_for_hashtags(keyword, count=num_videos)

    for result in search_results:
        tiktok_url = result['video']['playAddr']
        caption = result['desc']
        hashtags = result['challenges']
        like_count = result['stats']['diggCount']
        comment_count = result['stats']['commentCount']
        view_count = result['stats']['playCount']

        # Download video without watermark
        video_filename = f"{keyword}_{time.time()}_{random.randint(1, 1000)}.mp4"
        download_video(tiktok_url, video_filename, use_proxy)

        # Append data to the list
        scraped_data.append({
            'Video_File': video_filename,
            'Caption': caption,
            'Hashtags': hashtags,
            'Like_Count': like_count,
            'Comment_Count': comment_count,
            'View_Count': view_count
        })

        # Pause for a moment to avoid being flagged
        time.sleep(random.uniform(1, 3))

    return scraped_data


# Function to download video without watermark
def download_video(url, filename, use_proxy):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.3'}

    if use_proxy:
        req = ProxyRequests(url)
        req.get()
        content = req.get_raw().content
    else:
        content = requests.get(url, headers=headers).content

    # Save video to file
    with open(filename, 'wb') as f:
        f.write(content)


if __name__ == "__main__":
    # Read keywords from CSV file
    keywords_file = 'keywords.csv'
    keywords_df = pd.read_csv(keywords_file)
    keywords_list = keywords_df['Keyword'].tolist()

    # Scrape TikTok for each keyword
    for keyword in keywords_list:
        print(f"Scraping TikTok for keyword: {keyword}")
        scraped_data = scrape_tiktok(keyword)
        # Save scraped data to CSV
        output_file = f"{keyword}_tiktok_data.csv"
        pd.DataFrame(scraped_data).to_csv(output_file, index=False)
        print(f"Scraping for keyword {keyword} completed. Data saved to {output_file}")
