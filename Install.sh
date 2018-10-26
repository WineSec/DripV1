# Installer for DripV1 
# Any problems contact @WineSec on instagram

echo "installing dependancys hold on"
sleep 1.5
sudo apt-get update 
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo dnf install python3
sudo apt-get install python3.6
sudo apt-get install zenmap
sudo apt-get install mysql server
echo "installed main dependancys hopefully"
sleep 0.5
sudo pip install termcolor 
# Open pip install space
# Open pip install space
# Open pip install space
# Open pip install space
# Open pip install space
echo "Installed all python modules"
cls
clear
python3 --version
echo "if python3 is not installed please do this manually before continuing"
sleep 3
cd Desktop
git clone https://github.com/WineSec/DripV1.git
cd DripV1
sudo chmod 777 *
clear
echo "Installation done"
./DripV1
