import requests
import time,sys

class animations:
    def anim(self):
        animation = ["*","**","***","****","*****","******"]
        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\n")

    def fetchAnim(self):
        animation = ["Fetching.","Fetching..","Fetching...","Fetching....","Fetching.....","Fetching......"]
        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\n")  

class fetcher:

#Browser app fetcher
    def browserFetcher(self):
        Browser = int(input('''
        Choose the browser you need. Type "8" to skip:
            1. Chrome Installer
            2. Brave Installer
            3. Firefox Installer
            4. Opera Installer
            5. Edge Installer
            6. All of them
        '''))  

        if Browser == 1:
            x.fetchAnim()
            url ="https://www.google.com/chrome/thank-you.html?statcb=1&installdataindex=empty&defaultbrowser=0#"
            response =requests.get(url)
            open("Chrome.exe", "wb").write(response.content)
            print("Done fetching Google Chrome!")

        if Browser == 2:
            x.fetchAnim()
            url = "https://laptop-updates.brave.com/latest/winx64"
            response = requests.get(url)
            open("Brave.exe", "wb").write(response.content)
            print("Done fetching Brave Browser!")

        if Browser == 3:
            x.fetchAnim()
            url = "https://download.mozilla.org/?product=firefox-stub&os=win&lang=en-US"
            response = requests.get(url)
            open("Firefox.exe", "wb").write(response.content)
            print("Done Fetching Firefox browser!")

        if Browser == 4:
            x.fetchAnim()
            url = "https://net.geo.opera.com/opera/stable/windows?utm_tryagain=yes&utm_source=google&utm_medium=ose&utm_campaign=(none)&http_referrer=https%3A%2F%2Fwww.google.com%2F&utm_site=opera_com&&utm_lastpage=opera.com/download"
            response = requests.get(url)
            open("opera.exe", "wb").write(response.content)
            print("Done Fetching Opera browser!")

        if Browser == 5:
            x.fetchAnim()
            url = "https://go.microsoft.com/fwlink/?linkid=2109047&Channel=Stable&language=en-gb&brand=M100"
            response = requests.get(url)
            open("Edge.exe", "wb").write(response.content)
            print("Done Fetching Edge browser!")


        if Browser == 6:
            x.fetchAnim()

            
            url ="https://www.google.com/chrome/thank-you.html?statcb=1&installdataindex=empty&defaultbrowser=0#"
            response =requests.get(url)
            open("Chrome.exe", "wb").write(response.content)
            print("Done fetching Google Chrome!")

            
            url = "https://laptop-updates.brave.com/latest/winx64"
            response = requests.get(url)
            open("Brave.exe", "wb").write(response.content)
            print("Done fetching Brave Browser!")

            
            url = "https://download.mozilla.org/?product=firefox-stub&os=win&lang=en-US"
            response = requests.get(url)
            open("Firefox.exe", "wb").write(response.content)
            print("Done Fetching Firefox browser!")


            url = "https://net.geo.opera.com/opera/stable/windows?utm_tryagain=yes&utm_source=google&utm_medium=ose&utm_campaign=(none)&http_referrer=https%3A%2F%2Fwww.google.com%2F&utm_site=opera_com&&utm_lastpage=opera.com/download"
            response = requests.get(url)
            open("opera.exe", "wb").write(response.content)
            print("Done Fetching Opera browser!")


            url = "https://go.microsoft.com/fwlink/?linkid=2109047&Channel=Stable&language=en-gb&brand=M100"
            response = requests.get(url)
            open("Edge.exe", "wb").write(response.content)
            print("Done Fetching Edge browser!")


        if Browser == 8:
            print("Skipping...")
        else:
            print("Done")


#Developer tools fetcher
    def devFetcher(self):

        devFetch = int(input('''
        Choose the devTools you need. Type "8" to skip:
            1. VS Code
            2. Pycharm
            3. Python
            4. NodeJs
            5. Postman
            6. git
            7. All of the above
            8. None (skip)
        '''))
