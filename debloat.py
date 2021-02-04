# This a program used to debloat your smartphone with ease.
# It requires no programming experience to use. It is just 
# like a simple application w/hich will be running on command line
# This program is developed by
# Kanak Shilledar | Class XII | Nagpur | Date: 08/07/2020

# importing libraries
import ctypes
import os
import subprocess
import sys
import colorama
import time

# initializing the color library for more support in ANSI command line color encoding 
colorama.init()

# this section will check whether the person has admin rights or not
# this program requires admin rights at least at the first run to satisfy all the requirements.
def isAdmin():  
    try:
        admin = os.getuid() == 0
    except AttributeError:
       admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    
    # if admin rights are not provided then the program will terminate within 3 seconds
    if admin != True:
        print('\033[91mYou are not an Administrator!!')
        print('Please relaunch as Administrator!!\033[00m')
        time.sleep(3)
        sys.exit()

# check for requirements
def reqSatisfied(tools):
    try:
        os.popen(tools)
        return True
    except:
        print('Requirements are not satisfied...')
        print('Installing requirements!')

# getting the list of all the installed app packages on the device
def installedApps():
    DEVICE_APPS = os.popen('adb shell pm list packages').read().split()
    for pack in range(len(DEVICE_APPS)):
        # the elements are sliced because there is 'package:' attached in front of every package
        DEVICE_APPS[pack] = DEVICE_APPS[pack][8::]
    # returning list of installed packages
    return DEVICE_APPS

# checking the admin rights
isAdmin()
# creating a constant of chinese apps with all the package names
CHINESE_APPS = ['com.zhiliaoapp.musically', 'com.baidu.searchbox', 
                'com.zhiliaoapp.musically.go', 
                'com.zhiliao.musically.livewallpaper', 
                'com.ss.android.ugc.tiktok.livewallpaper', 
                'com.tencent.mobileqq', 
                'com.netqin.ps', 'com.ps.vaultprotector', 
                'com.ss.android.ugc.boom', 'com.autonavi.minimap',
                'com.ss.android.ugc.boom.livewallpaper', 
                'com.ss.android.ugc.boomlite', 
                'sg.bigo.live', 'sg.bigo.live.lite', 
                'com.weico.international', 'com.tencent.mm', 
                'com.lenovo.anyshare.gps', 'com.xiaomi.midrop', 
                'com.uc.iflow', 'com.UCMobile.intl', 
                'com.uc.browser.en', 'com.ucturbo', 
                'com.CricChat.intl', 'com.commsource.beautyplus',
                'com.meitu.beautyplusme', 'com.meitu.makeup', 
                'com.magicv.airbrush', 'com.meitu.meiyancamera', 
                'com.mt.mtxx.mtxx', 'com.meitu.oxygen', 
                'com.meitu.wheecam',  'app.buzz.share',
                'com.beautyplus.pomelo.filters.photo', 
                'com.meitu.airvid', 'com.meitu.meipaimv', 
                'cn.xender', 'club.fromfactory', 'com.miui.player',
                'app.buzz.share.lite', 'video.like', 
                'video.like.lite', 'com.kwai.video', 
                'com.romwe', 'com.zzkko', 'com.newsdog', 
                'com.yubitu.android.YubiCollage', 
                'com.apusapps.browser', 'com.quvideo.xiaoying', 
                'com.quvideo.vivavideo.lite', 'com.quvideo.slideplus', 
                'com.quvideo.xiaoying.pro', 'com.mi.global.bbs', 
                'com.DUrecorder.screenrecorder.videorecorde', 
                'com.mi.global.shop', 'com.DUsavebattery.faster.charge', 
                'com.DU.antivirus.cleaner.boosterpro', 
                'com.cyberlink.youcammakeup', 'com.mi.global.jointly', 
                'com.DUcalleradress.trackerlocation.callerid', 
                'com.DU.Cleaner.antivirus.cleanbooster', 'com.hcg.ctw.gp', 
                'com.hcg.cok.gp', 'com.netease.mail', 'com.tencent.wework', 
                'com.netease.mobimail', 'com.netease.buff163', 
                'com.miui.videoplayer', 'com.lbe.parallel.intl', 
                'com.parallel.space.pro', 'com.lbe.parallel.intl.arm64', 
                'com.parallel.space.lite', 'com.parallel.space.pro.arm64', 
                'com.parallel.space.lite.arm64', 'com.lbe.parallel.intl.arm32', 
                'com.parallel.space.lite.arm32', 'com.parallel.space.pro.arm32', 
                'com.lbe.camera.pro',  'com.lbe.knocktower', 
                'com.gamestudio.moveout', 'com.yy.hagolite', 'com.intsig.BCRLite',
                'com.intsig.lic.camscanner', 'com.intsig.notes', 
                'com.intsig.BizCardReader', 'com.intsig.camscannerhd', 
                'com.intsig.camocr', 'com.intsig.camcard.enterprise', 
                'com.intsig.BCRLatam', 'com.intsig.camcard.sfdc', 
                'sweet.facecamera.selfie', 'sweet.selfie.lite', 
                'photo.editor.filter.camera', 'best.sweet.selfie', 
                'instagramstory.maker.unfold', 'com.cam001.selfie361', 
                'sweet.snapface.facefilter', 'sweet.selfie.classic',
                'sweet.candy.camera', 'com.ai.ifly', 'com.miya.mobile', 
                'com.mi.globalbrowser', 'com.mi.globalbrowser.mini']

