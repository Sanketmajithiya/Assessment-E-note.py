from datetime import datetime

def log_file(Details):
    datetime = datetime.now().strftime("%Y-%m-%d %H: %M:%s")
    file = open('log.txt','a')
    file.write("f{Date Time}:{Details}\n") 