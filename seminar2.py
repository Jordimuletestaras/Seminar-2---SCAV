import subprocess as sp


if __name__ == '__main__':

    # ex 1

    line = 'ffmpeg -i bbb.mp4 -ss 00:02:30 -to 00:02:40y -c:v copy -c:a copy 10secbbb.mp4'
    sp.run(line, shell=True)

    # ex 2

    line = 'ffmpeg -i 10secbbb.mp4 -vf histogram -y yuv_hist.mp4'
    sp.run(line, shell=True)
    line = 'ffmpeg -i 10secbbb.mp4 -i yuv_hist.mp4 -filter_complex "overlay" 10sec_yuv_hist_bbb.mp4'
    sp.call(line, shell=True)

    # ex 3

    print("""Select the resize option
             1. 780
             2. 480
             3. 360 x 240
             4. 160 x 120""")
    selected = int(input())
    if selected == 1:
        line = 'ffmpeg -i 10secbbb.mp4 -s hd720 720_10sec_bbb.mp4'
    if selected == 2:
        line = 'ffmpeg -i 10secbbb.mp4 -s vga 480_10sec_bbb.mp4'
    if selected == 3:
        line = 'ffmpeg -i 10secbbb.mp4 -vf "scale=(iw*sar)*max(360/(iw*sar)\,240/ih):ih*max(360/(iw*sar)\,240/ih),crop=360:240" 360x240_10sec_bbb.mp4'
    if selected == 4:
        line = 'ffmpeg -i 10secbbb.mp4 -vf "scale=(iw*sar)*max(160/(iw*sar)\,120/ih):ih*max(160/(iw*sar)\,120/ih),crop=160:120" 160x120_10sec_bbb.mp4'
    sp.run(line, shell=True)

    # ex 4

    line = 'ffmpeg -i 10secbbb.mp4 -ac 1 -c:a aac -c:v copy mono_codec_10sec_bbb.mp4'
    sp.run(line, shell=True)
