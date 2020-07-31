from pytube import YouTube
n = int(input("Número de vídeos para download:   "))
links=[]
print("\nLinks:")

for i in range(0,n):
    temp = input()
    links.append(temp)

for i in range(0,n):
    link = links[i]
    yt = YouTube(link)
    print("\nDetalhes",i+1,"\n")
    print("Título:   ",yt.title)
    print("Visualizações:  ",yt.views)
    print("Duração:  ",yt.length,"segundos")
    stream = str(yt.streams.filter(progressive=True))
    stream = stream[1:]
    stream = stream[:-1]
    streamlist = stream.split(", ")
    print("\nOpções de download:\n")
    for i in range(0,len(streamlist)):
        st = streamlist[i].split(" ")
        print(i+1,") ",st[1]," and ",st[3],sep='')
    tag = int(input("\nSelecione as itags:   "))
    ys = yt.streams.get_by_itag(tag)
    print("\nDownloading...")
    ys.download()
    print("\nDownload completo!!")
    print()