import os
while True:
    try:
        os.system("python3 twitter_stream_download.py -q submarino -d data")
    except:
        pass
    else:
        break
