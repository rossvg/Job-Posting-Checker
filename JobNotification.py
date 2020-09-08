'''
Job Notifier                                        Ross Vrana-Godwin

Script checks if a job on a website is still up, and pushes an appropriate windows 10 notification

August 18, 2020 notes : Make this fully customizable. Accept user entered website and job posting from csv
file of possibilities and show all. This is more of a working concept with two methods.


'''


from bs4 import BeautifulSoup #  Used for finding the correct link for job posting in the html from website
import requests
from plyer import notification #  Sends a customizable win10 notification
import time


def main():
    
    showFirstJob()    
    time.sleep(7.5) #  Pause for smooth transitions of notifications.
    showSecondJob()
    
    
def showFirstJob():
    
    r = requests.get('https://www.eluta.ca/jobs-at-urthecast#!')
    if r:
        soup = BeautifulSoup(r.text,'html.parser')
        jobLink = soup.findAll('a', title='Jr. Software Engineer (SAR) - 6-9 mo contract')
        if jobLink:
            notification.notify(
            title='<SampleCompany> Job Posting Update',
            message='The Jr. Software Engineer position is still posted on <sampleCompany>.com',
            app_icon='C:\\Users\\Ross\\Desktop\\PythonLearning\\Notif\\Danleech-Simple-Linkedin.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,# seconds
            )
        else:
            notification.notify(
            title='<sampleCompany> Job Posting Update',
            message='The Mechatronics Engineer position is NO LONGER POSTED on automationX.com/careers/',
            app_icon='C:\\Users\\Ross\\Desktop\\PythonLearning\\Notif\\Danleech-Simple-Linkedin.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            )
    else:
        raise RuntimeError("bad website")

def showSecondJob():
    
    r = requests.get('https://automationx.ca/careers/')
    if r:
        soup = BeautifulSoup(r.text,'html.parser')
        jobLink = soup.findAll('a', title='Mechatronics Engineer')
        if jobLink:
            notification.notify(
            title='<sampleCompany> Job Posting',
            message='The Mechatronics Engineer position is still posted on <sampleCompany>.com',
            app_icon='C:\\Users\\Ross\\Desktop\\PythonLearning\\Notif\\Danleech-Simple-Linkedin.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,# seconds
            )
        else:
            notification.notify(
            title='automationX Job Posting',
            message='The Mechatronics Engineer position is NO LONGER POSTED on automationX.com/careers/',
            app_icon='C:\\Users\\Ross\\Desktop\\PythonLearning\\Notif\\a_logo.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            )
    else:
        raise RuntimeError("bad website")
    

    
if __name__ == "__main__":
    main()


