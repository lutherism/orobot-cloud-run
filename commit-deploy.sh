git add .
git commit . -m 'deploy'
git push origin master
gcloud config set project robots-gateway
cd src/run/orobot-cloud-run
printf '\ry\n' | gcloud run deploy orobot-cloud-run --region us-central1 --source ./src/run/orobot-cloud-run
