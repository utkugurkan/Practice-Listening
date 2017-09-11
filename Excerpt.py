import webbrowser

class Excerpt:
	link_idx = 0
	title_idx = 1
	composer_idx = 2
	genre_idx = 3
	date_idx = 4
	features_idx = 5

	def __init__(self, line):
		info_list = line.split(",")

		self.link = info_list[Excerpt.link_idx]
		self.title = info_list[Excerpt.title_idx]
		self.composer = info_list[Excerpt.composer_idx]
		self.genre = info_list[Excerpt.genre_idx]
		self.date = info_list[Excerpt.date_idx]
		self.features = info_list[Excerpt.features_idx:]

		self.features_print_idx = 0 # Used when printing features one by one

	def open_link(self):
		webbrowser.open(self.link)

	def print_single_feature(self):
		print(self.features[self.features_print_idx])
		self.features_print_idx = (self.features_print_idx + 1 ) % len(self.features)

