import re
import sys
from collections import OrderedDict

def main():
	"""Return non duplicate-records in the order they're read using the highest order name format."""
	num_lines = int(sys.stdin.readline().strip())
	records = OrderedDict()
	for line in sys.stdin:
		line = line.strip()
		ssn_match = re.search(r'\d{9}', line)
		ssn = ssn_match.group(0)
		if ssn in records.keys():
			records[ssn].append(line.rpartition(':')[0])
		else:
			records[ssn] = [line.rpartition(':')[0]]
	for record in records.items():
		names = record[1]
		longest_name = max(names, key=len)
		display_name = longest_name
		if ',' in longest_name:
			(last_name, seperator, given_name) = longest_name.rpartition(',')
			display_name = ' '.join([given_name.strip(), last_name.strip()])
		print '{display_name}:{ssn}'.format(display_name=display_name, ssn=record[0])

if __name__ == '__main__':
	main()