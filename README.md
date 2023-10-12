CheckVPN.py: The VPN Guardian 🛡️

Hey there, DevOps aficionado! 

Are you tired of your VPN acting like a rebellious teenager, disconnecting whenever it feels like it? Say hello to CheckVPN.py, the digital chaperone for your VPN connection. It's like a watchdog, but for adults who need to get work done.

# Pre-requisites 📋

1. Python: You'll need Python 3.x. If you're still on Python 2, what are you doing?
2. You will also need to install pip for python and install smtplib and socket library so that you can use them in your code.
3. SMTP Email Account: You'll need an email account that allows SMTP. We've used Gmail here because, well, it's free!
4. A Sense of Humor: Because life's too short to read boring READMEs ;)

# How to Run 🏃‍♂️

Clone this repo: git clone https://github.com/YourUsername/CheckVPN.git

Navigate to the directory: cd ../CheckVPN

Install any dependencies: Just kidding, we like to keep it simple. No dependencies here! (assuming you followed my instructions and installed smtplib and socket libraries)

Update the email info: Open CheckVPN.py and replace the placeholder email and password. Please, for the love of all that's holy, use a secure app password.

Run the script: python3 CheckVPN.py

All right, so you should get some nice output telling you " Successfully connected to <HOST> <PORT>" if succesfull and "Failed to connect to <HOST> <PORT>" if unsuccesfull.

#How to install it as a Service - Using Supervisor & Systemd on Linux

There are quite a few ways to accomplish this, I will emphasis on Two methods - using Supervisorctl  & Systemd on Linux (because real programmers use the Linux files system, yes, I said it!)
    
## Method 1 - Supervisor
1. Install supervisor
   In Ubuntu, this can be accomplished using the "sudo apt-get update && sudo apt install supervisor" command, on CentOS use "sudo yum install epel-release && sudo yum install supervisor"

2. You now have Supervisor installed, you will need to configure it so as to create an entry for your program. Run the following commands as sudo (with great powers cometh great responsibiliteth)

   sudo nano /etc/supervisor/conf.d/checkVpn.conf

   Add the following content to the configuration file and save it.

    [program:checkVpn]
    command=/usr/bin/python3 /srv/monitoring/checkVpn.py
    autostart=true
    autorestart=true
    stderr_logfile=/srv/monitoring/logs/checkVpn.err.log
    stdout_logfile=/srv/monitoring/logs/checkVpn.out.log

    A quick gloassary for the configuration options above;

   command: The command to run your Python script. (My script is called checkVpn.py and is located on the path /srv/monitoring)
   autostart: The service will start when Supervisor starts.
   autorestart: The service will restart automatically if it exits. (The program will restart whenever there is a fail condition)
   stderr_logfile and stdout_logfile: Paths to the log files. (In case you require an Error log and output log, define these and ensure that the files exist.)

   After saving the configuration file, update Supervisor to read the new configuration:


   sudo supervisorctl reread
   sudo supervisorctl update
   You can then start your service:


   sudo supervisorctl start checkVpn

 ## Method 2 - Systemd

   Ah, "systemd", the init system that people either love to love or love to hate.
   It's like the pineapple on pizza of the Linux world. Jokes aside, systemd is an init system used in Linux distributions to     
   bootstrap the user space and manage system processes.

   Ubuntu comes with systemd pre-installed, so you usually don't need to install it. If for some reason it's not there (did you time-travel to 2009?), you can install it with:


   sudo apt-get update
   sudo apt-get install systemd

   Create a Systemd Service file

   sudo nano /etc/systemd/system/checkVpn.service

   Paste the following content below:

   [Unit]
   Description=The Guardian of the VPN Galaxy
   After=network.target

   [Service]
   ExecStart=/usr/bin/python3 /srv/monitoring/checkVpn.sh
   WorkingDirectory=/srv/monitoring
   StandardOutput=append:/srv/monitoring/logs/checkVpn.log
   StandardError=append:/srv/monitoring/logs/checkVpn_error.log
   Restart=always

   [Install]
   WantedBy=multi-user.target

   Save the file.

   Enable and Start the Service 🚀
   Now, let's reload the systemd daemon and enable your service:

   sudo systemctl daemon-reload
   sudo systemctl enable checkVpn.service
   
   To start the service:
   sudo systemctl start checkVpn.service

   I have used nano for editing most of the configuration files above, if your preference is vim, please go ahead and substitute nano with vim.
   
# Checking Logs 🌳

You can check the logs at /srv/monitoring/logs/checkVpn.err.log for errors and /srv/monitoring/logs/checkVpn.out.log for standard output.

Sit back and relax: Your VPN is now under surveillance. Any funny business, and you'll get an email.

# Debugging 🐛

No Emails: If you're not getting emails, first check if you've entered the correct "secure app password". If you've used your regular password, you're just asking for trouble.

False Alarms: If you're getting false alarms, consider increasing the timeout in the check_connection function. Maybe your VPN is just a slow 🐌.

Still Stuck?: Try turning it off and on again. No, seriously, sometimes it works.



