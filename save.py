import json


def save_content(content, file_to_save_to = "save_file.json"):
    json_content = json.dumps(content) # tuples will be turned into lists

    with open(file_to_save_to, "+wt") as f:
            f.write(json_content)
    print(json_content)

content = [("January", "1"), ("February", "2"), ("March", "3")]
save_content(content, "test_file.json")