#fetchers according to selection

        if devFetch == 1:
            x.fetchAnim()
            url ="https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user"
            response =requests.get(url)
            open("VScode.exe", "wb").write(response.content)
            print("Done fetching VS Code!")

        if devFetch == 2:
            x.fetchAnim()
            url = "https://download.jetbrains.com/python/pycharm-community-2022.3.2.exe"
            response = requests.get(url)
            open("pycharm.exe", "wb").write(response.content)
            print("Done fetching Pycharm")

        if devFetch == 3:
            x.fetchAnim()
            url = "https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe"
            response = requests.get(url)
            open("python.exe", "wb").write(response.content)
            print("Done Fetching python!")

        if devFetch == 4:
            x.fetchAnim()
            url = "https://nodejs.org/dist/v18.13.0/node-v18.13.0-x64.msi"
            response = requests.get(url)
            open("node.msi", "wb").write(response.content)
            print("Done Fetching Node Installer!")
        
        if devFetch == 5:
            x.fetchAnim()
            url = "https://dl.pstmn.io/download/latest/win64"
            response = requests.get(url)
            open("postman.exe", "wb").write(response.content)
            print("Done Fetching Postman!")      
        
        if devFetch == 6:
            x.fetchAnim()
            url = "https://github.com/git-for-windows/git/releases/download/v2.39.1.windows.1/Git-2.39.1-64-bit.exe"
            response = requests.get(url)
            open("git.exe", "wb").write(response.content)
            print("Done Fetching Git!")
        
        if devFetch == 7:
            x.fetchAnim()
            #All devtools
            url ="https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user"
            response =requests.get(url)
            open("VScode.exe", "wb").write(response.content)
            print("Done fetching VS Code!")

            url = "https://download.jetbrains.com/python/pycharm-community-2022.3.2.exe"
            response = requests.get(url)
            open("pycharm.exe", "wb").write(response.content)
            print("Done fetching Pycharm")

            url = "https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe"
            response = requests.get(url)
            open("python.exe", "wb").write(response.content)
            print("Done Fetching python!")

            url = "https://nodejs.org/dist/v18.13.0/node-v18.13.0-x64.msi"
            response = requests.get(url)
            open("node.msi", "wb").write(response.content)
            print("Done Fetching Node Installer!")
        
            url = "https://dl.pstmn.io/download/latest/win64"
            response = requests.get(url)
            open("postman.exe", "wb").write(response.content)
            print("Done Fetching Postman!")      
        
            url = "https://github.com/git-for-windows/git/releases/download/v2.39.1.windows.1/Git-2.39.1-64-bit.exe"
            response = requests.get(url)
            open("git.exe", "wb").write(response.content)
            print("Done Fetching Git!")

            print("Done fetching all devTools!...")

        if devFetch == 8:
            print("Skipping....")


#music app fetcher
    def musicFetch(self):
        musFetch = int(input('''
        Choose the music app you need. Type "8" to skip:
            1. Spotify
            2. Spotube
            3. All of the above
            4. None (skip)
        '''))
        if musFetch == 1:
            x.fetchAnim()
            url = "https://download.scdn.co/SpotifySetup.exe"
            response = requests.get(url)
            open("spotify.exe","wb").write(response.content)
            print("Done fetching Spotify.")

        if musFetch == 2:
            x.fetchAnim()
            url = "https://github.com/KRTirtho/spotube/releases/latest/download/Spotube-windows-x86_64-setup.exe"
            response = requests.get(url)
            open("spotube.exe","wb").write(response.content)
            print("Done fetching Spotube")

        if musFetch == 3:
            x.fetchAnim()

            url = "https://github.com/KRTirtho/spotube/releases/latest/download/Spotube-windows-x86_64-setup.exe"
            response = requests.get(url)
            open("spotube.exe","wb").write(response.content)
            print("Done fetching Spotube")

            url = "https://download.scdn.co/SpotifySetup.exe"
            response = requests.get(url)
            open("spotify.exe","wb").write(response.content)
            print("Done fetching Spotify.")
            
        if musFetch == 8:

            print("Skipping")

 
x = animations()
f=fetcher()

print("Welcome.....to shit you need when you reinstall windows..")
x.anim()

f.browserFetcher()
f.devFetcher()
f.musicFetch()


print("Done......Files are located in the same directory as this script..")
print("More features coming soon...")
print("Thanks")