__author__ = 'Brian'
import os
import subprocess

cmd_base = '/var/packages/VideoStation/target/bin/synovideoconversion ' \
      '-i {input_video} -o {output_video} ' \
      '-v original -a -1 -u 1026'

videos = [os.path.join(dp, f) for dp, dn, filenames in os.walk('/volume1/video') for f in filenames if os.path.splitext(f)[1] in ('.mp4', '.mkv', '.rmvb', '.avi', '.flv')]
for video in videos:
    if '@eaDir' not in video or '(original) not in video':
        input_video = video
        if video.split('.')[-1] in ('mp4', 'mkv', 'avi'):
                output_video = video[:-4]+' (original).mp4'
        elif video.split('.')[-1] in ('rmvb'):
            output_video = video[:-5]+'_original.mp4'
        else:
            output_video = None
        if output_video:
            cmd = cmd_base.format(input_video="'"+input_video+"'", output_video="'" + output_video + "'")
            resp_code = subprocess.check_call(cmd, shell=True)
            if resp_code != 0:
                print('get profit error: {cmd}'.format(cmd=cmd))
                continue
    else:
        continue

