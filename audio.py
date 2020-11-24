import subprocess as sp


if __name__ == '__main__':

    line = 'ffmpeg -i 10secbbb.mp4 -ac 1 -c:a aac -c:v copy mono_codec_10sec_bbb.mp4'
    sp.run(line, shell=True)