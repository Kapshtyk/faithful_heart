from enum import Enum


class BOT_ANSWERS(str, Enum):
    greeting = (
        "Приветствую! Я бот приюта для животных. Готовы ли вы представиться?"
    )
    greeting_partial_data = "Рады приветствовать вас снова! Готовы ли вы предоставить дополнительную информацию?"
    greeting_full_data = "Рады приветствовать вас снова! Чем могу помочь?"
    permission = (
        f"""Жаль, без этой информации нам будет сложнее держать вас в курсе последних новостей.\n"""
        """Может быть вы хотели получить ответ на ваш вопрос либо узнать дополнительную информацию о нас?"""
    )
    first_name = "Введите ваш имя:"
    second_name = "Введите ваше отчество:"
    surname = "Введите вашу фамилию:"
    email = "Введите ваш email:"
    phone_number = "Нажмите кнопку 'Отправить номер телефона', чтобы поделиться номером, на который зарегистрирован ваш аккаунт, либо введите ваш номер телефона (в формате 7ХХХХХХХХХХ):"
    send_contact = "Отправить номер телефона"
    registration_message = (
        f"""Спасибо за регистрацию!\n"""
        """Теперь вы можете узнать дополнительную информацию о нас либо получить ответ на свой вопрос."""
    )
    shelter = "Информация о приюте"
    questions = "Задать вопрос"
    questions_title = "Что бы Вы хотели узнать?"
    faq = "Часто задаваемые вопросы"
    faq_reply = "Список часто задаваемых вопросов"
    info = "Данные приюта"
    info_reply = "Подробная информация о контактных данных приюта"
    needs = "Нужды приюта"
    needs_reply = """Вы можете заказать и оплатить покупку в любом интернет-магазине С ДОСТАВКОЙ прямо в приют.
    Адрес доставки : ул. Автовская, д. 31, лит И.
    Время: с 10:00 до 21:00.
    Тел. для курьера: +7 (952) 209-39-51 Алиева Инна Петровна
    ПОЖАЛУЙСТА, ПРОСЛЕДИТЕ, ЧТОБЫ ЗАКАЗ БЫЛ ОПЛАЧЕН, НЕОПЛАЧЕННЫЕ ЗАКАЗЫ НЕ ПРИНИМАЮТСЯ
    """
    unique_question = "Задать свой вопрос"
    enter_unique_question = "Пожалуйста, введите Ваш вопрос"
    unique_question_reply = (
        "Спасибо за вопрос, мы обязательно свяжемся с Вами."
    )
    cancel = "Отмена"
    yes = "Да"
    no = "Нет"
    try_again = "Попробуйте ввести данные еще раз"
    nothing_to_cancel = "Отменять нечего, мы и так в самом начале :)"
    choose_correct_category = "Пожалуйста, выберите правильную категорию, либо нажмите на кнопку 'Отмена'"
    choose_correct_option = "Пожалуйста, выберите корректный вариант"
    enter_correct_value = "Пожалуйста, введите корректное значение"
    enter_correct_question = "Пожалуйста, введите корректный вопрос, либо нажмите на кнопку 'Отмена'"
    validation_error = "Ошибка валидации, пожалуйста, попробуйте еще раз"
    update_error = "Ошибка, попробуйте еще раз позднее"
    user_creation_error = (
        "Ошибка создания пользователя, пожалуйста, попробуйте еще раз"
    )
    question_creation_error = (
        "При создании вопроса возникла ошибка, пожалуйста, попробуйте еще раз"
    )
    question_validation_error = (
        "Ошибка валидации вопроса - вопрос содержит запрещённые слова"
    )
    something_went_wrong = (
        "Что-то пошло не так, пожалуйста, попробуйте еще раз"
    )
    monetary_aid = "Оказать финасовую помощь"
    monetary_aid_title = "Как вы хотите оказать финансовую помощь?"
    guardianship = "Участвовать в попечительской программе"
    guardianship_url = (
        "https://predannoeserdce.ru/programmy-prijuta/popechitelstvo/"
    )
    donation = "Сделать пожертвование"
    donation_url = "https://predannoeserdce.ru/sms-pozhertvovanie/)"
    animals = "Посмотреть животных"
    animals_title = "Посмотреть животных, которым нужна помощь"
    animals_url = "https://predannoeserdce.ru/catalog/"
    update_data = "Нажмите 'Обновить' если хотите обновить свои данные, 'Удалить' для их удаления и 'Назад' для возврата к главному меню"
    update = "Обновить"
    delete = "Удалить"
    back = "Назад"
    data_back_message = "Хорошо, вы сможете вернуться к изменению своих данных позже выбрав соответствующую команду в меню, а пока можете выбрать действие"


PAGINATION = 3
