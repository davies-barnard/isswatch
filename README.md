# ISS-WATCH for WEEWX
Simple Search List extension for ISS Sightings

weewx extension that implements uses an RSS Feed from Spot the Station to 
provide template variables to alert to possible sighting opportunities

Copyright 2016 Chris Davies

## Background:

The skin now includes two files one that works with Bootstrap and can be included into another skin and a standalone version.


## Installation instructions:

1) run the installer:

setup.py install --extension extensions/isswatch

or

./bin/wee_extension --install=extensions/isswatch.tar.gz

2) restart weewx:

sudo /etc/init.d/weewx stop
sudo /etc/init.d/weewx start

Manual installation instructions:

1) copy files to the weewx user directory:

cp bin/user/isswatch.py /home/weewx/bin/user
cp -R skins/isswatch /home/weewx/skins/

2) in weewx.conf, add the following section 

[StdReport]
	[[isswatch]]
			skin = isswatch
			HTML_ROOT = public_html/isswatch

3) restart weewx

sudo /etc/init.d/weewx stop
sudo /etc/init.d/weewx start

