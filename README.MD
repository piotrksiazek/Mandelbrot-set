# Opis
program jest wizualizacją zbioru Mandelbrota, który tworzą te
punkty, dla których ciąg rekurencyjny dla płaszczyzny zespolonej 
  
z_0 = 0  
z_(n+1) = z^2_n + p  
  
nie dąży do nieskończoności.

# Instrukcja uruchomienia
Aby wystartować program należy zainstalować zależności  
pip3 install -r dependencies  
  
a następnie uruchomić poleceniem  
python3  main.py

# Instrukcja korzystania
Po załadowaniu się pierwszego obrazu można zrobić kilka rzeczy:  
1. Zoomowanie - wybieramy myszą lewy dolny róg nowego obszaru a następnie prawy górny róg.
Po drugim kliknięciu zostanie wyrysowany nowy obszar.
2. Za pomocą strzałek lewo-prawo zwiększamy liczbę maksymalnych iteracji. Im więcej, tym bardziej szczegółowy będzie obraz.
3. Za pomocą strzałek góra-dół zmieniamy szybkość zmiany maksymalnych iteracji.