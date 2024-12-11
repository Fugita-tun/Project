 FROM	ubuntu:latest
 #	Устанавливаем	рабочую	директорию
 WORKDIR	/web
 #	Копируем	файл	зависимостей
 COPY	requirements.txt	.
 #	Устанавливаем	зависимости

 RUN    apt update -y
 RUN    apt install -y python3 pip
 RUN	pip	install	--no-cache-dir	--break-system-packages -r	requirements.txt
 #	Копируем	остальной	код	приложения
 COPY	.	.
 #	Указываем	переменные	окружения
 ENV	PYTHONUNBUFFERED	1
 #	Открываем	порт,	который	будет	использоваться	приложением
 EXPOSE	8000
 #	Определяем	команду	для	запуска	приложения
 CMD	["python3",	"proga.py"]
