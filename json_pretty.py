import json
import sys

file_name = sys.argv[1]

if (file_name[-5:] == ".json") :
    try :
        # read ugly json data
        with open(file_name, 'r') as file_reader :
            json_content = json.load(file_reader)

        # format the text into a pretty string
        formatted_text = json.dumps(
            json_content,
            indent = 2,
            separators = (',', ': '),
            sort_keys = True,
        )

        # overwrite ugly text with prettified text
        with open(file_name, 'w') as file_writer :
            file_writer.write(formatted_text)
    except :
        print('Error found. Traceback:')
        traceback.print_exc()
    else:
        print('Success')
else :
    print("error: not .json")
