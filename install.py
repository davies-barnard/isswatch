# installer for JasonPlotly
# Copyright 2016 Chris Davies

from setup import ExtensionInstaller

def loader():
	return IssWatchInstaller()

class IssWatchInstaller(ExtensionInstaller):
	def __init__(self):
		super(IssWatchInstaller, self).__init__(
			version='0.1',
			name='isswatch',
			description='Uses an RSS Feed from Spot the Station to provide template variables to alert to possible sighting opportunities',
			author='Chris Davies',
			author_email='weewx@davies-barnard.co.uk',
			config={
				'StdReport': {
						'isswatch': {
								'url' : 'http://spotthestation.nasa.gov/sightings/xml_files/United_Kingdom_England_Bristol.xml',
								'skin': 'isswatch',
								'HTML_ROOT': 'isswatch'
						}
				}
			},
			files=[
				('bin/user', ['bin/user/isswatch.py']),
				('skins/isswatch', ['skins/isswatch/skin.conf', 'skins/isswatch/index.html.tmpl']),
			]
		)