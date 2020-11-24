import subprocess as sp


if __name__ == '__main__':

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
    else:
        print("chosse a valid option")

    sp.run(line, shell=True)
