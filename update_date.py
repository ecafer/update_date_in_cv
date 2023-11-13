from odf import text, teletype
from odf.opendocument import load

odt_file_path = 'path-to-your-odt-file'

updated_date = 'Berlin, den 13. November 2023'

text_document = load(odt_file_path)
all_paragraps = text_document.getElementsByType(text.P)
paragraph = all_paragraps[-4]
extracted_date_line = teletype.extractText(paragraph)
core_date = extracted_date_line.replace('\t', '')
extracted_date_line = extracted_date_line.\
    replace(core_date, updated_date)

new_element = text.P()
new_element.addText(extracted_date_line)

paragraph.parentNode.insertBefore(new_element, paragraph)
paragraph.parentNode.removeChild(paragraph)

text_document.save('result.odt')
