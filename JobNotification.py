'''
Job Checker                                        Ross Vrana-Godwin

Script checks if a job on a website is still up, and pushes an appropriate windows 10 notification.

August 18, 2020 notes : Make this fully customizable. Accept user entered website and job posting from csv
file of possibilities and show all. This is more of a working concept with two methods.

September 9, 2020 notes: Refactored code. Removed two methods in favour of one working method. Added better comments.
Would like to make GUI of program mentioned in August 18 notes. 
'''

from bs4 import BeautifulSoup #  Used for finding the correct link for job posting in the html from website
import requests
from plyer import notification #  Sends a customizable win10 notification
import time

def main():
    
    CheckJob('https://www.eluta.ca/jobs-at-google', 'Software Engineer, iOS Applications, Chrome')
    time.sleep(7.5)
    CheckJob('https://www.eluta.ca/jobs-at-google', 'Enterprise Partner Sales Manager, Google Cloud')
    
def CheckJob(websiteUrl, jobTitle):
    '''Goes to the website, checks if title of link is there, and pushes notification
    
    Uses the requests library. If the request is good, find the a tag containing the job title.
    Then send a notification based on whether the job link is posted or not 
    '''
    
    r = requests.get(websiteUrl)
    
    if r:
        soup = BeautifulSoup(r.text,'html.parser')
        jobLink = soup.findAll('a', title=jobTitle)
        if jobLink:
            notification.notify(
            title='Job Checker',
            message = f'The {jobTitle} position is still posted on {websiteUrl}',
            app_icon='C:\\Users\\Ross\\Desktop\\PythonLearning\\Notif\\Danleech-Simple-Linkedin.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,# seconds
            )
        else:
            notification.notify(
            title='Job Checker',
            message = f'The {jobTitle} position is NO LONGER posted on {websiteUrl}',
            app_icon='C:\\Users\\Ross\\Desktop\\PythonLearning\\Notif\\Danleech-Simple-Linkedin.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,# seconds
            )
    else:
        raise RuntimeError('Website not found')
        
if __name__ == "__main__":
    main()


