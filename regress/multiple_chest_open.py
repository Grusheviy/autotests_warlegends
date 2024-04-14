from altunityrunner import By
from alt_tester_python.base_test_case import BaseTestCase
from testing.cases.chest_open.common.chest_open_utils import ChestOpenUtils
from testing.cases.mail.common.mail_regress_utils import Letter, MailRegressUtils
from wrapper_specific import WrapperSpecific as Wrapper


def chest_open_multiple_script(test: BaseTestCase, wrapper: Wrapper):
    # Проверяем получение награды из нескольких сундуков
    # Используем команду на порт для получения почты с сундуком
    letter_with_chest = Letter('"COMMON"', '"Three chest with reward for bro"', '"Just open the three chest"',
                               '"CHEST"', 1150002, 3)
    letter_with_chest.send_message_with_reward(wrapper)

    cards_list_after = []
    cards_list_reward_in_chests = []

    # Переходим в почту в непрочитанное письмо
    wrapper.tap_and_check("button_messages", [], ['inbox_list_window(Clone)'])
    wrapper.tap_and_check("inbox_item_letter(Clone)", [],
                          ["panel_inbox_letter_background", "panel_inbox_letter_header",
                           "image_head", "text_date", "panel_bottom"])
    rewards_count_all = int(wrapper.wait_object_and_get_text(
        By.PATH, '//scrollview_rewards/viewport/list_rewards_content//panel_common_reward_currency(Clone)/'
                 'text_common_reward_currency_value').split(' ')[1])
    wrapper.tap_and_check('button_get', ['inbox_letter_window(Clone)'], [])

    # Открываем сундуки и получаем награды
    for i in range(rewards_count_all):
        wrapper.tap_and_check('rawimage_chestopen_chest_preview', ['button_chestopen_tap_to_open'],
                              ['text_chestopen_tap_to_continue', 'text_chestopen_rewards_count'], sleep_before_tap=1)

        # Пропускаем получение наград нажатием на кнопку "Пропустить"
        wrapper.tap_and_check('button_chestopen_skip_all', ['button_chestopen_skip_all'],
                              ['scrollview_chestopen_rewards_final', 'button_chestopen_take',
                               'text_chestopen_chests_count'], sleep_before_tap=1)
        wrapper.altdriver.wait_for_object(By.NAME, 'button_chestopen_take')

        cards_list_reward_in_chests.clear()
        # Записываем в массив значения наград из поля "У вас будет:" для сравнения
        rewards_list = wrapper.altdriver.find_objects(
            By.PATH, '//scrollview_chestopen_rewards_final/panel_chestopen_rewards_final_viewport/'
                     'panel_chestopen_rewards_final_content/item_chestopen_reward_final(Clone)')
        for rewards_count, rewards_in_list in enumerate(rewards_list, 1):
            rewards_in_chest = int(wrapper.wait_object_and_get_text(
                By.PATH, f'//panel_chestopen_rewards_final_viewport/'
                         f'panel_chestopen_rewards_final_content[{rewards_count}]//panel_item_count/'
                         f'image_item_count_lvlup/text_item_count').split('size> ')[1].split('/')[0])
            cards_list_reward_in_chests.append(rewards_in_chest)
            if rewards_count == 4:
                break
            wrapper.sleep(1)
        gold_reward = int(wrapper.wait_object_and_get_text(
            By.PATH, '//panel_chestopen_rewards_final_viewport/panel_chestopen_rewards_final_content[0]//'
                     'panel_item_count/image_item_count_lvlup/text_item_count'))
        cards_list_reward_in_chests.insert(0, gold_reward)

        # Забираем награду нажатием на кнопку "Забрать награды"
        wrapper.tap_and_check('button_chestopen_take', ['button_chestopen_take', 'text_chestopen_chests_count'], [],
                              sleep_before_tap=1)

    # Выходим из почты
    wrapper.tap_and_check("button_inbox_letter_close", ["panel_inbox_letter_background", "icon_letter_not_readed"],
                          ["icon_letter_readed"])
    wrapper.tap_and_check("button_inbox_list_close", ["panel_inbox_list_background"],
                          ["button_messages"])
    MailRegressUtils.check_notifications_absence(wrapper)

    # Заходим в армию для подсчета количества карточек и золота после получения наград из трех сундуков
    cards = ['item_8_22', 'item_8_20', 'item_8_3']
    wrapper.tap_and_check("button_army", ["button_army"], ["toggle_units"])
    ChestOpenUtils.counting_number_of_cards_and_gold(wrapper, cards_list_after, cards, "item_11_14", 2)

    # Сравниваем массивы
    if cards_list_reward_in_chests != cards_list_after:
        raise Exception(
            f' The number of cards does not match, cards_list_reward_in_chests={cards_list_reward_in_chests}, '
            f'cards_list_after={cards_list_after}')

    wrapper.tap_and_check("button_back", ["item_11_1"], ["button_army"])
