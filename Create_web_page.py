#!/usr/bin/python
import os
import webbrowser


# -----


# ***********************************************************************************************
# *
# *  Script name: create_cam_web_page
# *
# *  Description :  This function create a web page contents the camera commands and open the web page.
# *
# ***********************************************************************************************
def create_cam_web_page():
    file = 'camera.html'
    file_path = os.path.join(os.getcwd(), 'TestDataFiles', 'html', file)

    for cnt in range(1, 1 + 1):
        if cnt == 1:
            web_site = 'google.com'
            f = open(file_path, 'w')
            message = '''
            <html>
                <head>Connected Camera IP: {0} <br><br></head>
                <body>
                    <label>Camera Model and Serial <br></label>
                    <a href="http:{0}">http:{0}<br></a>
                    <a href="http:{0}">http:{0}<br></a>
                    <br>            
                </body>
                <body>
                    <label>Radios and Languages<br></label>
                    <a href="http:{0}">http:{0}<br></a>
                    <a href="http:{0}">http:{0}<br></a>
                    <br>            
                </body>
            </html>
            '''.format(web_site)
            f.write(message)
            f.close()
        if cnt == 2:  # form
            pass

        if cnt == 10:
            pass

    webbrowser.open(file_path)

    return


if __name__ == '__main__':
    create_cam_web_page()
