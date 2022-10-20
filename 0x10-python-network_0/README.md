
nstalls a Nginx server
0x10-python_network_0
In this project I learnt about:

What a URL is
What HTTP is
How to read a URL
The scheme for a HTTP URL
What a domain name is
What a subdomain is
How to define a port number in a URL
What a querry staring is
WHat a HTTP request is
What an HTTP response is
What HTTP headers are
What the HTTP message body is
What an HTTP request method is
What an HTTP response status code is
What an HTTP Cookie is
How to make a request with cURL
What happens when you type google.com in your browser (Application level)
Resources used
developer.mozilla.org
www3.ntu.edu.sg

exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt install nginx -y ; echo "Hello World!" | sudo tee /var/www/html/index.html ; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/VicNW permanent;/" /etc/nginx/sites-available/default ; sudo service nginx start',
}
