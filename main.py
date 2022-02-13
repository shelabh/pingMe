from pynotifier import Notification

Notification(
	title='heyy',
	description='how are you',
	icon_path='/image/unknown.png', # On Windows .ico is required, on Linux - .png
	duration=5,                                   # Duration in seconds
	urgency='normal'
).send()