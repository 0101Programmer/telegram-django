<h2>PET проект представляет собой создание сайта по продаже бытовой техники на фреймворке "Django" и объединение его работы с телеграм ботом, который написан на библиотеке "aiogram".</h2>
<p>В качестве базы данных используется "PostgreSQL", подключение осуществляется через "DjangoORM" и "SQLAlchemy" (для запросов к БД через бота телеграм)</p>
<h3>Рассмотрим некоторые особенности проекта.</h3>
<h4>Для начала запустим сервер и перейдём по ссылке</h4>

![Снимок экрана 2025-02-01 115240](https://github.com/user-attachments/assets/0eca3c45-bdcc-43ee-a06e-b9d46f14ca37)

<h4>Пока что на главной странице пусто...</h4>

![Снимок экрана 2025-02-01 115254](https://github.com/user-attachments/assets/54a0f7ee-90ed-4f98-ae2d-6329bfe2e518)

<h4>...как и в базе данных</h4>

![Снимок экрана 2025-02-01 115308](https://github.com/user-attachments/assets/0870893f-a4f4-4399-89c7-40ec4b178d06)

<h4>Через админ-панель "Django" добавим товар в БД</h4>

![Снимок экрана 2025-02-01 115331](https://github.com/user-attachments/assets/47c91bd6-8ac5-44d5-b6b3-38083dfcc423)
<hr>

![Снимок экрана 2025-02-01 115345](https://github.com/user-attachments/assets/34b0e918-b5d8-4dac-8b02-fb295a86810d)

<h4>Модель продукта выглядит следующим образом:</h4>
<p>(по ней и опишем первый товар)</p>

![Снимок экрана 2025-02-01 115353](https://github.com/user-attachments/assets/b29b8b5a-f9fb-47c2-8213-e6c4a32d7231)

<h4>Запись готова</h4>

![Снимок экрана 2025-02-01 115519](https://github.com/user-attachments/assets/bd9b3d18-0589-475a-bc25-f70e5134964c)

<h4>Теперь на главной странице отображается товар</h4>

![Снимок экрана 2025-02-01 115532](https://github.com/user-attachments/assets/15be1a91-1ad3-4aff-b70a-407445039eff)

<h4>Чтобы посмотреть подробности достаточно перейти по ссылке, которая находится прямо в картинке товара</h4>

![capture_250201_115622](https://github.com/user-attachments/assets/c2ba6d27-658c-4303-a618-c1a20ddf1ac9)

<h4>Попадаем в категорию "игровые консоли". По следующему клику попадаем...</h4>

![capture_250201_115645](https://github.com/user-attachments/assets/9430e170-6cc1-4ae4-b1ba-8bac2afc6a53)

<h4>...на страницу конкретного товара</h4>
<p>Однако пока приобрести ничего нельзя (для этого нужно пройти регистрацию или войти в личный кабинет)</p>

![Снимок экрана 2025-02-01 115702](https://github.com/user-attachments/assets/62acbd6c-04a9-4678-b21f-55860b465840)

<p>Регистрацию можно пройти на сайте</p>

![Снимок экрана 2025-02-01 115750](https://github.com/user-attachments/assets/6daa07e2-30db-4b38-99d1-8f5a4a326a58)

<p>А также через телеграм. Взглянем поподробнее, для этого вернёмся в "PyCharm" и запустим бота</p>

![Снимок экрана 2025-02-01 115839](https://github.com/user-attachments/assets/c5becbe4-2480-4595-a5be-ebfaf07b7a78)
<hr>

![Снимок экрана 2025-02-01 115849](https://github.com/user-attachments/assets/b2da4190-2b39-4410-ac04-d81fca1c15a5)
<hr>

![Снимок экрана 2025-02-01 115922](https://github.com/user-attachments/assets/2d49197c-334f-4588-94b5-a607bd5f90a2)
<hr>

<h4>Пока что посмотреть на свои заказы не представляется возможным</h4>

![Снимок экрана 2025-02-01 115934](https://github.com/user-attachments/assets/b7f80704-a2a0-4664-a01e-f88592046467)

<p>(потому что таблица "User" пустая)</p>

![Снимок экрана 2025-02-01 115945](https://github.com/user-attachments/assets/ed16269a-69f2-4468-86aa-f7cfd1e00cfb)

<h4>Сейчас мы это исправим</h4>

![Снимок экрана 2025-02-01 120000](https://github.com/user-attachments/assets/970cf208-e34f-4dfa-bfa9-f656920f8faf)

<h4>На этом этапе запускается машина состояний, отвечающая за регистрацию пользователя</h4>
<p>В случае некорректно введённых данных нужная информация запрашивается повторно, пока пользователь не нажмёт на кнопку воврата в главное меню (или просто не введёт нужную информацию)</p>

![Снимок экрана 2025-02-01 120016](https://github.com/user-attachments/assets/bdf29c99-dd0d-41a4-af48-5132d46cec44)
<hr>

![Снимок экрана 2025-02-01 120036](https://github.com/user-attachments/assets/833218bd-700c-42be-a146-19b7e1b8a028)

<h4>В итоге получаем сообщение об успешной регистрации</h4>

![Снимок экрана 2025-02-01 120145](https://github.com/user-attachments/assets/6ec22519-af01-4e56-be87-818b76e228ff)

<h4>А в таблице уже отобразилась соответствующая запись</h4>

![Снимок экрана 2025-02-01 120311](https://github.com/user-attachments/assets/21fd9b11-98e6-46d0-a0b7-d499816477db)

<h4>На сайте теперь можно зайти под своим паролем и логином</h4>

![Снимок экрана 2025-02-01 120513](https://github.com/user-attachments/assets/f0b71999-ca01-42c8-85a6-63bd5c8febe0)

<h4>Попадаем в личный кабинет</h4>

![Снимок экрана 2025-02-01 120520](https://github.com/user-attachments/assets/1fe96840-a276-4943-b3c8-de6ba78a67a1)

<h4>Данные отображаются по конкретному ID пользователя из адресной строки</h4>

![Снимок экрана 2025-02-01 120529](https://github.com/user-attachments/assets/e382944c-7a7d-4990-b982-8bb52839fea7)

<h4>Если изменить ID вручную, то, конечно же, ничего не получится</h4>

![Снимок экрана 2025-02-01 120734](https://github.com/user-attachments/assets/2c88f62f-8053-4703-bacd-d59ace5b54a7)
![Снимок экрана 2025-02-01 120729](https://github.com/user-attachments/assets/c368ce04-00be-482a-a526-a48d2a97c6ae)

<h4>За это отвечает параметр ID текущей сессии, который обновился после авторизации</h4>

![Снимок экрана 2025-02-01 120712](https://github.com/user-attachments/assets/950a67a4-cc68-479a-90ce-984b85516c69)

<h4>Вернёмся к личному кабинету. Отсюда можно изменить личные данные</h4>

![Снимок экрана 2025-02-01 120745](https://github.com/user-attachments/assets/d3ec556f-28d0-428f-8172-abcfd866af33)

<h4>Например, имя</h4>

![Снимок экрана 2025-02-01 120806](https://github.com/user-attachments/assets/6ae140e3-02c8-4eea-b98d-ccb7713426fa)
<hr>

![Снимок экрана 2025-02-01 120813](https://github.com/user-attachments/assets/3602be46-a40a-4b44-97fa-428570b15378)


<h4>К слову, теперь, наконец-то, можно оформить заказ</h4>

![Снимок экрана 2025-02-01 120826](https://github.com/user-attachments/assets/030fe953-50ed-4f14-b597-9b1e886306aa)
<hr>

![Снимок экрана 2025-02-01 120833](https://github.com/user-attachments/assets/6b095dc6-30e2-4068-b09e-332a8a5077e5)
<hr>

![Снимок экрана 2025-02-01 120840](https://github.com/user-attachments/assets/1587d177-86de-4224-bb3c-f2647c54fb42)

<h4>Добавим 3 позиции в корзину</h4>

![Снимок экрана 2025-02-01 120848](https://github.com/user-attachments/assets/4c3c6f54-e994-42ef-a54c-dca08a5a9be7)

<h4>Они будут ждать "финального решения" в личном кабинете</h4>

![Снимок экрана 2025-02-01 120908](https://github.com/user-attachments/assets/fc5d103e-6b56-4c9a-b18f-fe8032c552d5)

<h4>В телеграме тоже отобразиться похожая таблица (при выборе соответствующего пункта меню)</h4>

![Снимок экрана 2025-02-01 120931](https://github.com/user-attachments/assets/2233442e-0d65-457f-b86d-3f7651106c2f)


<h4>Внесём изменения в заказ</h4>

![Снимок экрана 2025-02-01 120952](https://github.com/user-attachments/assets/36667c80-8934-4b4c-9440-7e22550de8b0)
<hr>

![Снимок экрана 2025-02-01 120959](https://github.com/user-attachments/assets/38273892-2182-4ee0-9aee-300afcbe375d)

<hr>

![Снимок экрана 2025-02-01 121009](https://github.com/user-attachments/assets/4bc14ad6-2718-419b-962d-2c394d207a83)

<h4>Таблица в телеграм тоже обновилась</h4>

![Снимок экрана 2025-02-01 121017](https://github.com/user-attachments/assets/26e72789-a254-4050-b210-c34430e5e150)

<h4>"Оплатим" заказ</h4>

![Снимок экрана 2025-02-01 121042](https://github.com/user-attachments/assets/f4e9d888-46ab-47ae-b1be-a61e32901d20)

<h4>Не забывая указать корректные данные</h4>

![Снимок экрана 2025-02-01 121046](https://github.com/user-attachments/assets/35e566ef-49f2-4591-a591-aec0ae9df5a1)
<hr>

![Снимок экрана 2025-02-01 121055](https://github.com/user-attachments/assets/1eab3654-34ae-4ab0-a755-7d63a902b8be)
<hr>

![Снимок экрана 2025-02-01 121059](https://github.com/user-attachments/assets/3a1a6dfc-1f27-4216-8717-cfd7274bf7b6)
<hr>

![Снимок экрана 2025-02-01 121111](https://github.com/user-attachments/assets/b8f384d5-434e-4307-810f-b2783952953a)

<h4>После оплаты можно оставить отзыв</h4>

![Снимок экрана 2025-02-01 121118](https://github.com/user-attachments/assets/5ca93d6e-e51f-4c7a-8acf-1b78f7e908ec)
<hr>

![Снимок экрана 2025-02-01 121128](https://github.com/user-attachments/assets/f2e3ea99-8976-4fdd-abad-e6607da2fa18)
<hr>

![Снимок экрана 2025-02-01 121155](https://github.com/user-attachments/assets/f4b629fe-d661-4180-903c-16208b1fa56f)
<hr>

<h4>Валидация данных тоже присутствует</h4>

![Снимок экрана 2025-02-01 121200](https://github.com/user-attachments/assets/6b07d004-f12d-4f67-b7b7-07f7848d36b1)
<hr>

![Снимок экрана 2025-02-01 121231](https://github.com/user-attachments/assets/454aea1e-5379-489c-a428-19d0b51ac979)

<h4>1 отзыв на 1 заказ</h4>

![Снимок экрана 2025-02-01 121239](https://github.com/user-attachments/assets/6650383e-ccac-4b60-8474-f2985a8fdecb)

<h4>В базе данных у соответствующего продукта уже появилась запись в столбце с отзовами</h4>

![Снимок экрана 2025-02-01 121257](https://github.com/user-attachments/assets/e25257c2-8418-4d93-9832-d4b5f5742ada)

<h4>Также отзыв можно увидеть на странице товара</h4>

![Снимок экрана 2025-02-01 121315](https://github.com/user-attachments/assets/20f88e8e-b981-4b5e-a1ea-eb0d1281ae84)

<h4>Теперь сделаем заказ из телеграм. Создадим новый товар для разнообразия, но сделаем это не через "Django", а через "SQLAlchemy ORM"</h4>
<p>(для этого через "automap_base" получим схемы существующих моделей созданных с помощью "Django")</p>

![Снимок экрана 2025-02-01 123310](https://github.com/user-attachments/assets/1096a249-a86b-474a-9db4-af6f10fa9f21)
<hr>

![Снимок экрана 2025-02-01 123318](https://github.com/user-attachments/assets/8b8705d3-e9ab-4ca0-95de-cb8226582963)
<hr>

![Снимок экрана 2025-02-01 131902](https://github.com/user-attachments/assets/63f6e750-e241-4371-b885-f309b8b306fe)


<h4>Товар создан, можно заказывать</h4>

![Снимок экрана 2025-02-01 131920](https://github.com/user-attachments/assets/cf8ebba0-4b79-4a2a-9927-c2c119b7d717)

<h4>Вернёмся к боту. Оформляем заказ</h4>

![Снимок экрана 2025-02-01 132430](https://github.com/user-attachments/assets/d5a4d876-f2fd-4aa7-acee-70e9ce5065fd)

<h4>Прописываем необходимые параметры (за заказ тоже отвечает машина состояний)</h4>

![Снимок экрана 2025-02-01 133056](https://github.com/user-attachments/assets/081cd924-4af8-458b-aba5-f47f5d3f4c5b)

<p>Карта, которой был оплачен заказ на сайте теперь появилась как подсказка при текущем заказе</p>

![Снимок экрана 2025-02-01 133118](https://github.com/user-attachments/assets/a1f76e09-aec8-47bf-ae7e-41e28d62d102)

<h4>"Оплачиваем"</h4>

![Снимок экрана 2025-02-01 133149](https://github.com/user-attachments/assets/4364f844-05da-4cda-aa67-f5d734015096)

<h4>Таблица пополнилась новым товаром</h4>

![Снимок экрана 2025-02-01 133812](https://github.com/user-attachments/assets/199a4dfb-6883-443e-9263-d6f44795dab7)


<h4>И в личном кабинете на сайте также отобразился новый заказ</h4>

![Снимок экрана 2025-02-01 133836](https://github.com/user-attachments/assets/fc12faa2-7756-4268-86c4-6b3bbc782c3f)

