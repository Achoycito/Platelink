# import OS module
import os
 
# Get the list of all files and directories

color = "NA"
path = "D:\\Documents\\UABCS\\9no semestre\\didi\\"+color+"\\"
dir_list = os.listdir(path)

i = 0


print(len(dir_list))


for filename in dir_list:
    print(filename)
#     flag = False
#     new_name = color + str(i)

#     if(filename.endswith(".jpg")):
#         # print(filename + " termina con .jpg")
#         new_name = new_name + ".jpg"
#         flag = True
#     elif(filename.endswith(".jpeg")):
#         # print(filename + " termina con .jpeg")
#         new_name = new_name + ".jpeg"
#         flag = True
#     elif(filename.endswith(".png")):
#         # print(filename + " termina con .png")
#         new_name = new_name + ".png"
#         flag = True
#     original_name = path + filename
#     new_name = path + new_name

#     if flag==True:
#         os.rename(original_name, new_name)
#         i += 1

# print("Files and directories in '", path, "' :")
 
# prints all files
# print(dir_list)