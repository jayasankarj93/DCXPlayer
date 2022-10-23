echo ">> FETCHING UPSTREAM..."
git clone https://github.com/sakhaavvaavaj9saDCXPlayer /DCXPlayer 
echo ">> INSTALLING REQUIREMENTS..."
cd /DCXPlayer 
pip3 install -U -r requirements.txt
echo ">> STARTING MUSIC PLAYER USERBOT..."
clear
echo "
MUSIC PLAYER USERBOT IS SUCCESSFULLY DEPLOYED!
"
python3 main.py
