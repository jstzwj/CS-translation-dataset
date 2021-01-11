


if __name__ == "__main__":
    in_path = "AlexNet论文翻译-中英文对照.txt"
    out_path = "out.txt"

    with open(in_path, 'r', encoding="utf-8") as f:
        lines  = f.readlines()

    english_sections = []
    chinese_sections = []

    is_en = True
    space_line = False
    for each_line in lines:
        
        if len(each_line.strip()) == 0:
            space_line = True
        else:
            space_line = False


