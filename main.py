from tweet_generator import TweetGenerator
from spaces_downloader import download_twitter_space, extract_host_details
from twitter_api import TwitterAPI
import assemblyai as aai
import os
import sys







def main():
    space_url = sys.argv[1]  #"https://twitter.com/i/spaces/1mrGmyYeAqQGy"  # Verify this URL
    cookies_path = "metadata/twitter.com_cookies.txt"
    
    # Ensure cookies file exists
    if not os.path.exists(cookies_path):
        print(f"Cookie file {cookies_path} not found.")
        return
    hostName=""
    
    json_file = download_twitter_space(space_url, cookies_path)
    if json_file and os.path.exists(json_file):
        hostName=extract_host_details(json_file)

    aai.settings.api_key = os.environ["AAI_API_KEY"]
    transcriber = aai.Transcriber()

    transcript = transcriber.transcribe("/home/lokesh/bot-test/metadata.m4a")
    # transcript = transcriber.transcribe("./my-local-audio-file.wav")

    # transcription text
    speech = transcript.text
    print("transcription Completed")
    model = "llama2-uncensored"
    prompt = f"""
You are an expert assistant with expertize in summarizing speeches. Provide a summary of the entire speech in 150 words with important points.
Speech:
{speech}
"""
    main_tweet = "Here is the summary of spaces hosted by {hostName}"

    generator = TweetGenerator(model=model)
    tweets = generator.generate_tweets(prompt)

    twitterAPI = TwitterAPI()
    twitterAPI.tweet_thread(main_tweet, tweets)


if __name__ == "__main__":
    main()