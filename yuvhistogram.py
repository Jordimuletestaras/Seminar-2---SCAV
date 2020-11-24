import subprocess as sp


if __name__ == '__main__':

    line = 'ffmpeg -i 10secbbb.mp4 -vf histogram -y yuv_hist.mp4'
    sp.run(line , shell=True)
    line = 'ffmpeg -i 10secbbb.mp4 -i yuv_hist.mp4 -filter_complex "overlay" 10sec_yuv_hist_bbb.mp4'
    sp.call(line, shell=True)