import os

def nasa_pics(num):
    full_path = os.path.expanduser(r"~\ponko_app\nasa_pics\NasaPic.jpg")
    if num == 1:
        full_path = os.path.expanduser(r"~\ponko_app\nasa_pics\NasaPic.jpg")
    elif num == 2:
        full_path = os.path.expanduser(r"~\ponko_app\nasa_pics")

    return full_path

test_path = r"~\ponko_app\saved"

print(test_path)

print(nasa_pics(1))
print(nasa_pics(2))

 
def saved():
    return os.path.expanduser(r"~\ponko_app\saved")

print(saved())

if __name__ == "__main__":
    nasa_pics(1)
    nasa_pics(2)
    saved()