# Всероссийский хакатон по биометрии 2024
# Кейс: Создание инструмента для генерации синтетического датасета изображений ладоней
<a name="readme-top"></a>
<p align="center">  
<img width="100%" src="./images/Снимок экрана от 2024-10-13 01-10-04.png" alt="banner">
</p>
  <p align="center">
    <!--<h1 align="center">Сборная 1</h1>-->
  </p>
  <p align="center">
    <p></p>
    <!-- <p><strong>Генерация ладоней.</strong></p> -->

  </p>
</div>

**Содержание:**
- [Проблематика задачи](#title1)
- [Описание решения](#title2)
- [Тестирование решения](#title3)

### Разработан в рамках [Всероссийский хакатон по биометрии 2024](https://biometricshack.ru/) командой "Сборная 1".

### Live версия доступна [тут](https://t.me/rosatom_support_bot)

## <h3 align="start"><a id="title1">Проблематика задачи</a></h3> 

### Описание кейса

Описание: разработать метод генерации изображений ладони, которые могут быть использованы для тренировки моделей аутентификации клиентов. Датасет должен обладать достаточной полнотой и разнообразием, необходимыми для обучения.
Для генерации датасета можно выбрать обученную open source модель или разработать собственную. Базу данных реальных изображений ладоней для дальнейшей работы нужно подготовить самостоятельно

Предусмотреть возможность управления генерацией задавая цвет кожи, наличие аксессуаров, шрамов и т.д.

#### Задачи
* инструмент, который позволяет генерировать синтетические изображения ладоней с пальцами
* возможность инструмента генерировать несколько разных изображений ладоней с пальцами,
принадлежащих одному синтетическому индивиду
* предложения по дальнейшему использованию и улучшению созданного синтетического датасета
для задач машинного обучения


### Датасет
* Открытый [датасет](https://biometricshack.ru/) (5397 подходящих изображений)
* Собранный датасет из открытых источников (7833 изображений)
* Отчищенный датасет с удаленным фоном и поворотом ладони перпендекулярно листу (7000 обучение, 700 тест)

## <h3 align="start"><a id="title2">Описание решения</a></h3>

### Контролируемая генерация

#### Stable Diffusion 1.5 
* Unet 
* ASR Wave2vec
* Поиск команды из заданного набора в тексте
* Вывод в формате .json

### Неконтролируемая генерация

#### ProGan

#### DDPM
 
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


