set root=C:\ProgramData\Anaconda3
call %root%\Scripts\activate.bat
call activate pycaretenv
call cd "C:\Users\m4005001\Documents\_SG\Pessoal\FIAP\Aula06_20230317\deploy"
call streamlit run "app_pycaret.py" --theme.base="light"
PAUSE