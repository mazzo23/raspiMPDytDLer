# ssh into raspi 
user=pi	
pw=w@w  

########################################################-MPD-###########################################################

# MPD(Daemon):

## mpd
`sudo apt install mpd`

## make config files:

'mkdir ~/.mpd .ncmpcpp'

## in .mpd create:
touch mpd.conf

## insert:
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

#OR use this:

#mpc 
sudo apt install mpc

to control the Daemon :)

ex.:
mpc -h 192.168.0.102 playlist 
mpc -h 192.168.0.102 play (pause,next,stop,...)

mpc -h IP OPTION

#or 

mpc stats
mpc play (when local)


######################
# in .ncmpcpp create:#
######################

touch config

#insert:

nano .ncmpcpp/config

##############################################################################
% egrep -v '^#' .ncmpcpp/config
mpd_host = "127.0.0.1"
mpd_port = "6600"
mpd_music_dir = "/home/pi/Music/"
visualizer_in_stereo = "yes"
visualizer_fifo_path = "~/.mpd/mpd.fifo"
visualizer_output_name = "my_fifo"
visualizer_sync_interval = "30"
visualizer_type = "spectrum"
visualizer_look = "◆▋"
message_delay_time = "3"
playlist_shorten_total_times = "yes"
playlist_display_mode = "columns"
browser_display_mode = "columns"
search_engine_display_mode = "columns"
playlist_editor_display_mode = "columns"
autocenter_mode = "yes"
centered_cursor = "yes"
user_interface = "alternative"
follow_now_playing_lyrics = "yes"
locked_screen_width_part = "60"
display_bitrate = "yes"
external_editor = "nano"
use_console_editor = "yes"
header_window_color = "cyan"
volume_color = "red"
state_line_color = "yellow"
state_flags_color = "red"
progressbar_color = "yellow"
statusbar_color = "cyan"
visualizer_color = "red"
mouse_list_scroll_whole_page = "yes"
lines_scrolled = "1"
enable_window_title = "yes"
song_columns_list_format = "(25)[cyan]{a} (40)[]{f} (30)[red]{b} (7f)[green]{l}"

##############################################################################

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
#########################################################################################################################
#replace url from the playlist you created in Youtube, and execute the command to download the out to "/home/pi/Music/"##
#########################################################################################################################


#downloads a saved YT-playlist(must be unlisted or public)and converts it to *.MP3
youtube-dl https://www.youtube.com/playlist?list=XXXXXXXXXXXXXXXXXXXXXXX -x --audio-format "mp3" --audio-quality 0 --add-metadata --metadata-from-title "%(artist)s - %(title)s" --verbose -o "/home/pi/Music/%(title)s.%(ext)s"


#dowloads a video from tvthek.orf.at (find *.m3u8 playlist first then replace url) converts to *.MP4
youtube-dl --console-title --hls-prefer-native -c --no-part "https://apasfiis.sf.apa.at/ipad/cms-austria/2019-01-22_2015_in_02_Universum--Dyna_____14002090__o__7702361505__s14434296_Q8C.mp4/playlist.m3u8" -o "/home/pi/Videos/Universum - Löwen.mp4"

#########################################################################################################################

#id3Tags for fixing the metadata

https://squell.github.io/id3/

#MPD WebClient

https://fatg3erman.github.io/RompR/

