import docx
from docx.enum.text import WD_COLOR_INDEX

class Docx:
    def __init__(self):
        pass

    @classmethod
    def markedYellow(cls, p):
        p.font.highlight_color = WD_COLOR_INDEX.YELLOW