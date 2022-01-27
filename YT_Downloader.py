from pytube import YouTube

ch = {1 : "Title" ,2 : "Thumbnail", 3 : "Download Video" , 0 : "Exit" }

# def get_title(link):
#     yt = YouTube(link)
#     print(yt.title(link))
# def get_thumbnail():
#     pass
# def get_video():
#     pass

# def main():

if __name__ == "__main__":
    link = "https://www.youtube.com/watch?v=yMpt1AAIRPQ"
    yt = YouTube(link)
    while True:
        print(ch)
        oc = int(input())
        if oc == 1:
            # get_title(link)
            print(yt.title)
        elif oc == 2:
            # get_thumbnail(link)
            print(yt.thumbnail_url)
        elif oc == 3:
            # get_video(link)
            SAVE_PATH = "D:\python"
            # mp4files = yt.filter('mp4')
            # d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
            # stream = yt.streams.first()
            
            try: 
            # downloading the video 
                # stream.download(SAVE_PATH)
                yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(SAVE_PATH)
            except: 
                print("Some Error!") 
            print('Task Completed!') 
        elif oc == 0:
            exit()
        else :
            print("Enter valid Choice")








# link = "https://www.youtube.com/watch?v=EAYlckSaviI"
# yt = YouTube(link)

# print(yt.title)
# print(yt.thumbnail_url)
# videos = yt.streams.all()
# vid = list(enumerate(videos))
# for i in vid:
#     print(i)
# strm = int(input("enter :"))
# # videos[strm].download()

