import csv

def extract_youtube_slug(yt_url):
	if len(yt_url) < 5:
		return ''
	elif '?v=' in yt_url:
		return yt_url.split('?v=')[1]
	else:
		return yt_url.split('.be/')[1]	

# Read template
tpl_file = open('template.txt',mode='r')
# read all lines at once
tpl_string = tpl_file.read()
# close the file
tpl_file.close()

# Build YouTube links
yt_paper_ids = []
yt_ids = []
with open("youtube_ids.csv") as fp:
	reader = csv.reader(fp, delimiter=",", quotechar='"')
	for (r_i, row) in enumerate(reader):
		paper_id = row[1]
		youtube_url = row[4]
		yt_paper_ids.append(paper_id)
		yt_ids.append(extract_youtube_slug(youtube_url))
	

	

def get_youtube_id(paper_id):
	try:
		idx = yt_paper_ids.index(paper_id)
	except:
		return ''
	return yt_ids[idx]

def format_day(day):
	if day[:3] == 'Mon':
		return 'Monday'
	elif day[:3] == 'Tue':
		return 'Tuesday'
	elif day[:3] == 'Wed':	
		return 'Wednesday'
	else:
		raise Exception("Invalid day string.") 



with open("InteractiveSessions.csv") as fp:
	reader = csv.reader(fp, delimiter=",", quotechar='"')
	next(reader, None)  # skip the headers
	for (r_i, row) in enumerate(reader):
		paper_id = row[0]
		title = row[1]
		abstract = row[2]
		authors = row[3]
		code = row[9]
		day = format_day(row[11])
		pheedloop = row[22]
		pdf = row[23]
		supp = row[24]
		date = row[15]
		start_time = row[16]
		end_time = row[17]
		youtube_id = get_youtube_id(paper_id)
		reviews_link = row[26]

		file_string = tpl_string.format(id=paper_id, short_title=title, paper_day=day, pdf=pdf, 
		supp=supp, code=code, video='', long_title=title, authors=authors, abstract=abstract,
		date=date, start_time=start_time, end_time=end_time, youtube_id=youtube_id, reviews_link=reviews_link, pheedloop=pheedloop)

		f = open("papers/paper_{}.md".format(paper_id), "w")
		f.write(file_string)
		f.close()