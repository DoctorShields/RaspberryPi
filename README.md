# RaspberryPi

## Python Program 01 – Calculator

What I did

## Python Program 02 - Quadratic solver

What I did

<a href="https://google.com" target="_blank">Here's a link</a>

## wpa_supplicant.conf

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=us

network={
      ssid="MyNetworkSSID"
      psk="Pa55w0rd1234"
}
```

## Prompt is too long

`sudo nano ~/.bashrc`

Find the if [ "$color_prompt" = yes] line.  Below that, edit the PS1 variable.

Change the last w to a capital W

## Run at startup

`sudo nano /etc/rc.local`

Above the exit 0 line, add 

`python3 /home/pi/Documents/[path to your file]/myscript.py &`

Don't forget the ampersand

## Colors in terminal

`sudo nano /etc/profile`

Then, add at the end:

`export TERM=xterm`
