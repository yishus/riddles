### Title: Enter Space-Time Coordinates

Description: Ok well done. The console is on. It's asking for coordinates. Beating heavily on the console yields little results, but the only time anything changes on your display is when you put in numbers.. So what numbers are you going to go for?  You see the starship's logs, but is there a manual? Or should you just keep beating the console?Ok well done. The console is on. It's asking for coordinates. Beating heavily on the console yields little results, but the only time anything changes on your display is when you put in numbers.. So what numbers are you going to go for?  You see the starship's logs, but is there a manual? Or should you just keep beating the console?

Attachment:

**log.txt**
```
0: AC+79 3888{6652492084280_198129318435598}
1: Pliamas Sos{276116074108949_243544040631356}
2: Ophiuchus{11230026071572_273089684340955}
3: Pax Memor -ne4456 Hi Pro{21455190336714_219250247519817}
4: Camion Gyrin{235962764372832_269519420054142}
```

**rand2**

I tried running `rand2` as an executable and got this
```
Failed to execute process './rand2'. Reason:
exec: Exec format error
The file './rand2' is marked as an executable but could not be run by the operating system.
```

Checking on the file type with `file ./rand2`
```
./rand2: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=0208fc60863053462fb733436cef1ed23cb6c78f, not stripped
```

Docker it is. (a barebone setup, also included in this repo)

Finally got around to executing `rand2`

```
Travel coordinator
0: AC+79 3888 - 34406653720322, 177528345282932
1: Pliamas Sos - 21235446713534, 184184763712505
2: Ophiuchus - 206830308424617, 243269057047278
3: Pax Memor -ne4456 Hi Pro - 101561731958443, 225576844846119
4: Camion Gyrin - 18923689341948, 233950498404807
5: CTF - <REDACTED>
```

Giving a random pair of coordinates 

```
Enter your destination's x coordinate:
>>> 18923689341948  
Enter your destination's y coordinate:
>>> 233950498404807
Arrived somewhere, but not where the flag is. Sorry, try again.
```

With the correct pair of coordinates, the flag will be printed.

_Printed_

Let's use `strings` to look into all the printable strings in the executable.

`strings ./rand2`

```
...
Arrived at the flag. Congrats, your flag is: CTF{welcome_to_googlectf}
...
```

---

Flag:`CTF{welcome_to_googlectf}`
