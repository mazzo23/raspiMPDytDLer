# Troubleshooting

### encountered problems:

**Webinterface-Rompr:**  
* Rompr does not send commands to MPD
* Music collection update failed

**apache2 log:**  
* call to undefined function connect_to_database() in /var/www/html/rompr/backends/sql/backend.php  
* PHP Notice:  Undefined index: collection_type in /var/www/html/rompr/index.php on line 138, referer: http://192.168.0.102/rompr/  
* PHP Warning:  include(): Failed opening 'backends/sql//specifics.php' for inclusion (include_path='.') in /var/www/html/rompr/index.php on line 138  
* PHP Notice:  Undefined index: collection_type in /var/www/html/rompr/includes/functions.php on line 494, referer: http://192.168.0.102/rompr  
* PHP Warning:  file_put_contents(prefs/prefs.var): failed to open stream: No such file or directory in /var/www/html/rompr/includes/vars.php on line 298  
* ERROR!              : COULD NOT SAVE PREFS, referer: http://192.168.0.102/rompr/index.php  
* PHP Warning:  mkdir(): Permission denied in /var/www/html/rompr/includes/firstrun.php on line 29, referer: http://192.168.0.102/rompr/index.php  


