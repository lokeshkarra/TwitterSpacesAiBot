# Twitter Spaces Ai Bot
## _The project is segmented into four main components:_



- Audio Downloading      :   Utilized twspace-dl for downloading audio content
- Transcription          :   Employed the AssemblyAI API for audio transcription
- Text Summary           :   Generated summaries using the Ollama llama2-uncensored Model
- Tweet Generator        :   Implemented using tweepy


## Installation

This project requires [Python](https://www.python.org/downloads/release/python-3110/) v3.11 to run.

- Set the following environment variables 

```sh
export TWITTER_API_KEY="your_consumer_key"
export TWITTER_API_KEY_SECRET="your_consumer_secret"
export TWITTER_ACCESS_TOKEN="your_access_token"
export TWITTER_ACCESS_TOKEN_SECRET="your_access_token_secret"
export AAI_API_KEY="your_assembly_api_key"
```

Install the dependencies.

```sh
python3 -m pip install requirements.txt
curl -fsSL https://ollama.com/install.sh | sh
```
- Make sure to install Ollama llama2-uncensored
  
- Make sure to create a dir named "/metadata"
  
- Download twitter cookies (use [Get cookies.txt LOCALLY
Get cookies.txt LOCALLY](https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc?hl=en) to download cookies)

- Inside metadata dir include twitter cookies

```sh
TwitterSpacesAiBot/metadata/twitter.com_cookies.txt
```

## Execution

- Run the following command. Replace "link_to_spaces" with actual link
```sh
python main.py link_to_spaces
```




