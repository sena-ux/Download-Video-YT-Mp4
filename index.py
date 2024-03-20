from pytube import YouTube

def on_progress(stream, chunk, bytes_remaining):
    current = stream.filesize - bytes_remaining
    percent = (current / stream.filesize) * 100
    print(f"\rDownloading... {percent:.2f}%", end='', flush=True)

def download_video(url):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        # Pilih stream dengan kualitas tertinggi
        video = yt.streams.get_highest_resolution()
        #tempat penyimpanan
        output_path = "./download"
        # Unduh video ke output_path
        video.download(output_path)
        print("Video berhasil diunduh!")
    except Exception as e:
        print("Terjadi kesalahan:", str(e))

if __name__ == "__main__":
    video_urls = []
    while True:
    	url = True
    	while True:
    		url = input("Masukkan URL video (tekan Enter untuk berhenti): ")
    		if url == "":
    			url = False
    			break
    		video_urls.append(url)

    	for url in video_urls:
        	download_video(url)

    
