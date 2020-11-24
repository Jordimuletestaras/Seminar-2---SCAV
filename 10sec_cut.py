
import subprocess as sp


if __name__ == '__main__':

    line = 'ffmpeg -i bbb.mp4 -ss 00:02:30 -to 00:02:40y -c:v copy -c:a copy 10secbbb.mp4'
    sp.run(line, shell=True)
