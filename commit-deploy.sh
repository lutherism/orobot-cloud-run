git add .
git commit . -m 'deploy'
git push origin master
gcloud config set project robots-gateway
cd src/run/orobot-cloud-run
printf '\ry\n' | gcloud run deploy --source ./src/run/orobot-cloud-run
