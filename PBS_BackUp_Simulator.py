# a python function to create back up import and file imports on the CHPC PBS. 
#Gaurav Sablok 
#Senior Postdoctoral Fellow Faculty of Natural and Agricultural Sciences 
#Room 7-35, Agricultural Sciences Building 
#University of Pretoria, Private Bag X20 Hatfield 0028, 
#South Africa 
import os 
import subprocess
def PBSBackUpSimulator():
    """a function to backup your files in the PBS system.
    """
    dir_extend = []
    dir_clone = []
    file_extension = []
    while True:
        take_dir_extend = input("Please enter the original dir path")
        take_dir_clone = input("Please enter the clone dir path")
        take_file_extension = input("Please enter the file extension to be backed up")
        if dir_extend and dir_clone and file_extension is "":
            break
        print(f"the original directory path is: {dir_extend} and the \
                      the clone directory path is {dir_clone} and the file \
                                     is {file_extension}")
    if not os.path.exists(dir):
        os.mkdir(os.path.join(os.getcwd(), clone_dir))
        print(f"the path to the clone directory is: {os.path.join(os.getcwd(), clone_dir)}") 
    filenames = []
    filenames_with_path = []
    dir_path = []
    while True:
        take_dir_path = input("Please enter the directory_path")
        dir_path = os.path.join(os.getcwd(), take_dir_path)
        if take_dir_path is "":
            break
    for dirnames, filenames in os.walk("dir_path"):
        for i in dirnames:
            dir_path.append(i)
        for file in filenames:
            for j in file:
                if j.endswith("filenames")
                filenames_with_path.append(os.path.join(os.getcwd(),j))
    for i in range(len(filenames_with_path)):
        print(f"{filenames_with_path[i]} back_up_{filenames_with_path[i]}")
        with open(filename_back, "r") as backup:
            backup.write(f"{filenames_with_path[i]} back_up_{filenames_with_path[i]}")
            backup.close()
        subprocess.run("cp -r f"{filenames_with_path[i]} back_up_{filenames_with_path[i]}"", shell = True)
        if __name__ == __main__:
            main()
