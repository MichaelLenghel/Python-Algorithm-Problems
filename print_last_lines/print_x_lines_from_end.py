# Problem: Print a certain amount of lines from the end of a text lfile
# I used two counter variables as pointers. The first one iterate 'Num_lines' number of times. We then use the second pointer that iterates until the first pointer reaches the
# end, effectively reaching the end of a file.
# Complexity: O(N)

from pprint import pprint

def tail_print(file, num_lines):
	start_ptr = end_ptr = 0
	not_enough_lines = False

	with open(file) as f:
		lines = f.readlines()

		while lines:
			end_ptr += 1

			# Break
			if end_ptr == num_lines:
				break
		else:
			raise exception("Not enough lines in the document to print ", num_lines, " from the end")
			return
			
		while lines[end_ptr:]:
			start_ptr += 1
			end_ptr += 1

		# Pretty print lines
		pprint(lines[start_ptr:])
		

if __name__ == "__main__":
	file = "numbered_doc.txt"
	num_lines = 10

	tail_print(file, num_lines)
	