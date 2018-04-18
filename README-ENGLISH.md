# ubuntu-wallpaper-changer
Place the scripts at the same folder of your wallpapers images.
Then just run the bash script to change the wallpaper
```bash
$ ./wallpaper.sh
```
To change automatically the wallpaper every hour, let's add the script to crontab
```bash
$ crontab -e 
```
Add the following line, 
```bash
0 * * * * /path/to/wallpaper.sh > /tmp/wallpaper.log 2>&1
```
You probaly also want to make an alias to change the wallpaper. To do this write the following line to .bashrc
```bash
alias nextwall="/path/to/wallpaper.sh"
```
All set! :)
