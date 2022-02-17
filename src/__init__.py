import youtube_dl

class YtR_VideoGET:

    def __init__(self, location: str):
        self.videos_loc = location + "/"


    def __reddit(self, link :str):
        caption = link.split('/')[-2]
        print(caption)
        self.ydl_opts2 = {
                    'format': 'bestvideo+bestaudio/best',  #set video titl as opt
                    'outtmpl' : self.videos_loc + caption + '.%(ext)s',
                    }


        with youtube_dl.YoutubeDL(self.ydl_opts2) as ydl: #download
                ydl.download([link])
        
    def _youtube(self, link:str):
        self.ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            }

        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl: # get video title
            info_dict = ydl.extract_info(link, download=False)
            video_title = info_dict.get('title', None)

        self.ydl_opts2 = {              # set video title as opt
            'format': 'bestvideo+bestaudio/best',
            'outtmpl' : self.videos_loc + video_title + '.%(ext)s',
            }

        with youtube_dl.YoutubeDL(self.ydl_opts2) as ydl: #download
            ydl.download([link])
