# Всероссийский хакатон по биометрии 2024
# Кейс: Создание инструмента для генерации синтетического датасета изображений ладоней
<a name="readme-top"></a>
<p align="center">  
<img width="30%" src="./images/photo_2024-10-06_07-08-13.jpg" alt="banner">
</p>
  <p align="center">
    <!--<h1 align="center">LLAIM</h1>-->
  </p>
  <p align="center">
    <p></p>
    <!-- <p><strong>Интеллектуальный пульт составителя.</strong></p> -->

  </p>
</div>

**Содержание:**
- [Проблематика задачи](#title1)
- [Описание решения](#title2)
- [Тестирование решения](#title3)

### Разработан в рамках [Всероссийский хакатон по биометрии 2024](https://biometricshack.ru/) командой "Сборная 1".

### Live версия доступна [тут](https://t.me/rosatom_support_bot)

## <h3 align="start"><a id="title1">Проблематика задачи</a></h3> 

### Поиск по неструктурированным данным (вопросы из документации в виде pdf)


Поиск информации по заданной тематике на основе неструктурированных данных (текста).

----

### Поиск по структурированным данным (схожие вопросы на основе истории обращений)


Поиск информации по заданной тематике на основе структурированных данных (таблицы).

----

## <h3 align="start"><a id="title2">Описание решения</a></h3>

<img src="./resources/photo_2024-06-16_08-42-59.jpg" alt="Архитектура решения" width="700"/>

* Шумоподавление 
* ASR Wave2vec
* Поиск команды из заданного набора в тексте
* Вывод в формате .json
 
### Структура проекта

```
├── app # основная директория проекта
│   ├── utils # содержит утилиты для работы проекта
│   ├── main_app.py # тг бот
│   ├── chat_bot.py # файл ответов на вопросы в формате excel
│   ├── app.ipynb # demo бота с gradio
├── data # содержит данные и БД для проекта, а также тестовые вопросы
├── README.md
├── requirements.txt
└── resources # ресурсы проекта
```

## <h3 align="start"><a id="title3">Тестирование решения</a></h3> 

## Development

0. Install requirements

```
pip install -r requirements.txt
```





## Palm image generation images with unconditional latent diffusion

original repository for train ddpm [repository](https://github.com/zyinghua/uncond-image-generation-ldm.git)

### Cloning to local
```bash
git clone https://github.com/Yagorka/ddpm_ema_512.git
```
Then call:
```bash
cd ddpm_ema_512
```
### Installing the dependencies
Before running the scripts, make sure to install the library's training dependencies:
```bash
pip install -r requirements.txt
```

### Generate images
```bash
python gen.py dir_name number_image
```
dir_name - dir for save generated images

number_images - number images for generation


