pip install -r requirements.txt


pip install psycopg2

echo "make migration...."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput


echo "collect static ...  "
python3 manage.py collectstatic --noinput --clear