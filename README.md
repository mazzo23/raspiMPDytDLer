# raspiMPDytDLer
#################################
# Installation of raspiMPDytDLer:#
#################################
this guide assumes you already have a clean raspbian with all nessesary network stuff installed and ready to go. 
here is where we start.
Basic install routine for all Linux distros(i guess).

# essentials

# ffmpeg (video and conversion)
sudo apt install ffmpeg 

#youtube-dl (downloading youtube streams)

sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl

sudo chmod a+rx /usr/local/bin/youtube-dl

#Daemon Control
sudo apt install mpd

sudo apt install mpc 

sudo apt install ncmpcpp 

#####nice terminal that works well together with ncmpcpp (for client only, no use on raspi)
sudo apt install tilda 


