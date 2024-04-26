cd backend/backend/config
rm db.sqlite3
cd ../../..

git pull

docker-compose up --build -d