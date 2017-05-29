#!/usr/bin/env python

from construct import *
import sys

# http://www.0xcafefeed.com/2007/12/yahoo-messenger-archive-file-format/

class YChatMsgAdapter(Adapter):
	def _decode(self, obj, context, username):
		ret = ""
		x = 0
		while x <  len(obj):
			ret += chr(obj[x] ^ username[x % len(username)])
			c += 1
		return ret
	def _encode(self, obj, context):
		pass

class YMessengerChatFile:

	def __init__(self, username, friend):
		self.username = username
		self.friend = friend
		self.records = []
		
	def ChatRecord(self):
		return Struct("YChatRecord",
			ULInt32("Timestamp"),
			Padding(4),
			ULInt32("DirectionFlag"),
			ULInt32("MsgLength"),
			YChatMsgAdapter(Bytes("Msg", lambda ctx: ctx.MsgLength), self.username)
		)
	
	def ParseFile(self, file):
		rec = self.ChatRecord()
		
		offset = 0
		while offset < len(file):
			try:
				record = rec.parse_stream(file)
				self.records.append(record)
				offset += 16 + record.MsgLength
			except:
				break
			
	def Print(self):
		for rec in self.records:
			if rec.Direction == 0:
				print rec.Timestamp, "-", username, "->", friend, ":", rec.Msg
			else:
				print rec.Timestamp, "-", friend, "->", username, ":", rec.Msg
			
if __name__ == "__main__":
	if len(sys.argv) < 4:
		print "Usage: yahoo_chat.py <chatfile> <username> <friendname>"
		sys.exit()
		
	chat_file = open(sys.argv[1], 'rb')
	
	chat = YMessengerChatFile(sys,argv[2], sys.argv[3])
	chat.ParseFile(chat_file)
	chat.Print()
