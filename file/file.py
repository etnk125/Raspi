import time 
import datetime

def main():
    while True:
        f = open('file/log.txt','a')
        now = datetime.datetime.now()
        Date = now.strftime("%d/%m/%Y")
        timestamp = now.strftime("%H:%M:%S")
        output = str(Date)+' '+str(timestamp)+'\n'
        print(output)
        f.write(output)
        f.close()
        time.sleep(1)

if __name__ == '__main__':
    main()