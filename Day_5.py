# Path to the database file
db_file = r"c:\VSCODE\day5.txt"

def parse_database(filename):
	with open(filename, 'r') as f:
		lines = [line.strip() for line in f]

	# Split into ranges and available IDs
	try:
		blank_idx = lines.index('')
	except ValueError:
		raise Exception("No blank line separating ranges and IDs")

	range_lines = lines[:blank_idx]
	id_lines = lines[blank_idx+1:]

	# Parse ranges
	ranges = []
	for line in range_lines:
		if '-' in line:
			start, end = map(int, line.split('-'))
			ranges.append((start, end))
		elif line:
			# Single value range
			val = int(line)
			ranges.append((val, val))

	# Parse available IDs
	available_ids = [int(line) for line in id_lines if line]
	return ranges, available_ids

def is_fresh(ingredient_id, ranges):
	for start, end in ranges:
		if start <= ingredient_id <= end:
			return True
	return False

def main():

	# Part One
	ranges, available_ids = parse_database(db_file)
	fresh_count = sum(is_fresh(i, ranges) for i in available_ids)
	print(f"Number of fresh ingredient IDs (Part One): {fresh_count}")

	# Part Two - Efficient range merging
	def merge_ranges(ranges):
		# Sort ranges by start
		sorted_ranges = sorted(ranges)
		merged = []
		for start, end in sorted_ranges:
			if not merged or start > merged[-1][1] + 1:
				merged.append([start, end])
			else:
				merged[-1][1] = max(merged[-1][1], end)
		return merged

	merged_ranges = merge_ranges(ranges)
	total_fresh = sum(end - start + 1 for start, end in merged_ranges)
	print(f"Number of unique fresh ingredient IDs (Part Two): {total_fresh}")

if __name__ == "__main__":
	main()
