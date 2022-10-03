# scorpio_zadanie_software

Zadanie wykonane w ramach rekrutacji do działu software Projektu Scorpio

Cały program został napisany w Pythonie 

Do pozyskania informacji o statusie elementów takich jak procseor czy wykorzystanie interfesjów sieciowych została użyta biblioteka psutil
(https://psutil.readthedocs.io/en/latest/) zaimportowana w programie jak "psu"

Program wyświetla i zapisuje w pliku system_data_readings.txt wszystkie podane w zadaniu parametry

Do zautomatyzowania działania programu oraz jego został użyty crontab - "@reboot python3 ~/zadanie_Scorpio.py &" - w wyniku użycia crontab plik z danymi
pojawia się i aktualizuje w głównym katalogu systemowym (W przypadku RPi OS jest to ścieżka "/home/pi")

W repozytorium znajduje się również przykładowy plik zawierający tabelę crontab

Cały projekt wykonany na systemie Raspberry Pi OS 
