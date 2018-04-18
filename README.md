# ubuntu-wallpaper-changer
[Readme in English](https://github.com/estevaofon/ubuntu-wallpaper-changer/blob/master/README-ENGLISH.md)

Coloque os scripts no mesma pasta dos papeis de paredes.
E apenas execute o script para mudar o papel de parede
```bash
$ ./wallpaper.sh
```
Para mudar automaticamente o papel de parede a cada hora, vamos adicionar o script ao crontab
```bash
$ crontab -e 
```
Adicione a linha abaixo 
```bash
0 * * * * /path/to/wallpaper.sh > /tmp/wallpaper.log 2>&1
```
Você provavelmente também quer fazer um atalho para mudar o papel de parede. Para fazer isso escreva a linha seguinte no home/user/.bashrc
```bash
alias nextwall="/path/to/wallpaper.sh"
```
Tudo pronto! :)
