import re
pattern = r'[a-z]+_[a-z]+'
test_string = 'hello_world this_is_a_test I_am_working_on_a_program'
matches = re.findall(pattern, test_string)
print(matches)