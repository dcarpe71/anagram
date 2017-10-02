git clone https://github.com/dcarpe71/anagram.git
cd anagram
cp tapp.py ttest.sh /usr/local/bin
cp web/index.html /var/www/html
cp /usr/share/dict/american-english /var/www/html/words
mkdir /var/www/html/cgi-bin
cp web/anagram_cgi.py /var/www/html/cgi-bin
