#Coder Name : Mr.F3eLL Ganns
#Do not change rights , Remember the hacker who makes tools , The tools do not make a hacker
import urllib2,os
while True:

    print("""\033[34;1m
   mm.           dM8
   YMMMb.       dMM8
    YMMMMb     dMMM'
     YMMMb   dMMMP
       YMMM  MMM'
          MbdMP
      .dMMMMMM.P   -=[ADMIN PANEL FINDER TERMUX]=-
     dMM  MMMMMMM  -=[Coded By : Mr.F3eLL]=-
     8MMMMMMMMMMI  -=[Team : BlackHat Hacker Indonesia]=-
      YMMMMMMMMM   -=[Facebook : Rafell]=-
        MMMMMMP
       MxM .mmm
""")
    admin_site = list(open("admin.txt","r"))
    print ("\033[31;1m - Warning : Add a link like this > [http://www.localhost.com] ")
    web_url = raw_input(" - URL : ")
    
    if "http://" not in web_url:
        if "https://" in web_url:
            web_url = web_url.replace("https://","http://")
        else:
            web_url = "http://"+web_url
            
    if not web_url.endswith("/"):
        web_url = web_url+"/"
    print("\n")

    admin_url_site = []
    for i in admin_site:
        try:
            open_web_url = urllib2.urlopen(web_url+i)
            if open_web_url:
                print " [+] Found : "+web_url+i 
                admin_url_site.append(web_url+i)
        except:
            print " [!] Not Found : "+i

    print "---------------------------------------------------\n - Found ones : "
    for found in admin_url_site:
        print (found)

    raw_input("\n ...")
    os.system("cls" or "clear")
    print "- Found ones : "
    for found in admin_url_site:
        print (found)
