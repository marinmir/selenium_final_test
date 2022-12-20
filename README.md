# the_final_task_for_stepik
1. тесты запускаются из корневой директории, это директория the_final_task_for_stepik
2. тесты можно запустить командой pytest -v --tb=line --language=en -m need_review 
3. для добавления стабильности тестам исмользуется команда --reruns:
    pytest -v --tb=line --language=en -m need_review --reruns=5
4. все локаторы в папке locators

Для запуска тестов необходимо:
1. Скопировать репозиторий через SHH (git clone)
2. Загрузите chromedriver для вашей операционной системы и соответствующую версию
и поместите ее в переменную PATH.
3. Создайте виртуальную среду и войдите в нее(
win:python -m venv venv, venv/Scripts/activate, linux: python -m ven ven, source venv/bin/activate)
4. Загрузите все модули в виртуальную среду (pip3 install -r requirements.txt )
5. Для генирации отчетов в Allure понадобится дополительно установка:
Allure документация по установке 
    Windows: https://docs.qameta.io/allure-report/#_installing_a_commandline
https://github.com/ScoopInstaller/Scoop
    Linux: wget https://github.com/allure-framework/allure2/releases/download/2.19.0/allure-2.19.0.tgz
sudo tar -zxvf allure-2.19.0.tgz -C /opt/ 
sudo ln -s /opt/allure-2.19.0/bin/allure /usr/bin/allure
OpenJDK документация по установке 
    Windows: https://learn.microsoft.com/ru-ru/java/openjdk/download
https://docs.oracle.com/cd/E19182-01/820-7851/inst_cli_jdk_javahome_t/
    Linux: sudo apt install default-jre -y
6. Тесты выполняются из корневой дириктории командой: pytest -v -s --alluredir=/reports
7. Просмотреть отчет: allure serve /reports
