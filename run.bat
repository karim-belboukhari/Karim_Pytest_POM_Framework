@echo off
pytest -v --alluredir=report/allure-results
allure generate report/allure-results -o report/allure-report --clean
allure open report/allure-report
