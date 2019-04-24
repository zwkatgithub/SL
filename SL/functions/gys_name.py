import docx
from SL.config import GYS_NAME
from SL.config import STR_NAME


def gys_name_inspect(gys_name, doc):

	for para in doc.paragraphs:
		for gys in GYS_NAME:
			if gys in para.text:
				rs = [r for r in para.runs if r.underline]
				s = ''.join([r.text.strip() for r in rs])
				if s != gys_name:
					for r in rs:
						r.font.highlight_color = docx.enum.text.WD_COLOR_INDEX.YELLOW
				return doc
	return doc
	
	
def str_name_inspect(str_name, doc):
	for para in doc.paragraphs:
		for str_ in STR_NAME:
			if  str_ in para.text:
				rs = [r for r in para.runs if r.underline]
				s = ''.join([r.text.strip() for r in rs])
				if s != str_name:
					for r in rs:
						r.font.highlight_color = docx.enum.text.WD_COLOR_INDEX.YELLOW
				return doc
	return doc
