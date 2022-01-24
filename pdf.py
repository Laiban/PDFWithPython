import pypdf2

with open('dummy.pdf','r') as file:
	reader = pypdf2.pdfFileReader(file)
	page=reader.getPage(0)
	page.rotateCounterClockwise(180)
	writer = pypdf2.pdfFileWriter()
	writer.addPage(page)
	with open('tilt.pdf','wb') as new_file:
		writer.write(new_file)

