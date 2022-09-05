git add .
git commit . -m 'deploy'
git push origin master
gcloud config set project robots-gateway
cd src/run/orobot-cloud-run
printf 'y\n' | gcloud run deploy
