import time
import webbrowser
total_breaks=3
break_counts=0
print("The program starts at " + time.ctime())
while(break_counts < total_breaks):
    time.sleep(3*60*60)
    webbrowser.open("http://youtube.be/s7L2PVdrb_8")
    break_counts=break_counts+1