# constant running while loop
while True:
    # used a try block to handle all the errors
    try:
        # printing the main menu
        print('''\033[92m
            8888888b.           888      888                   888                    
            888  "Y88b          888      888     \033[96mBETA MODE\033[92m     888                    
            888    888          888      888                   888                    
            888    888  .d88b.  88888b.  888  .d88b.   8888b.  888888 .d88b.  888d888 
            888    888 d8P  Y8b 888 "88b 888 d88""88b     "88b 888   d8P  Y8b 888P"   \033[00m \033[94m
            888    888 88888888 888  888 888 888  888 .d888888 888   88888888 888     
            888  .d88P Y8b.     888 d88P 888 Y88..88P 888  888 Y88b. Y8b.     888     
            8888888P"   "Y8888  88888P"  888  "Y88P"  "Y888888  "Y888 "Y8888  888 \033[00m                                                                                       
        ''')

        print('\033[91mWarning: Please read the readme file before proceeding as careless handling of the software could lead to permanent damage to your device!!!')
        print('Proceed at your own risk I will not be responsible for anything happening. This is safe to run.\033[00m')
        print('\033[95m\nChoose an option to proceed.\033[00m')
        print('''   
        1. Fulfil Requirements
        2. Remove Chinese Apps
        3. Remove Apps of your Choice.
        4. Help
        5. About
        6. Exit
                    ''')
        
        option = int(input('Enter your choice: '))

        # Fulfiling requirements
        if option == 1:
            print('Checking all the requirements...')
            # choco is for checking installation of chocolatey command line PM for windows
            if reqSatisfied('choco') != True:
                # installation of chocolatey requires powershell so navigating to powershell on windows
                # C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe and using the command
                # Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
                subprocess.call(["C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe", "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"])
                print('\033[92mDone\033[00m')
            # adb is for Android Debug Bridge which is a most important tool for removing packages from the device
            if reqSatisfied('adb') != True:
                # chocolatey has adb so we can install it using
                # choco install adb
                subprocess.call('choco install adb')
                print('\033[92mDone\033[00m')

            if reqSatisfied('choco') == True and reqSatisfied('adb') == True:
                print('\033[92mAll the requirements are satisfied. You can proceed!\033[00m')
        
        # removing all the Chinese Apps
        if option == 2:
            print('''
            \033[91mWARNING: This option will remove all the chinese apps from you device.
            Proceed at your own risk. Please check the readme file for which all apps are getting removed.\033[00m''')
            
            # checking whether all requirements are satisfied
            if reqSatisfied('choco') == True and reqSatisfied('adb') == True:          
                # converting list to sets and using set theory to take common elements via intersection and 
                # assigning it a variable DELETE_APPS
                CHINESE_APPS_SET = set(CHINESE_APPS)
                DEVICE_APPS_SET = set(installedApps())
                # intersection will help in getting common packages
                DELETE_APPS = DEVICE_APPS_SET.intersection(CHINESE_APPS_SET)
                # if there are no chinese apps then the program will not show the option for proceeding 
                # else you will get the option for proceeding which will be final no further permission will be asked
                print('\033[91m{} \033[93mChinese Apps Detected\033[00m'.format(len(DELETE_APPS)))
                if len(DELETE_APPS) > 0:
                    proceed = input('\033[92mDo you want to proceed\033[00m [y/n]: ')
                    if proceed == 'y' or proceed == 'Y': # asking the final permission
                        print('\033[93mRemoving Chinese Apps...\033[00m')    
                        for delete in DELETE_APPS:
                            # using os.system function is better when merging the variable with the command
                            # it gets a bit complicated when we use subprocess.call function or any such other
                            print(delete)
                            os.system('adb shell pm uninstall --user 0 ' + delete)
                if len(DELETE_APPS) == 0:
                    print('\033[96mHurray! No Chinese Apps Detected\033[00m')

                    print('\033[92m{} Chinese Apps Successfully Deleted\033[00m'.format(len(DELETE_APPS)))                
            else:
                # if requiremets are not satisfied then you will get this message everytime
                print('\033[91mERROR: Requirements are not satisfied\033[00m')
        
        # removing apps of your choice. in this you will get the full list of packages installed on your device
        # along with every package there will be a number we just need to input the number and the rest will be handeled by the algorithm
        # the format will be <number>   <packageName>
        # this is very handy if you want to remove any specific app which you dont use but unable to remove directly.        
        if option == 3:
            print('''
            \033[93mSelect any App from the above list of Apps to remove any of you choice.
            See help section for further help
            Just Enter the number against the package name which you wish to remove\033[00m''')
            # checking the requirements
            if reqSatisfied('choco') == True and reqSatisfied('adb') == True:
                # adding a try block 
                try:    
                    # displaying in the format <number>     <packageName>
                    for pack in range(len(installedApps())):
                        print(pack, '\t', installedApps()[pack])
                    # only one package can be removed at once
                    packageNumber = int(input('\033[94mEnter Package Number: \033[94m\033[92m'))
                    # index of the number will be used to find the package and delete it
                    choice = input('\033[95mDo you want to proceed: [y/n] \033[92m')
                    if choice == 'y' or choice == 'Y':
                        os.system('adb shell pm uninstall --user 0 ' + installedApps()[packageNumber])
                        print('\033[00m')
                # except block to handle all the rest errors and terminate the program successfully
                except:
                    print('\033[91mTry Again or see Trouble Shooting\033[00m')
            
            else:
                # if requiremets are not satisfied then you will get this message everytime
                print('\033[91mERROR: Requirements are not satisfied\033[00m')

        # Help Option
        if option == 4:
            print('''
            \033[94mHaving some issues lets sort them out!!!
            Read the 'readme.txt' file for detailed instructions about the usage of this software.
            This software is very powerful. If not handled carefully it may cause damage to your
            device and you will need to FACTORY RESET your device.
            I have explained each function so please read the manual. 
            If you are having some issues then see the troubleshooting guide. If the issue still
            persists then contact me.\033[00m''')

        # About Option
        if option == 5:
            print('''
            \033[93mHello! I am Kanak Shilledar.
            If you want then you can contact me through the following:
            \tgmail: kanakshilledar111@gmail.com
            \tJoin Discord server for further help: https://discord.gg/jm8Sr5Z
            \tThis server will be specifically for discussion on this software.\033[00m ''')
        # Exit Option
        if option == 6:
            print('\033[94mExiting! Bye!\033[00m')
            break
        
        # Developer Options
        if option == 555:
            print('\033[91mDEVELOPER MODE SELECTED')
            print('\033[92mYou wish to send installed packages list to me\033[00m')
            with open('packagesList.txt', 'w') as packages:
                packages.write(installedApps()) 
            print('\033[92mThank You For Helping Me\033[00m')
    except:
        print('\33[91mInvalid Input\033[00m')    
