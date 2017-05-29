#!/usr/bin/env python

"""
Chat Structure

<username>
	Archive
		Messages
			<Friend>
				chatmessages
				
"""

import sys, os

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "Usage: yahoo_profile.py .\dir\to\<username>"
		sys.exit()
	
	full_path = os.path.abspath(sys.argv[1])	
	(base, username) = os.path.split(full_path)
	if os.path.exists(full_path+"\\Archive\\Messages"):
		for friend in os.listdir(full_path+"\\Archive\\Messages"):
			if os.path.isdir(friend):
				for chat_file in [f in os.listdir(full_path+"\\Archive\\Messages\\"+friend+"\\") if f.endswith(".dat")]
					chat = YMessengerChatFile(username, friend)
					chat.ParseFile(open(chat_file, 'rb'))
					chat.Print()
	
	
	
	