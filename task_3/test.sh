
echo "TESTING NGINX\n"
ab -n $1 -c $2 -k 127.0.0.1:8080/images/image_1.jpg
echo "-----------------------------------\n"

echo "TESTING GUNICORN\n"
ab -n $1 -c $2 -k 127.0.0.1:8000/
echo "-----------------------------------\n"

echo "TESTING NGINX + GUNICORN\n"
ab -n $1 -c $2 -k 127.0.0.1:8080/api/
echo "-----------------------------------\n"