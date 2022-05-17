import urllib.request, urllib.error, urllib.parse
import time
import os
from ParseAndSave import ParseAndSave
from Email import Email

raw_data_dir = "Download_Leaderboard"
parsed_data_dir = "Data_Leaderboard"
max_page_downloads = 30

named_tuple = time.localtime()
time_string = time.strftime("%d_%m_%Y_%H_%M_%S", named_tuple)

url = 'https://linewar.com/Leaderboard/Index'
url2 = 'https://linewar.com/Leaderboard?page='

try:
    print("Starting download.")
    if not os.path.exists(raw_data_dir):
        os.mkdir(raw_data_dir)
    if not os.path.exists(parsed_data_dir):
        os.mkdir(parsed_data_dir)

    os.chdir(raw_data_dir)
    os.mkdir(time_string)
    os.chdir("..")

    parser = ParseAndSave(parsed_data_dir + "/" + time_string + ".csv")

    i = 1
    while True and i < max_page_downloads:
        if i == 1:
            response = urllib.request.urlopen(url)
        else:
            response = urllib.request.urlopen(url2 + str(i))

        webContent = response.read().decode('UTF-8')

        number = str(i)
        filename = "leaderboard_" + number + "_" + time_string + ".html"
        f = open(raw_data_dir + "/" + time_string + "/" + filename, "w", encoding='utf-8')
        f.write(webContent)
        f.close()

        parser.parse(raw_data_dir + "/" + time_string + "/" + filename)

        if parser.no_more_data():
            break
        i += 1

    print("Download finished with " + str(i) + " pages downloaded.")

    parser.save()

except Exception as e:
    print("Leaderboard downloading failed!")
    print(e.__doc__)
    print(e)
    em = Email()
    em.send("LINEWAR Download Failed", str(e.__doc__) + "\n" + str(e))
