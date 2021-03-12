# Django poll app


## Задача:

Спроектировать и разработать API для системы опросов пользователей.

* Дополнительно реалезован функционал полноценного сайта

## Функционал для администратора системы:

* авторизация в системе (регистрация не нужна)
* добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
* добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

## Функционал для пользователей системы:

* получение списка активных опросов
* прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
* получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

## Окружение проекта:

* Django 2.2.10
* djangorestframework

# Документация API

## Чтобы получить токен пользователя:

* Request method: GET
* URL: http://localhost:8000/api/login/
* Body:
    * username:
    * password:
* Example:

```
curl --location --request GET 'http://localhost:8000/api/login/' \
--form 'username=%username' \
--form 'password=%password'
```

## Чтобы создать опрос:

* Request method: POST
* URL: http://localhost:8000/api/poll/create/
* Header:
   *  Authorization: Token userToken
* Body:
    * poll_name: name of poll
    * date_start: publication date can be set only when poll is created, format: YYYY-MM-DD HH:MM:SS
    * date_end: poll end date, format: YYYY-MM-DD HH:MM:SS
    * description: description of poll
* Example:

```
curl --location --request POST 'http://localhost:8000/api/poll/create/' \
--header 'Authorization: Token %userToken' \
--form 'poll_name=%poll_name' \
--form 'date_start=%date_start' \
--form 'date_end=%date_end \
--form 'description=%description'
```

## Обновить опрос:

* Request method: PATCH
* URL: http://localhost:8000/api/poll/update/[poll_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * poll_id
* Body:
    * poll_name: name of poll
    * date_end: poll end date, format: YYYY-MM-DD HH:MM:SS
    * description: description of poll
* Example:

```
curl --location --request PATCH 'http://localhost:8000/api/poll/update/[poll_id]/' \
--header 'Authorization: Token %userToken' \
--form 'poll_name=%poll_name' \
--form 'date_end=%date_end \
--form 'description=%description'
```

## Удалить опрос:

* Request method: DELETE
* URL: http://localhost:8000/api/poll/update/[poll_id]
* Header:
    * Authorization: Token userToken
* Param:
    * poll_id
Example:

```
curl --location --request DELETE 'http://localhost:8000/api/poll/update/[poll_id]/' \
--header 'Authorization: Token %userToken'
```

## Посмотреть все опросы:

* Request method: GET
* URL: http://localhost:8000/api/poll/view/
* Header:
    * Authorization: Token userToken
* Example:

```
curl --location --request GET 'http://localhost:8000/api/poll/view/' \
--header 'Authorization: Token %userToken'
```

## Просмотр текущих активных опросов:

* Request method: GET
* URL: http://localhost:8000/api/poll/view/active/
* Header:
    * Authorization: Token userToken
* Example:

```
curl --location --request GET 'http://localhost:8000/api/poll/view/active/' \
--header 'Authorization: Token %userToken'
```

## Создаем вопрос:

* Request method: POST
* URL: http://localhost:8000/api/question/create/
* Header:
    * Authorization: Token userToken
* Body:
    * poll: id of poll
    * question_text:
    * question_type: can be only `radiobutton`, `checkbox` or `Text`
* Example:

```
curl --location --request POST 'http://localhost:8000/api/question/create/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

## Обновляем вопрос:

* Request method: PATCH
* URL: http://localhost:8000/api/question/update/[question_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * question_id
* Body:
    * poll: id of poll
    * question_text: question
    * question_type: can be only `one`, `multiple` or `text`
* Example:

```
curl --location --request PATCH 'http://localhost:8000/api/question/update/[question_id]/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

## Удаляем вопрос:

* Request method: DELETE
* URL: http://localhost:8000/api/question/update/[question_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * question_id
* Example:

```
curl --location --request DELETE 'http://localhost:8000/api/question/update/[question_id]/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

## Создаем выбор:
* Request method: POST
* URL: http://localhost:8000/api/choice/create/
* Header:
    * Authorization: Token userToken
* Body:
    * choice_question: id of question
    * choice_text: choice
* Example:
```
curl --location --request POST 'http://localhost:8000/api/choice/create/' \
--header 'Authorization: Token %userToken' \
--form 'choice_question=%choice_question' \
--form 'choice_text=%choice_text'
```

## Обновляем выбор:
* Request method: PATCH
* URL: http://localhost:8000/api/choice/update/[choice_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * choice_id
* Body:
    * choice_question: id of question
    * choice_text: choice
* Example:
```
curl --location --request PATCH 'http://localhost:8000/api/choice/update/[choice_id]/' \
--header 'Authorization: Token %userToken' \
--form 'choice_question=%choice_question' \
--form 'choice_text=%choice_text'
```

## Удаляем выбор:

* Request method: DELETE
* URL: http://localhost:8000/api/choice/update/[choice_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * choice_id
* Example:

```
curl --location --request DELETE 'http://localhost:8000/api/choice/update/[choice_id]/' \
--header 'Authorization: Token %userToken' \
--form 'choice_question=%choice_question' \
--form 'choice_text=%choice_text'
```

## Создаем ответ:

* Request method: POST
* URL: http://localhost:8000/api/answer/create/
* Header:
    * Authorization: Token userToken
* Body:
    * poll: id of poll
    * question: id of question
    * choice: if question type is one or multiple then it’s id of choice else null
    * choice_text: if question type is text then it’s text based answer else null
* Example:

```
curl --location --request POST 'http://localhost:8000/api/answer/create/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question=%question' \
--form 'choice=%choice \
--form 'choice_text=%choice_text'
```

## Обновляем ответ:

* Request method: PATCH
* URL: http://localhost:8000/api/answer/update/[answer_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * answer_id
* Body:
    * poll: id of poll
    * question: id of question
    * choice: if question type is one or multiple then it’s id of choice else null
    * choice_text: if question type is text then it’s text based answer else null
* Example:

```
curl --location --request PATCH 'http://localhost:8000/api/answer/update/[answer_id]' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question=%question' \
--form 'choice=%choice \
--form 'choice_text=%choice_text'
```

## Удаляем ответ:

* Request method: DELETE
* URL: http://localhost:8000/api/answer/update/[answer_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * answer_id
* Example:

```
curl --location --request DELETE 'http://localhost:8000/api/answer/update/[answer_id]' \
--header 'Authorization: Token %userToken'
```

## Просматриваем ответы пользователя:

* Request method: GET
* URL: http://localhost:8000/api/answer/view/[user_id]/
* Param:
    * user_id
* Header:
    * Authorization: Token userToken
* Example:

```
curl --location --request GET 'http://localhost:8000/api/answer/view/[user_id]' \
--header 'Authorization: Token %userToken'
```
