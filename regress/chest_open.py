from altunityrunner import By

from alt_tester_python.base_test_case import BaseTestCase
from testing.cases.army.regress.get_resources import open_all_elements
from testing.cases.chest_open.common.chest_open_utils import ChestOpenUtils
from wrapper_specific import WrapperSpecific as Wrapper
from testing.cases.mail.common.mail_regress_utils import MailRegressUtils


def chest_open_skip_reward_steps_script(test: BaseTestCase, wrapper: Wrapper):
    open_all_elements(wrapper, wrapper.get_account_id(), 5, 1, 1)
    wrapper.sleep(15)  # Не удалять, т.к. требуется для обновления клиента

    # Читаем первое письмо на почте
    try:
        wrapper.tap_and_check("button_messages", [], ['inbox_list_window(Clone)'])
        wrapper.tap_and_check("inbox_item_letter(Clone)", [],
                              ["panel_inbox_letter_background", "panel_inbox_letter_header",
                               "image_head", "text_date", "panel_bottom"])
        wrapper.tap_and_check("button_inbox_letter_close", ["panel_inbox_letter_background", "icon_letter_not_readed"],
                              ["icon_letter_readed"])
        wrapper.tap_and_check("button_inbox_list_close", ["panel_inbox_list_background"],
                              ["button_messages"])
        # Проверяем, что уведомлений о новых письмах нет
        MailRegressUtils.check_notifications_absence(wrapper)
    except Exception as e:
        raise Exception("Unable to read first letter", e)

    # Проверка действительно ли начисляется награда из сундуков, когда пропускаются все шаги получения награды
    wrapper.tap_and_check("button_army", ["button_army"], ["toggle_units"], timeout_of_tap=15)
    cards = ['item_8_22', 'item_8_20', 'item_8_3']
    ChestOpenUtils.check_accrual_of_rewards(wrapper, cards, "item_11_14", 2, 1150002)
