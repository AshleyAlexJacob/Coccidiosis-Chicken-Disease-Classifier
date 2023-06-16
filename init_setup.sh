echo "[ `date` ]": "START"
echo "[ `date` ]": "Creating Python Environment" 
python -m venv venv/
echo "[ `date` ]": "activate venv"
source venv/bin/activate
echo "[ `date` ]": "installing the requirements" 
pip install -r requirements.txt
echo "[ `date` ]": "END" 