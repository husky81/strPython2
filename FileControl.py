import os


# 지정된 dir 하위의 모든 filename 파일 list 생성
def find_all_files(target_dir, filename):
    file_list = []
    for (path, dir2, files) in os.walk(target_dir):
        for fn in files:
            ext = os.path.splitext(fn)[-1]
            if fn == filename:
                file_list.append(os.path.join(path, fn))
    return file_list


# 지정된 dir 하위의 모든 filename 파일 list 생성 _ 재귀함수를 사용해보려 했으나 list 누적이 안됨.
def find_all_files_reculsive(dir, filename):
    try:
        file_names = os.listdir(dir)
        for fn in file_names:
            full_filename = os.path.join(dir,fn)
            if os.path.isdir(full_filename):
                find_all_files_reculsive(full_filename, filename)
            else:
                if fn == filename:
                    print(os.path.join(dir, filename))
    except PermissionError:
        pass

