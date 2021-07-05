from utils.utils import get_person, get_age
import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--person", help="The person whom's age to find.", type=str, required=True)
	args = parser.parse_args()

	person = get_person(args.person)
	age = get_age(person)
	print(f"{args.person} is {age} old according to Google.")
