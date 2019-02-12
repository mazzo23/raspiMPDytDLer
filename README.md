# raspiMPDytDLer
#################################
#Installation of raspiMPDytDLer:#
#################################
this guide assumes you already have a clean raspbian with all nessesary network stuff installed and ready to go. 
here is where we start.
Basic intall routine for all Linux distros(i guess).

#################
#ssh into raspi #
#user=pi	#
#pw=w@w		#	
#################

#essentials:

#ffmpeg (video and conversion)
sudo apt install ffmpeg 

#youtube-dl (downloading youtube streams)

sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl

sudo chmod a+rx /usr/local/bin/youtube-dl

#Daemon Control
sudo apt install mpd

sudo apt install mpc 

sudo apt install ncmpcpp

#nice terminal that works well together with ncmpcpp (for client only, no use on raspi)
sudo apt install tilda 


##########################################################-MPD-###########################################################

#MPD(Daemon):

#mpd
sudo apt install mpd

#config:

mkdir ~/.mpd .ncmpcpp

# in .mpd create:
touch mpd.conf

#insert:
nano mpd.conf

##########################################################
music_directory "/home/pi/Music/"
playlist_directory "/home/pi/.mpd/"
db_file "/home/pi/.mpd/mpd.db"
log_file "/home/pi/.mpd/mpd.log"
pid_file "/home/pi/.mpd/mpd.pid"
state_file "/home/pi/.mpd/mpdstate"

playlist_plugin {
    name "m3u"
    enabled "true"
}
filter {
    plugin "volume"
    name "software volume"
}
audio_output {
    type            "alsa"
    name            "My ALSA Device"
    device          "hw:0,0"        # optional
   #format          "44100:16:2"    # optional
}
audio_output {
    type "alsa"
    name "my ALSA device2"
    device "hw:0"
}
audio_output {
    type                    "fifo"
    name                    "my_fifo"
    path                    "/tmp/mpd.fifo"
    format                  "44100:16:2"
}

 
bind_to_address "127.0.0.1"
port "6600"

##########################################################

#Start/Restart MPD:

#kill
sudo killall mpd
#or
pidof mpd 
kill PID

#start
mpd
mpc stats 
mpc play

##########################################################-MPD-##########################################################

##########################################################-MPC-##########################################################
#MPC(Client):
#Remoteconnection(client to MPD):

if not local(client case) then get ip:

#scan for OS and u find it

sudo apt install nmap

nmap -sn 192.168.1.0/24 #basic scan

man nmap

###################
#Clients USE this:#
###################

#ncmpcpp 
sudo apt install ncmpcpp 

ncmpcpp is just awesome looking; you can do the same with mpc basically.
i use it just because awesome.

ncmpcpp -h 192.168.0.xxx ==> to connect to MPD 

connect to MPD as client with ncmpcpp/mpc to control the MPD (get IP from raspi if not local) 

######################
# in .ncmpcpp create:#
######################

touch config

#insert:

nano .ncmpcpp/config

##############################################################################

##############################################################################
#OR us this:

#mpc 
sudo apt install mpc

to control the Daemon :)

ex.:
mpc stats
mpc -h 192.168.0.102 playlist 
mpc -h 192.168.0.102 play (pause,next,stop,...)

mpc -h IP OPTION

mpc -h 192.168.0.102 playlist





##########################################################-MPC-###########################################################

###########
#alsamixer#
###########

sudo apt install alsa-utils

#important!... was looking too long for this setting(no GUI)... just turn it up a bit Oo

alsamixer

#to ~92% to counter clipping (better Power Supply would be good) atm running at 1.8A phone charger but no crashes so far
#(no HDMI or USB exept the 64Gb SD)  
#-----------------------------------------------------------------------------------------------------------------------#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#########################################################################################################################
########################################################-YT-DLer-########################################################
##################################-Download Youtube Videos and convert them to MP3-######################################
#########################################################################################################################
#####################										  
#Console Commands:#############-https://github.com/rg3/youtube-dl/blob/master/README.md#readme
#########################################################################################################################
#replace url from the playlist you created in Youtube, and execute the command to download the out to "/home/pi/Music/"##
#########################################################################################################################


#downloads a saved YT-playlist(must be unlisted or public)and converts it to *.MP3
youtube-dl https://www.youtube.com/playlist?list=PLoUzyPs5snEf1GuRlSAfl95CVwcJAVgVr -x --audio-format "mp3" --audio-quality 0 --add-metadata --metadata-from-title "%(artist)s - %(title)s" --verbose -o "/home/pi/Music/%(title)s.%(ext)s"


#dowloads a video from tvthek.orf.at (find *.m3u8 playlist first then replace url) converts to *.MP4
youtube-dl --console-title --hls-prefer-native -c --no-part "https://apasfiis.sf.apa.at/ipad/cms-austria/2019-01-22_2015_in_02_Universum--Dyna_____14002090__o__7702361505__s14434296_Q8C.mp4/playlist.m3u8" -o "/home/mazzo/Videos/Universum - Löwen.mp4"

#########################################################################################################################

#id3Tags for fixing the metadata

https://squell.github.io/id3/
