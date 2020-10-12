echo "Installing Dependencies..."
pip3 install tensorflow sklearn opencv-contrib-python flask flask-ngrok pil numpy scipy
echo "Downloading Data..."
git clone https://github.com/UCSD-AI4H/COVID-CT
cp COVID-CT/Images-processed/{CT_COVID.zip,CT_NonCOVID.zip} .
rm -rf COVID-CT
echo "Preprocessing The Dataset..."
unzip CT_COVID.zip
unzip CT_NonCOVID.zip
python3 create_dataset.py
echo "Extracting Features..."
python3 extract_features.py
echo "Running the Server..."
python3 server.py
