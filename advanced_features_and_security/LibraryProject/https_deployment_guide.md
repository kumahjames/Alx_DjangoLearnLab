<VirtualHost \*:80>

&nbsp;   ServerName yourdomain.com

&nbsp;   ServerAlias www.yourdomain.com

&nbsp;   Redirect permanent / https://yourdomain.com/

</VirtualHost>



<VirtualHost \*:443>

&nbsp;   ServerName yourdomain.com

&nbsp;   ServerAlias www.yourdomain.com



&nbsp;   # SSL Configuration

&nbsp;   SSLEngine on

&nbsp;   SSLCertificateFile /etc/letsencrypt/live/yourdomain.com/cert.pem

&nbsp;   SSLCertificateKeyFile /etc/letsencrypt/live/yourdomain.com/privkey.pem

&nbsp;   SSLCertificateChainFile /etc/letsencrypt/live/yourdomain.com/chain.pem



&nbsp;   # Security Headers

&nbsp;   Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"

&nbsp;   Header always set X-Frame-Options "DENY"

&nbsp;   Header always set X-Content-Type-Options "nosniff"

&nbsp;   Header always set X-XSS-Protection "1; mode=block"

&nbsp;   Header always set Referrer-Policy "same-origin"



&nbsp;   # Django Application

&nbsp;   WSGIDaemonProcess libraryproject python-path=/path/to/your/project

&nbsp;   WSGIProcessGroup libraryproject

&nbsp;   WSGIScriptAlias / /path/to/your/project/LibraryProject/wsgi.py



&nbsp;   # Static Files

&nbsp;   Alias /static/ /path/to/your/static/files/

&nbsp;   <Directory /path/to/your/static/files>

&nbsp;       Require all granted

&nbsp;   </Directory>



&nbsp;   # Media Files

&nbsp;   Alias /media/ /path/to/your/media/files/

&nbsp;   <Directory /path/to/your/media/files>

&nbsp;       Require all granted

&nbsp;   </Directory>

</VirtualHost>

