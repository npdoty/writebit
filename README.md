# writebit
Robot that tracks and announces writing wordcounts. See it in use for my writing at [@writebit](https://twitter.com/writebit).

## Usage

1. Set up `config.py` to include consumer key and secret and access token and secret (the latter can be obtained using `get_access_token.py`).

2. Create a `cron` job, or equivalent. For example:

        launchctl load ./name.npdoty.writebit-wordcount.plist