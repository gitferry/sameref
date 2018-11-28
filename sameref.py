from refextract import extract_references_from_file
import os

def extract_title(misc):
    return misc.split('.')[0]

def read_files_from_path(directory_path):
    refrence_dic = {}
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.pdf'):
            references = extract_references_from_file(directory_path + file_name)
            for reference_item in references:
                if reference_item.has_key('misc'):
                    title  = extract_title(reference_item['misc'][0])
                    if refrence_dic.has_key(title):
                        refrence_dic[title] += 1
                    else:
                        refrence_dic[title] = 1
    
    for k, v in refrence_dic.iteritems():
        if v > 1:
            print k, v

if __name__ == "__main__":
    read_files_from_path("./test/")


# TODO: read files from a directory path
# TODO: extract references from each file
# TODO: extract titles from each file
# TODO: use a dic to store a "title -> count" mapping