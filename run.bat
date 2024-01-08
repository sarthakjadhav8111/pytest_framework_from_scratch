rem chrome
rem pytest -s -v -m "sanity and regression" --html=./reports/report1.html testCases/ --browser chrome
pytest -s -v -m "sanity or regression" --html=./reports/report1.html testCases/ --browser chrome
rem pytest -s -v -m "sanity" --html=./reports/report1.html testCases/ --browser chrome
rem pytest -s -v -m "regression" --html=./reports/report1.html testCases/ --browser chrome

rem edge
rem pytest -s -v -m "sanity and regression" --html=./reports/report1.html testCases/ --browser edge
rem pytest -s -v -m "sanity or regression" --html=./reports/report1.html testCases/ --browser edge
rem pytest -s -v -m "sanity" --html=./reports/report1.html testCases/ --browser edge
rem pytest -s -v -m "regression" --html=./reports/report1.html testCases/ --browser edge

