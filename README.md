# Usafe——U盘防丢程序
Just in case that your flash disk is lost.<br>
每次插入电脑时，自动发送主机名、MAC地址，内外网IP到指定邮箱。其中外网IP可用于较精确的定位（见ip138）
### Initial
I got my flash disk lost two weeks ago. Some important data was in it and, to be honest, that flash disk was of good quality. And I was kind of annoyed because it should be left in the print shop in our campus with a high probability, but no one came to return it even if I tried my best to post notifications to look for it. <br>
I believe there would be few people who would take things which others lost as their own. But I gave up looking for it and bought a new one (same to the old). And just in case, I wrote this program.
### Explaination
`usafe.py` record the hostname, MAC address, intranet and internet IP address of the host, and send these infomation to your Email address (with the help of SMTP).<br>
`myAES.py` I used AES to encrypt those info in email. Mostly for the afraid of Program Reverssing which would leak the username and password of the sender's email, and here the address I used was bought on the internet with 0.02 RMB, so it could be unsafe if too many private data are recorded. 
<br><br>
`autorin.inf` you can use `pyinstaller` to pack Usafe. This file will autorun usafe.exe (in Windows) when the flash disk is put into use.<br>
If using other operating systems, there might be other ways or not. But still, with the concept of Social Engineering in Information Security, maybe we could rename the application as something like <u>click to reset all</u> to incur the startup we want.
### In the end
However, I still hope there will be little chance for the program to give its value.<br>
What's more, encryptions and backups are also very important.
