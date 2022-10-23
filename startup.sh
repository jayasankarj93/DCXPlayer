echo ">> FETCHING UPSTREAM..."
git clone https://github.com/jayasankarj93/DCXPlayer
echo ">> INSTALLING REQUIREMENTS..."
cd /DCXPlayer 
pip3 install -U -r requirements.txt
echo ">> STARTING MUSIC PLAYER USERBOT..."
clear
echo "
MUSIC PLAYER USERBOT IS SUCCESSFULLY DEPLOYED!
"
python3 main.py
