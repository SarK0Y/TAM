Set-PSDebug -Trace 2
Set-Alias -Name grep -Value findstr
py.exe Z:\taw0.py  -find_files -path0 "S:\" -tmp_file "C:\Users\tst\tmp\01547.log"  -view_w "C:\Program Files\VideoLAN\VLC\vlc.exe" "--sout-x264-b-bias=-15" -view_w "C:\Program Files\SMPlayer\smplayer.exe" $args
