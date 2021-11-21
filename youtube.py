from pytube import YouTube
ch='y'
while((ch=='y')|(ch=='Y')):
    link=input("Youtube Link: ")
    yt=YouTube(link)
    yhighest=yt.streams.get_highest_resolution()
    print("Downloading")
    yhighest.download()
    print("Downloading Finished")
    ch=input("Y for continuing, N for ending")
print("Program Finished")