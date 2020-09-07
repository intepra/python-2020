# Инструкция по настройке окружения и сдаче заданий

<details><summary><b>Настройка окружения</b></summary>

### Регистрация
Для начала нужно зарегистрироваться [на GitHub](github.com).

Далее вы заходите на [репозиторий курса на GitHub](https://github.com/ismc-spbu-courses/python-2020), где переходите по ссылке соотвествующего домашнего задания. Автоматически создаётся ваш личный репозиторий для решения этого задания.

### Добавление ssh-ключа
Рекомендуем [добавить публичный ssh-ключ](https://git-scm.com/book/ru/v2/GitHub-Настройка-и-конфигурация-учетной-записи) в настройках профиля на GitHub.

#### Создание ключа
Для того чтобы сгенерировать ssh-ключ, вам нужно, в зависимости от системы, сделать следующее:

##### **Windows**
В Windows 10 появилась такая фича как WSL: Windows Subsystem for Linux, с её помощью можно запускать Linux-приложения на Windows. Мы рекомендуем воспользоваться ею, и в дальнейшем следовать инструкциям, как будто бы у вас стоит операционная система Linux. Если вы не уверены в своих силах (или у вас старая версия Winodows), то можете воспользоваться вариантом инструкции без WSL.

<details><summary><a>Как настроить WSL?</a></summary></br>
Оффициальная инструкция
https://docs.microsoft.com/ru-ru/windows/wsl/install-win10

При выборе операционной системы Linux берите Ubuntu 16.04 или 18.04.

Переходите к инструкции про генерацию ключа на Linux.
</details>

<details><summary><a>Вариант без WSL (сложнее)</a></summary></br>
Вам нужно будет [установить Putty и сгенерировать ключ с помощью PuTTYgen](https://docs.joyent.com/public-cloud/getting-started/ssh-keys/generating-an-ssh-key-manually/manually-generating-your-ssh-key-in-windows)

В этой инструкции вам нужны **только** пункты "About PuTTY" и "Generating an SSH key", после чего ключ будет уже скопирован.

Переходите к пункту про добавление ключа.
</details>

##### **Linux** или **MacOS**
В консоли воспользуйтесь `ssh-keygen`, затем копируйте **.pub** ключ:

```bash
ssh-keygen -t ed25519 -f ~/.ssh/python_ed25519  # создаем ключ c типом ed25519, можно взять более стандартный rsa, но это более старый алгоритм
# Обратите внимание, что вы можете не вводить пароль для ключа, это стандартная практика, хотя и не очень безопасная,
# чтобы не приходилось его потом вводить на каждое действие c ключом
cat ~/.ssh/python_ed25519.pub  # выводим содержимое **публичного** ключа в консоль
                                 # его надо просто скопировать, как есть, включая подпись - обычно это "ваш-логин@имя-устройства"
# Публичным ключом можно делиться, приватным (то же имя, без .pub на конце) - никогда, иначе злоумышленник сможет представиться вами
```

<details><summary><a>Картинка</a></summary><img src="https://i.imgur.com/FMHgxsL.png" width=800/></details></br>

#### Добавление ключа на GitHub

Идете на [GitHub](https://github.com), находите в правом верхнем углу иконку с вашим профилем.

Нажимаете на неё -> `Settings` -> слева выбираете `SSH and GPG keys`.

Здесь нопка New SSH key, вставляете ключ в формочку и нажимаете на "Add key".

<details><summary><a>Картинка</a></summary><img src="https://i.imgur.com/CSPBoGp.png" width=800/></details></br>

<details><summary><a>Как проверить себя?</a></summary></br>
Из консоли выполнить:
```bash
ssh git@github.com
```
(Если у вас Windows без WSL, то нужно воспользоваться PuTTY для проверки)

Вывод должен быть примерно таким:
```
PTY allocation request failed on channel 0
Hi avalur! You've successfully authenticated, but GitHub does not provide shell access.
Connection to github.com closed.
```
</details>

### Клонирование и настройка репозитория

#### Установка git
О том, что такое гит, и как вообще с ним работать, будет рассказано на втором занятии. Очень хорошая [подробная презентация](https://docs.google.com/presentation/d/1IQCRPHEIX-qKo7QFxsD3V62yhyGA9_5YsYXFOiBpgkk/mobilepresent).

##### **Windows без WSL**

Вы можете скачать гит отсюда: https://gitforwindows.org.

При установке на одном из этапов вам будет предложено выбрать текстовый редактор для работы с гитом.
Если вы умеете пользоваться vim, оставьте его, иначе смените на что-нибудь более привычное и удобное.

##### **MacOS**

Вы можете скачать установщик по ссылке: https://git-scm.com/download/mac

P.S. Можно поставить через [brew](https://brew.sh), если вы с ним знакомы.

##### **Linux или WSL**
С некоторой вероятностью гит уже даже стоит, проверить можно так: `git --version`.

Если не стоит, и у вас Ubuntu/Debian, то всё просто:
```bash
sudo apt-get install git
```

Если у вас другой дистрибутив, то думается, вы и сами знаете, как в нем поставить пакет.

#### Клонирование и настройка репозитория

Выбираем директорию, где будут лежать задачи, откуда вам будет удобно с ними работать.

- На Linux это может быть `~` - домашняя директория (обычно `/home/<username>`)
- На MacOS аналогично, но полный путь будет `/Users/<username>`
- На Windows без WSL, когда вы запускаете т.н. GitBash вы оказываетесь в директории `C:\Users\<username>`, возможно, вам стоит перейти в `C:\Users\<username>\My Documents` для упрощения поиска файлов задач из Проводника.
- Для WSL при входе вы оказываетесь в директории `/home/<username>`, которая в самой windows доступна по адресу `\\wsl$\<ubuntu-version>\home\<username>`

```bash
# Переходим в директорию, где разместится директория с задачами
cd <выбранная вами директория>
# Клонируем себе репозиторий с задачками
git clone git@github.com:ismc-spbu-courses/hw-1-avalur.git
# или
git clone https://github.com/ismc-spbu-courses/hw-1-avalur.git

# Переходим в директорию с задачами
cd hw-1-avalur
# Настраиваем гит так, чтобы он знал нас "в лицо"
git config --local user.name "<ваш логин с github.com>"
git config --local user.email "<ваш емейл с github.com>"

```

### Установка интерпретатора python и необходимых инструментов

#### Установка интерпретатора

Мы используем довольно новую версию питона: 3.7.3.

Есть простой способ её установить: скачиваете [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

##### **Windows (с или без WSL)**
Запустите скачанный установочный файл

После установки запустите "Anaconda Prompt" и выполните:
```bash
conda install python=3.7.3
```
В конце наберите `exit`, чтобы закрыть окно.

##### **MacOS**
Запустите скачанный установочный файл

В консоли выполните:
```bash
conda activate  # Для деактивации достаточно выполнить команду `conda deactivate`
conda install python=3.7.3
```

##### **Linux**
Запустите установку:
```bash
$ bash ./Miniconda3-latest-Linux-x86_64.sh
...

Do you wish the installer to initialize Miniconda3
by running conda init? [yes|no]
[no] >>> yes
...

Thank you for installing Miniconda3!
```

Можно отключить у себя автоматическую активацию виртуального окружения:
```bash
$ conda config --set auto_activate_base false
```
Затем перезапустите терминал, чтобы изменения применились.

Установите нужную версию питона:
```bash
conda activate  # Для деактивации достаточно выполнить команду `conda deactivate`
conda install python=3.7.3
```

<details><summary><a>Сложный способ без Anaconda через консоль</a></summary></br>

- Поставьте [pyenv](https://github.com/pyenv/pyenv#installation)

- Установите нужную версию питона
```bash
pyenv install 3.7.3
```

- Установите virtualenv
```bash
pip install virtualenv
```

Разверните виртуальное окружение с нужной версией питона в репозитории с задачами
```bash
cd <путь к директории с задачами>
virtualenv --python=`realpath ~/.pyenv/versions/3.7.3/bin/python` venv
```

В след. пункте инструкции в меню "Project interpreter" укажите "Existing interpreter" и путь до интерпретатора `.../venv/bin/python`
</details>

#### Установка и настройка IDE

Мы рекомендуем вам воспользоваться [PyCharm](https://www.jetbrains.com/pycharm/download/).
Скачайте бесплатную Community-версию, установите и запустите.

- Создайте новый проект (Create new project)
- Укажите путь до репозитория с задачами (см. пункт "Клонирование и настройка репозитория")
- Разверните меню "Project interpreter", выберите "Existing interpreter"
- Укажите путь до установленной анаконды, для этого выполните в консоли:
```bash
conda info --base
```
и допишите к полученному пути `bin/python`
- Подтвердите создание проекта

#### Установка пакетов для тестирования

Необходимо поставить:
- pytest версии 5.1.2 - для тестирования
По желанию:
- flake8 версии 3.7.8 - для проверки на кодстайл
- mypy версии 0.720 - для проверки типов

Вы можете поставить необходимые пакеты через консоль, аналогично тому, как вы ставили нужную версию питона:
```bash
conda install -c conda-forge pycodestyle==2.4.0 pytest==3.7.3
```

<details><summary><a>Вариант без Anaconda</a></summary></br>

Активируйте виртуальное окружение:
```bash
cd <путь к директории с задачами>
source venv/bin/activate
# Для деактивации достаточно выполнить команду `deactivate`
```

Установите необходимые пакеты:
```bash
pip install --upgrade pycodestyle==2.4.0 pytest==3.7.3
```
</details>

Проверьте версии:
```bash
$ python --version
Python 3.7.3
$ pytest --version
This is pytest version 3.7.3, ...
$ pycodestyle --version
2.4.0
```

</details>
<br/>
<details><summary><b>Сдача заданий</b></summary>

Для получения новых заданий надо делать `git pull`. Для локального тестирования кода используется библиотека `pytest` (см. выше установку).

Код относящийся к отдельной задаче находится в отдельной директории
(`hw-1-avalur` и т.д.). Там же находится условия задач
(`hw-1-avalur/1_middle_value_of_triple/README.md`).

```bash
# Переходим в задачу
$ cd hw-1-avalur/1_middle_value_of_triple

# Пишем код в файле 1_middle_value_of_triple.py, реализовывая заданный интерфейс

# Запускаем юниттесты
1_middle_value_of_triple$ pytest .

# Проверяем код-стайл
1_middle_value_of_triple$ pycodestyle .

# Отправляем задачу в систему
1_middle_value_of_triple$ git add --all
1_middle_value_of_triple$ git commit
1_middle_value_of_triple$ git push
```