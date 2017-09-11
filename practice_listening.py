from Excerpt import Excerpt
from random import randrange

def link_command(excerpts, excerpt_idx):
	excerpts[excerpt_idx].open_link()

def title_command(excerpts, excerpt_idx):
	print(excerpts[excerpt_idx].title)

def composer_command(excerpts, excerpt_idx):
	print(excerpts[excerpt_idx].composer)

def genre_command(excerpts, excerpt_idx):
	print(excerpts[excerpt_idx].genre)

def date_command(excerpts, excerpt_idx):
	print(excerpts[excerpt_idx].date)

def features_command(excerpts, excerpt_idx):
	excerpts[excerpt_idx].print_single_feature()


def main():
	file_name = "listening_info.txt"

	with open(file_name) as file:
		contents = file.readlines()

	excerpts = []

	for line in contents:
		excerpts.append(Excerpt(line))

	if len(excerpts) == 0:
		print("No excerpts found")
		return

	shuffle_mode = False # Plays in order by default
	excerpt_idx = 0

	while True:
		command = input("§")
	
		if command == "listen" or command == "link" or command == "play" or command == "l" or command == "p":
			link_command(excerpts, excerpt_idx)

		elif command == "title" or command == "t":
			title_command(excerpts, excerpt_idx)

		elif command == "composer" or command == "comp" or command == "c":
			composer_command(excerpts, excerpt_idx)

		elif command == "genre" or command == "gen" or command == "g":
			genre_command(excerpts, excerpt_idx)

		elif command == "date" or command == "d":
			date_command(excerpts, excerpt_idx)

		elif command == "features" or command == "info" or command == "f" or command == "i":
			features_command(excerpts, excerpt_idx)

		elif command == "shuffle_mode" or command == "shuffle" or command == "s":
			shuffle_mode = True

		elif command == "ordered_mode" or command == "ordered" or command == "o":
			shuffle_mode = False

		elif command == "next" or command == "n":
			if shuffle_mode and len(excerpts) > 1:
				cur_idx = excerpt_idx
				while (excerpt_idx == cur_idx):
					excerpt_idx = randrange(0, len(excerpts))
			else:
				excerpt_idx = (excerpt_idx + 1) % len(excerpts)

		elif command == "reset" or command == "r":
			excerpt_idx = 0

		elif command == "quit" or command == "q":
			return;

		else:
			print("Unknown command.")



if __name__ == '__main__':
    main()

