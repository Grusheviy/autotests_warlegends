from alt_tester_python.base_test_case import BaseTestCase
from testing.cases.chest_open.common.chest_open_utils import ChestOpenUtils
from wrapper_specific import WrapperSpecific as Wrapper


def chest_open_different_chests_script(test: BaseTestCase, wrapper: Wrapper):
    # Проверка, что из разных сундуков награда реально зачисляется
    wrapper.tap_and_check("button_army", ["button_army"], ["toggle_units"])
    cards = ['item_8_1', 'item_8_42', 'item_8_41', 'item_8_12']
    ChestOpenUtils.check_accrual_of_rewards(wrapper, cards, "item_11_15", 0, 1150001)

    # Переходим на темную сторону
    wrapper.select_faction('DARK')

    wrapper.tap_and_check("button_army", ["button_army"], ["toggle_units"])
    cards = ['item_8_1001', 'item_8_1042', 'item_8_1041', 'item_8_1012']
    ChestOpenUtils.check_accrual_of_rewards(wrapper, cards, "item_11_1015", 0, 1250001)

    wrapper.tap_and_check("button_army", ["button_army"], ["toggle_units"])
    cards = ['item_8_1022', 'item_8_1020', 'item_8_1003']
    ChestOpenUtils.check_accrual_of_rewards(wrapper, cards, "item_11_1014", 2, 1250002)
