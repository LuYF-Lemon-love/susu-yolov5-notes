import os

def re_name(dirname = ".", prefix = "train_"):
    print(len(os.listdir(dirname)))
    i = 0
    for file in os.listdir(dirname):
        i += 1
        print(file)
        suffix = os.path.splitext(file)[1]
        os.rename(dirname + "/" + file, dirname + "/" + prefix + str(i) + suffix)
        print(prefix + str(i) + suffix)
        # if os.path.splitext(file)[1] == '.ts':
        #     os.rename(file,os.path.splitext(file)[0].rjust(10,'0') + ".ts")
        #     print(file)

if __name__ == "__main__":
    re_name("./CMR_dataset/images/val", "val_")
