import sys
script, input_encoding, error = sys.argv # use cl-args for variables


def main(language_file, encoding, errors):
    line = language_file.readline() # returns one line from file

    if line:
        print_line(line, encoding, errors) # use print_line function
        return main(language_file, encoding, errors)
    
def print_line(line, encoding, errors):
    next_lang = line.strip() # remove whitespaces from line
    raw_bytes = next_lang.encode(encoding, errors = errors) # encodes text utf-8
    cooked_string = raw_bytes.decode(encoding, errors=errors) # decodes string

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8") # open file and set encoding

main(languages, input_encoding, error) # run main function
