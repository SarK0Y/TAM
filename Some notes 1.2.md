# <p align=center>Virtual Folders.</p>
This revision makes possible to proccess folder w/ links. For instance, we have two dirs (/someDir2, /someDir1) to search stuff in there, so we can merge them like that..<br>
bash> ln -s /someDir1 /VF/1<br>
bash> ln -s /someDir2 /VF/2<br>
bash> python3 /bin/tam.py -find_files -path0 "/VF" -in_name ".mp3" -in_name "some" -view_w "smplayer"<br>
# Timer's precision.<br>
To benchmark how accurate the timer on Your system, You can..<br>
bash> python3  /bin/tam.py -time_prec "time" -num_of_samples 230 <br>
or <br>
bash> python3  /bin/tam.py -time_prec "some" -num_of_samples 230 <br>
# <p align=right>Check the version.</p>
bash> python3 /bin/tam.py -ver
