def resize(patern_path):
    for file in patern_path :
        ratio_origin=cv.GetSize(file)
        print(ratio_origin)
        file_resized = cv.resize(file,ratio_origin[0]/50,ratio_origin[1]/50)

#E:\Coding\data\database\TRUMP_001
