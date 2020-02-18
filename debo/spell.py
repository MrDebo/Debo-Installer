import os, sys

print ("\033[1;32mMasukin Username&Password!")
print ("\033[1;31;1mGa Tau, Bisa Contact Mr.Debo =>> 081539279932")
Username = 'Paksu'
Password = 'Buis'

def restart():
        ngulang = sys.executable
        os.execl(ngulang, ngulang, *sys.argv)

def main():
        uname = raw_input("Username : ")
        if uname == Username:
                pwd = raw_input("Password : ")

                if pwd == Password:
                        sys.exit()

                else:
                        print "\n\033[1;36mSorry Invalid Password!\033[00m"
                        print "Contact Mr.Debo\n"
                        restart()
        else:
                print "\n\033[1;36mSorry Invalid Username!\033[00m"
                print "Contact Mr.Debo\n"
                restart()

try:
        main()
except KeyboardInterrupt:
        os.system('clear')
        restart()
